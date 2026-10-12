"""Build the six selected MachineMaker manuals into one portable HTML collection."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import quote, unquote
from urllib.request import Request, urlopen
import hashlib
import json
import os
import posixpath
import re
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
PUBLICATION = ROOT.parent
SITE = ROOT / "html"
WORK = ROOT / "build-work"
ADMIN = ROOT / "admin"
TOOLS = PUBLICATION / "audit-2026-10-08/tools"
DOCFX = TOOLS / "docfx/docfx.exe"
for path in [SITE, WORK, ADMIN]:
    path.mkdir(exist_ok=True)
sys.path.insert(0, str(TOOLS / "python"))
from bs4 import BeautifulSoup

GUIDES = [
    {"key": "milling-en", "kind": "milling", "language": "en", "title": "MachineMaker — Milling Machines", "label": "Фрезерные станки — EN", "pages": 31,
     "source": str(PUBLICATION / "ency-docs/docs/machinemaker/machines"), "format": "legacy-docfx", "family": "ency-docs",
     "source_ref": "EncySoftware/public-docs v3/features/machinemaker-manuals", "source_sha": "673aee9b82d91c283e3d3c7b34390548b317c7af", "source_date": "2026-09-22"},
    {"key": "milling-ru", "kind": "milling", "language": "ru", "title": "MachineMaker — Фрезерные станки", "label": "Фрезерные станки — RU", "pages": 33,
     "source": str(PUBLICATION / "sprutcam-docs/docs/machinemaker/machines"), "format": "legacy-docfx", "family": "sprutcam-docs",
     "source_ref": "spruttechnology/public-docs v20/features/machinemaker-publication", "source_sha": "c193b5a8f3c0f7b0e623895724c3168a00177cbd", "source_date": "2026-09-22"},
    {"key": "robots-en", "kind": "robots", "language": "en", "title": "MachineMaker — Robots", "label": "Роботы — EN", "pages": 47,
     "source": str(PUBLICATION / "mm-review-2026-10-09/robots-en/main"), "format": "docfx",
     "source_ref": "docs-work MachineMaker/Robots/en/v3", "source_sha": "76e60785c902c4cc11b3f7b0d3878ae7d1d2ed5b", "source_date": "2026-10-09 snapshot"},
    {"key": "robots-ru", "kind": "robots", "language": "ru", "title": "MachineMaker — Роботы", "label": "Роботы — RU", "pages": 47,
     "source": str(PUBLICATION / "mm-review-2026-10-09/robots-ru/main"), "format": "docfx",
     "source_ref": "docs-work MachineMaker/Robots/ru/v20", "source_sha": "28e11d7f52578fc6e09006bf31a2f63319f9e810", "source_date": "2026-10-09 snapshot"},
    {"key": "turnmill-en", "kind": "turnmill", "language": "en", "title": "MachineMaker — Turn-Milling Machines", "label": "Токарно-фрезерные станки — EN", "pages": 25,
     "source": str(WORK / "turnmill-en/main"), "format": "docfx-recovered-html",
     "source_ref": "https://docs.encycam.com/MachineMaker/1/turnmill/en/1.html", "source_sha": None, "source_date": "2026-10-09 recovered original"},
    {"key": "turnmill-ru", "kind": "turnmill", "language": "ru", "title": "MachineMaker — Токарно-фрезерные станки", "label": "Токарно-фрезерные станки — RU", "pages": 25,
     "source": str(PUBLICATION / "mm-review-2026-10-09/machines-ru/main"), "format": "docfx",
     "source_ref": "docs-work MachineMaker/Machines/ru/v20", "source_sha": "8962c6af3afd229b2f69b9c5502fa01982975c70", "source_date": "2026-10-09 snapshot"},
]


def copy_source(source, destination):
    if not destination.exists():
        shutil.copytree(source, destination, ignore=shutil.ignore_patterns("out", "obj", "build", "pdf", "_pdf", "__pycache__", ".git"))


def build(guide):
    source = Path(guide["source"])
    output = SITE / guide["kind"] / guide["language"]
    if guide["format"] == "original-html":
        shutil.copytree(source, output, dirs_exist_ok=True)
        guide["entry"] = guide["kind"] + "/" + guide["language"] + "/1.html"
        guide["articles"] = [p["file"] for p in json.loads((source.parent / "pages.json").read_text(encoding="utf-8"))]
        guide["build_exit"] = 0
        guide["build_method"] = "Byte-preserving copy of recovered original HTML"
        print(guide["key"], "copied original HTML", flush=True)
        return guide
    if guide["format"] == "docfx-recovered-html":
        project = source
        conversion = json.loads((ADMIN / "turnmill-en-docfx-conversion.json").read_text(encoding="utf-8"))
        guide["articles"] = [page["file"] for page in conversion["pages"]]
    elif guide["format"] == "legacy-docfx":
        project = WORK / guide["key"] / "docs/machinemaker/machines"
        copy_source(source, project)
        template = PUBLICATION / guide["family"] / "docs/_common/templates/custom"
        copy_source(template, WORK / guide["key"] / "docs/_common/templates/custom")
        guide["articles"] = ["src/" + path.stem + ".html" for path in sorted((source / "src").glob("*.md"))]
    else:
        project = WORK / guide["key"] / "main"
        copy_source(source, project)
        manifest = json.loads((source / "manifest.json").read_text(encoding="utf-8-sig"))
        guide["articles"] = [Path(page["target"]).with_suffix(".html").as_posix() for page in manifest["pages"].values()]
    config_path = project / "docfx.json"
    config = json.loads(config_path.read_text(encoding="utf-8-sig"))
    config["build"].pop("dest", None)
    config["build"]["globalMetadata"].update({"_appName": guide["title"], "_appTitle": guide["title"], "_appFooter": guide["title"], "_lang": guide["language"]})
    config_path.write_text(json.dumps(config, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    environment = os.environ.copy()
    environment["PATH"] = "C:/Program Files/dotnet" + os.pathsep + environment.get("PATH", "")
    environment["DOTNET_CLI_HOME"] = str(TOOLS / "dotnet-home")
    environment["DOTNET_CLI_TELEMETRY_OPTOUT"] = "1"
    arguments = [str(DOCFX), "build", str(config_path), "--output", str(output)]
    if (project / "doc-profile.json").exists():
        profile = json.loads((project / "doc-profile.json").read_text(encoding="utf-8-sig"))
        arguments += ["--metadata", "_documentationVersion=" + ".".join(str(profile[p]) for p in ["version", "minor", "patch"])]
    log_path = ADMIN / (guide["key"] + "-build.log")
    with log_path.open("w", encoding="utf-8") as log:
        result = subprocess.run(arguments, cwd=project, env=environment, stdout=log, stderr=subprocess.STDOUT)
    guide["build_exit"] = result.returncode
    guide["build_method"] = "DocFX 2.78.2 HTML build from isolated source copy"
    if result.returncode:
        raise RuntimeError(guide["key"] + " failed; inspect " + str(log_path))
    log = log_path.read_text(encoding="utf-8")
    guide["warnings"] = int(re.search(r"(\d+) warning\(s\)", log).group(1))
    guide["errors"] = int(re.search(r"(\d+) error\(s\)", log).group(1))
    # The generated build manifest contains local build paths, not site content.
    build_manifest = output / "manifest.json"
    if build_manifest.is_file():
        build_manifest.unlink()
    entry = "1.html" if guide["format"] == "docfx-recovered-html" else "src/index.html"
    (output / "index.html").write_text('<!doctype html><meta charset="utf-8"><meta http-equiv="refresh" content="0;url=' + entry + '"><a href="' + entry + '">' + guide["title"] + '</a>', encoding="utf-8")
    guide["entry"] = guide["kind"] + "/" + guide["language"] + "/" + entry
    print(guide["key"], "build", result.returncode, "warnings", guide["warnings"], "pages", len(guide["articles"]), flush=True)
    return guide


if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=3) as executor:
        built = list(executor.map(build, GUIDES))
    for guide in built:
        if len(guide["articles"]) != guide["pages"]:
            raise RuntimeError("Unexpected article count for " + guide["key"])
    (ADMIN / "inputs.json").write_text(json.dumps({"built_at": datetime.now(timezone.utc).isoformat(), "guides": built}, ensure_ascii=False, indent=2), encoding="utf-8")
    (ROOT / "guides.json").write_text(json.dumps(built, ensure_ascii=False, indent=2), encoding="utf-8")
    print("Built", len(built), "manuals,", sum(g["pages"] for g in built), "articles.", flush=True)
