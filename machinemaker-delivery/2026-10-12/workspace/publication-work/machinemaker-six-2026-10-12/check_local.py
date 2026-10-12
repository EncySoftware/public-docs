"""Validate all six rendered manuals and their portable local dependencies."""
from pathlib import Path
from urllib.parse import unquote, urlsplit, urlunsplit, parse_qs, urlencode
from zipfile import ZipFile
import hashlib
import json
import re
import sys

ROOT = Path(__file__).resolve().parent
SITE = ROOT / "html"
ADMIN = ROOT / "admin"
guides = json.loads((ROOT / "guides.json").read_text(encoding="utf-8"))
sys.path.insert(0, str(ROOT.parent / "audit-2026-10-08/tools/python"))
from bs4 import BeautifulSoup

errors = []
externals = {}
pages = []
soups = {}
file_map = {p.relative_to(SITE).as_posix().casefold(): p.relative_to(SITE).as_posix() for p in SITE.rglob("*") if p.is_file()}
for guide in guides:
    output = SITE / guide["kind"] / guide["language"]
    for relative in guide["articles"]:
        path = output / relative
        soup = BeautifulSoup(path.read_text(encoding="utf-8-sig"), "html.parser")
        soups[path.resolve()] = soup
        article = soup.select_one("article.content") or soup.select_one("#main-content")
        if not article:
            errors.append({"guide": guide["key"], "page": relative, "error": "missing-article"})
            continue
        pages.append({"guide": guide["key"], "path": path.relative_to(SITE).as_posix()})
        for element in soup.select("a[href],img[src],script[src],link[href],iframe[src]"):
            raw = element.get("href", element.get("src", ""))
            if not raw or raw.startswith(("javascript:", "data:", "mailto:", "tel:")):
                continue
            url = urlsplit(raw)
            if url.scheme or url.netloc:
                if element.name in {"a", "iframe"} and element in article.descendants:
                    externals.setdefault(raw, []).append({"guide": guide["key"], "page": path.relative_to(SITE).as_posix(), "text": element.get_text(" ", strip=True)})
                elif element.name == "img":
                    errors.append({"guide": guide["key"], "page": relative, "error": "nonlocal-image", "target": raw})
                continue
            target = (path.parent / unquote(url.path)).resolve() if url.path else path.resolve()
            if target.is_dir():
                target = target / "index.html"
            if not target.is_relative_to(SITE.resolve()) or not target.is_file():
                errors.append({"guide": guide["key"], "page": relative, "error": "missing-local-target", "target": raw})
                continue
            spelling = target.relative_to(SITE.resolve()).as_posix()
            if file_map.get(spelling.casefold()) != spelling:
                errors.append({"guide": guide["key"], "page": relative, "error": "path-case-mismatch", "target": raw, "actual": file_map.get(spelling.casefold())})
            # HTML defines #top as the top of the document even without an id.
            if url.fragment and unquote(url.fragment).casefold() != "top" and target.suffix.lower() == ".html":
                if target not in soups:
                    soups[target] = BeautifulSoup(target.read_text(encoding="utf-8-sig"), "html.parser")
                fragment = unquote(url.fragment)
                if not soups[target].find(id=fragment) and not soups[target].find(attrs={"name": fragment}):
                    errors.append({"guide": guide["key"], "page": relative, "error": "missing-anchor", "target": raw})

original = ROOT.parent / "turn-milling-en-recovered-2026-10-09"
revision_path = ADMIN / "content-changes.json"
revision = json.loads(revision_path.read_text(encoding="utf-8")) if revision_path.exists() else {"changes": []}
approved = {change["path"]: change for change in revision["changes"]}
for relative, change in approved.items():
    path = ROOT / relative
    if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != change["after_sha256"]:
        errors.append({"error": "approved-revision-hash-mismatch", "path": relative})
unchanged = []
conversion_path = ADMIN / "turnmill-en-docfx-conversion.json"
if conversion_path.exists():
    conversion = json.loads(conversion_path.read_text(encoding="utf-8"))
    for item in conversion["pages"]:
        after = SITE / "turnmill/en" / item["file"]
        source = ROOT / conversion["source"] / item["file"]
        soup = soups[after.resolve()]
        content = soup.select_one("#main-content")
        text = " ".join(content.get_text(" ", strip=True).split())
        valid = (hashlib.sha256(after.read_bytes()).hexdigest() == item["rendered_sha256"]
                 and hashlib.sha256(source.read_bytes()).hexdigest() == item["source_sha256"]
                 and hashlib.sha256(text.encode("utf-8")).hexdigest() == item["body_sha256"]
                 and set(item["ids"]).issubset({el["id"] for el in content.select("[id]")}))
        unchanged.append({"file": item["file"], "original_body_preserved": valid, "docfx_conversion": True})
        if not valid:
            errors.append({"guide": "turnmill-en", "page": item["file"], "error": "converted-content-changed"})
    for item in conversion["removed"]:
        if (SITE / "turnmill/en" / item["file"]).exists():
            errors.append({"guide": "turnmill-en", "page": item["file"], "error": "excluded-chapter-present"})
    for relative, item in conversion["resources"].items():
        if hashlib.sha256((SITE / "turnmill/en" / relative).read_bytes()).hexdigest() != item["sha256"]:
            errors.append({"guide": "turnmill-en", "path": relative, "error": "converted-resource-changed"})
for page in ([] if conversion_path.exists() else json.loads((original / "pages.json").read_text(encoding="utf-8"))):
    before = original / "site" / page["file"]
    after = SITE / "turnmill/en" / page["file"]
    identical = hashlib.sha256(before.read_bytes()).digest() == hashlib.sha256(after.read_bytes()).digest()
    change = approved.get("html/turnmill/en/" + page["file"])
    authorized = bool(change and hashlib.sha256(before.read_bytes()).hexdigest() == change["before_sha256"]
                      and hashlib.sha256(after.read_bytes()).hexdigest() == change["after_sha256"])
    unchanged.append({"file": page["file"], "unchanged": identical, "approved_revision": authorized})
    if not identical and not authorized:
        errors.append({"guide": "turnmill-en", "page": page["file"], "error": "original-article-changed"})

lfs_pointers = []
for path in SITE.rglob("*"):
    if path.is_file() and path.stat().st_size < 300:
        if path.read_bytes().startswith(b"version https://git-lfs.github.com/spec/v1"):
            lfs_pointers.append(path.relative_to(SITE).as_posix())
if lfs_pointers:
    errors.append({"error": "unresolved-lfs-pointers", "paths": lfs_pointers})
index = json.loads((SITE / "search-index.json").read_text(encoding="utf-8"))
expected_pages = sum(guide["pages"] for guide in guides)
if len(guides) != 6 or len(index) != expected_pages or len(pages) != expected_pages:
    errors.append({"error": "unexpected-guide-or-page-count", "guides": len(guides), "index": len(index), "pages": len(pages)})
(ADMIN / "internal-checks.json").write_text(json.dumps({"guides": len(guides), "pages": len(pages), "errors": errors, "original_english_turnmill_articles": unchanged}, ensure_ascii=False, indent=2), encoding="utf-8")
# Query strings are not copied into audit notes; the original links remain in the manuals.
safe_external = []
for address, references in externals.items():
    parts = urlsplit(address)
    public_video_id = parse_qs(parts.query).get("v", [None])[0] if parts.hostname and "youtube.com" in parts.hostname else None
    display = urlunsplit((parts.scheme, parts.netloc, parts.path, urlencode({"v": public_video_id}) if public_video_id else "", ""))
    safe_external.append({"url": display, "query_preserved_in_manual": bool(parts.query), "references": references})
(ROOT / "external-links-work.json").write_text(json.dumps(safe_external, ensure_ascii=False, indent=2), encoding="utf-8")
print("Internal check:", len(guides), "guides,", len(pages), "pages,", len(errors), "errors; external URLs", len(externals))
print(json.dumps(errors[:25], ensure_ascii=False, indent=2))
sys.exit(bool(errors))
