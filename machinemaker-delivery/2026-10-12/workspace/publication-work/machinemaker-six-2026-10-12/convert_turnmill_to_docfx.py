"""Render the recovered English TurnMilling text in the shared DocFX shell, without Trevisan."""
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import unquote, urlsplit, urlunsplit
import copy
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
PUBLICATION = ROOT.parent
SOURCE = ROOT / "html/turnmill/en"
PROJECT = ROOT / "build-work/turnmill-en/main"
OUTPUT = ROOT / "turnmill-docfx-output"
BACKUP = ROOT / "previous-turnmill-en-html"
ADMIN = ROOT / "admin"
TOOLS = PUBLICATION / "audit-2026-10-08/tools"
sys.path.insert(0, str(TOOLS / "python"))
from bs4 import BeautifulSoup
from PIL import Image


def sha(data):
    return hashlib.sha256(data).hexdigest()


def normalized(element):
    return " ".join(element.get_text(" ", strip=True).split())


def write_json(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def prepare_and_build():
    if BACKUP.exists() or OUTPUT.exists() or PROJECT.exists():
        raise RuntimeError("A conversion workspace already exists; inspect it before repeating the import")
    PROJECT.mkdir(parents=True)
    soup = BeautifulSoup((SOURCE / "toc.html").read_text(encoding="utf-8"), "html.parser")
    toc_nav = soup.select_one("nav.ht-pages-nav > ul")
    guides = json.loads((ROOT / "guides.json").read_text(encoding="utf-8"))
    guide = next(g for g in guides if g["key"] == "turnmill-en")
    pages = [name for name in guide["articles"] if name != "73.html"]
    assert len(pages) == 25
    report = {"converted_at": datetime.now(timezone.utc).isoformat(), "source": "previous-turnmill-en-html/",
              "source_origin": guide["source_ref"], "template": "Same custom DocFX template as turnmill-ru",
              "removed": [{"file": "73.html", "title": "Trevisan Machine", "sha256": sha((SOURCE / "73.html").read_bytes())}],
              "pages": [], "resources": {}, "errors": []}

    def toc_items(ul):
        result = []
        for li in ul.find_all("li", recursive=False):
            a = li.find("a", recursive=False)
            if not a or a.get("href") == "73.html":
                continue
            name = a.get("href")
            heading_soup = BeautifulSoup((SOURCE / name).read_text(encoding="utf-8"), "html.parser")
            title = heading_soup.select_one(".ht-content-header h1").get_text(" ", strip=True)
            item = {"name": title, "href": str(Path(name).with_suffix(".md"))}
            child = li.find("ul", recursive=False)
            if child:
                item["items"] = toc_items(child)
            result.append(item)
        return result

    toc = [{"name": "MachineMaker User Manual", "href": "1.md"}] + toc_items(toc_nav)
    # JSON is valid YAML and preserves the complete nesting without a YAML dependency.
    write_json(PROJECT / "toc.yml", toc)
    for name in pages:
        raw = (SOURCE / name).read_bytes()
        soup = BeautifulSoup(raw.decode("utf-8-sig"), "html.parser")
        content = copy.deepcopy(soup.select_one("#main-content"))
        heading = soup.select_one(".ht-content-header h1")
        title = heading.get_text(" ", strip=True)
        before = normalized(content)
        page_report = {"file": name, "title": title, "source_sha256": sha(raw), "body_sha256": sha(before.encode("utf-8")),
                       "ids": sorted({el["id"] for el in content.select("[id]")}),
                       "heading_id": heading.get("id"), "image_sources": [img.get("src") for img in content.select("img")],
                       "links": [a.get("href") for a in content.select("a[href]") if a.get_text(strip=True)]}
        for container in reversed(content.select(".scroll-expand-container")):
            control = container.select_one(".scroll-expand-control")
            body = container.select_one(".scroll-expand-content")
            if control is None or body is None:
                continue
            details = soup.new_tag("details", attrs={"class": "scroll-expand-container"})
            if container.get("id"):
                details["id"] = container["id"]
            summary = soup.new_tag("summary")
            summary.string = (control.select_one(".scroll-expand-control-text") or control).get_text(" ", strip=True)
            details.append(summary)
            details.append(body.extract())
            container.replace_with(details)
        for element in content.select("[href], [src], [poster]"):
            for attr in ["href", "src", "poster"]:
                if not element.get(attr):
                    continue
                parts = urlsplit(element[attr])
                if parts.scheme or parts.netloc or not parts.path:
                    continue
                relative = unquote(parts.path)
                if relative in pages:
                    element[attr] = urlunsplit(("", "", str(Path(relative).with_suffix(".md")), parts.query, parts.fragment))
                    continue
                path = (SOURCE / relative).resolve()
                if not path.is_relative_to(SOURCE.resolve()) or not path.is_file():
                    raise RuntimeError("Missing source resource: " + relative)
                target = PROJECT / relative
                target.parent.mkdir(parents=True, exist_ok=True)
                if not target.exists():
                    shutil.copy2(path, target)
                report["resources"][relative] = {"sha256": sha(path.read_bytes()), "bytes": path.stat().st_size}
        for image in content.select("img"):
            original = SOURCE / unquote(urlsplit(image["src"]).path)
            with Image.open(original) as bitmap:
                real_width, real_height = bitmap.size
            width = int(image.get("width", real_width))
            height = int(image.get("height", real_height))
            inline = width <= 64 and height <= 64
            classes = list(image.get("class", [])) + (["doc-inline"] if inline else ["doc-image"])
            image["class"] = classes
            image["style"] = "--doc-image-width:" + str(width if inline else min(width, 800)) + "px"
            if not inline and image.parent.name != "a":
                a = soup.new_tag("a", href=image["src"], attrs={"class": "doc-image-link", "target": "_blank", "rel": "noopener", "title": "Open full-size image"})
                image.wrap(a)
        assert normalized(content) == before, name
        wrapper = soup.new_tag("div", id="ht-wrap-container")
        article = soup.new_tag("div", id="ht-content", attrs={"class": "ht-content"})
        header = soup.new_tag("div", attrs={"class": "ht-content-header"})
        h1 = soup.new_tag("h1")
        h1.string = title
        if heading.get("id"):
            h1["id"] = heading["id"]
        header.append(h1)
        article.append(header)
        article.append(content)
        wrapper.append(article)
        markdown = "---\ntitle: " + json.dumps(title, ensure_ascii=False) + "\n---\n\n<link rel=\"stylesheet\" href=\"assets/manual.css\">\n\n" + str(wrapper) + "\n"
        (PROJECT / Path(name).with_suffix(".md")).write_text(markdown, encoding="utf-8-sig", newline="\r\n")
        report["pages"].append(page_report)
    shared = ROOT / "build-work/turnmill-ru/main/template/custom"
    shutil.copytree(shared, PROJECT / "template/custom")
    navbar = PROJECT / "template/custom/partials/navbar.tmpl.partial"
    navbar_text = navbar.read_text(encoding="utf-8")
    navbar_text = navbar_text.replace("{{#_nav}}\n          {{>partials/navbar-li}}\n        {{/_nav}}", '<ul class="nav level1 navbar-nav"><li><a href="{{_rel}}1.html" title="MachineMaker — Turn-Milling Machines">MachineMaker — Turn-Milling Machines</a></li></ul>')
    navbar.write_text(navbar_text, encoding="utf-8")
    (PROJECT / "template/custom/conceptual.extension.js").write_text("exports.postTransform = function(model) { model._disableToc = false; if (!model._rel) model._rel = './'; return model; };\n", encoding="utf-8")
    assets = PROJECT / "assets"
    assets.mkdir(exist_ok=True)
    css = (ROOT / "build-work/milling-en/docs/machinemaker/machines/src/assets/manual.css").read_text(encoding="utf-8-sig")
    css += "\n#main-content h1.heading {font-size:23px;margin:32px 0 16px;}\n"
    (assets / "manual.css").write_text(css, encoding="utf-8")
    shutil.copy2(SOURCE / "MMUM18TurnMill.png", assets / "machinemaker.png")
    config = {"build": {"content": [{"files": ["*.md", "toc.yml"]}],
              "resource": [{"files": ["images/**", "attachments/**", "assets/**"]}],
              "globalMetadata": {"_appName": "MachineMaker — Turn-Milling Machines", "_appTitle": "MachineMaker — Turn-Milling Machines",
                                 "_appFooter": "MachineMaker — Turn-Milling Machines", "_lang": "en", "_enableSearch": True,
                                 "_disableContribution": True, "_appLogoPath": "assets/machinemaker.png", "_appFaviconPath": "assets/machinemaker.png"},
              "postProcessors": ["ExtractSearchIndex"], "template": ["statictoc", "template/custom"], "markdownEngineName": "markdig"}}
    write_json(PROJECT / "docfx.json", config)
    env = os.environ.copy()
    env["PATH"] = "C:/Program Files/dotnet" + os.pathsep + env.get("PATH", "")
    env["DOTNET_CLI_HOME"] = str(TOOLS / "dotnet-home")
    env["DOTNET_CLI_TELEMETRY_OPTOUT"] = "1"
    log = ADMIN / "turnmill-en-build.log"
    with log.open("w", encoding="utf-8") as stream:
        result = subprocess.run([str(TOOLS / "docfx/docfx.exe"), "build", str(PROJECT / "docfx.json"), "--output", str(OUTPUT)], env=env, cwd=PROJECT, stdout=stream, stderr=subprocess.STDOUT)
    if result.returncode:
        raise RuntimeError("DocFX failed; inspect " + str(log))
    output_log = log.read_text(encoding="utf-8")
    report["build_warnings"] = int(re.search(r"(\d+) warning\(s\)", output_log).group(1))
    report["build_errors"] = int(re.search(r"(\d+) error\(s\)", output_log).group(1))
    for page in report["pages"]:
        path = OUTPUT / page["file"]
        soup = BeautifulSoup(path.read_text(encoding="utf-8-sig"), "html.parser")
        content = soup.select_one("#main-content")
        assert sha(normalized(content).encode("utf-8")) == page["body_sha256"], page["file"]
        assert [i.get("src") for i in content.select("img")] == page["image_sources"], page["file"]
        assert Counter(a.get("href") for a in content.select("a[href]") if a.get_text(strip=True)) == Counter(page["links"]), page["file"]
        page["rendered_sha256"] = sha(path.read_bytes())
    for relative, expected in report["resources"].items():
        assert sha((OUTPUT / relative).read_bytes()) == expected["sha256"], relative
    (OUTPUT / "manifest.json").unlink(missing_ok=True)
    (OUTPUT / "index.html").write_text('<!doctype html><meta charset="utf-8"><meta http-equiv="refresh" content="0;url=1.html"><a href="1.html">MachineMaker — Turn-Milling Machines</a>', encoding="utf-8")
    if (OUTPUT / "73.html").exists():
        raise RuntimeError("Excluded chapter was rendered")
    # Both moves are confined to this collection; retain the complete previous book for provenance.
    for path in [SOURCE, OUTPUT, BACKUP]:
        assert path.resolve().is_relative_to(ROOT.resolve())
    SOURCE.rename(BACKUP)
    OUTPUT.rename(SOURCE)
    guide.update({"format": "docfx-recovered-html", "pages": 25, "articles": pages,
                  "source": str(PROJECT), "title": "MachineMaker — Turn-Milling Machines", "build_method": "DocFX 2.78.2 using the original English article bodies and the shared TurnMilling template",
                  "build_exit": 0, "warnings": report["build_warnings"], "errors": report["build_errors"]})
    write_json(ROOT / "guides.json", guides)
    inputs = json.loads((ADMIN / "inputs.json").read_text(encoding="utf-8"))
    inputs["guides"] = guides
    inputs["turnmill_en_docfx_conversion"] = "turnmill-en-docfx-conversion.json"
    write_json(ADMIN / "inputs.json", inputs)
    revision = json.loads((ADMIN / "content-changes.json").read_text(encoding="utf-8"))
    write_json(ADMIN / "link-revision-before-docfx.json", revision)
    superseded = [x for x in revision["changes"] if x["path"].startswith("html/turnmill/en/")]
    revision["changes"] = [x for x in revision["changes"] if x not in superseded]
    revision["superseded_by_docfx_conversion"] = superseded
    revision["decisions"]["turnmill_en_docfx"] = "Convert the recovered English book to the shared DocFX template, preserve the 25 remaining article URLs and content, exclude Trevisan"
    write_json(ADMIN / "content-changes.json", revision)
    write_json(ADMIN / "turnmill-en-docfx-conversion.json", report)
    print("English TurnMilling converted: 25 pages; original article text, links and resource bytes verified; Trevisan excluded.", flush=True)
    print("DocFX warnings:", report["build_warnings"], "errors:", report["build_errors"], flush=True)


if __name__ == "__main__":
    prepare_and_build()
