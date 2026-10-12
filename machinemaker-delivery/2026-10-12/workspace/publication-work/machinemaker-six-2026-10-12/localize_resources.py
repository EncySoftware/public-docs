"""Make selected shared images and example downloads local in the six-manual site."""
from pathlib import Path
from urllib.parse import quote
from urllib.request import Request, urlopen
from zipfile import ZipFile
import hashlib
import json
import posixpath
import re
import shutil

ROOT = Path(__file__).resolve().parent
PUBLICATION = ROOT.parent
SITE = ROOT / "html"
ADMIN = ROOT / "admin"
MEDIA = "https://encysoftware.github.io/public-docs/v3/machinemaker/media/"
RELEASE = "https://github.com/EncySoftware/public-docs/releases/download/machinemaker-examples-2026-09-22/"
release_assets = {item["name"]: item for item in json.loads((PUBLICATION / "release-assets.json").read_text(encoding="utf-8-sig"))["assets"]}
resources = {}
changes = []


def digest(path):
    value = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            value.update(block)
    return value.hexdigest()


def ensure(url, category, name):
    if url in resources:
        return SITE / resources[url]["path"]
    if category == "media":
        source = PUBLICATION / "ency-docs/docs/machinemaker/_media" / name
        destination = SITE / "_shared/media" / name
        expected = Path(name).stem
    elif category == "release":
        source = PUBLICATION / "release-assets" / name
        destination = SITE / "_shared/examples" / name
        expected = release_assets[name]["sha256"]
    else:
        source = None
        destination = SITE / "_shared/examples/legacy-v16" / name
        expected = None
    destination.parent.mkdir(parents=True, exist_ok=True)
    if source is not None:
        if not source.is_file():
            raise FileNotFoundError("Required local resource is missing: " + str(source))
        if not destination.exists():
            shutil.copy2(source, destination)
    elif not destination.exists():
        with urlopen(Request(url, headers={"User-Agent": "MachineMaker-six-manuals-build"}), timeout=25) as response:
            destination.write_bytes(response.read())
        with ZipFile(destination) as archive:
            if archive.testzip() is not None:
                raise RuntimeError("Downloaded legacy example has a CRC error")
    checksum = digest(destination)
    if expected is not None and checksum != expected:
        raise RuntimeError("Resource checksum differs from its canonical value: " + name)
    resources[url] = {"path": destination.relative_to(SITE).as_posix(), "sha256": checksum,
                      "bytes": destination.stat().st_size, "kind": category,
                      "legacy_version_compatibility_confirmed": False if category == "legacy" else None}
    return destination


patterns = [
    ("media", re.compile(re.escape(MEDIA) + r"([0-9a-f]{64}\.[A-Za-z0-9]+)")),
    ("release", re.compile(re.escape(RELEASE) + r"([A-Za-z0-9_.%-]+\.(?:zip|rar))", re.I)),
    ("legacy", re.compile(r"https?://download\.sprutcam\.com/download/sprutcam/MachineMaker/version_16/examples/3AxesMillingMachine/((?:Milling_machine_3ax|Milling_machine)\.zip)", re.I)),
]
for path in SITE.rglob("*"):
    if not path.is_file() or path.suffix.lower() not in {".html", ".htm", ".json", ".js", ".css"}:
        continue
    original = path.read_text(encoding="utf-8-sig")
    text = original
    for category, expression in patterns:
        def replace(match):
            url = match.group(0)
            name = match.group(1)
            destination = ensure(url, category, name)
            relative = posixpath.relpath(destination.relative_to(SITE).as_posix(), path.parent.relative_to(SITE).as_posix())
            local_url = quote(relative, safe="/-_.~()")
            changes.append({"file": path.relative_to(SITE).as_posix(), "source_url": url, "local_url": local_url})
            return local_url
        text = expression.sub(replace, text)
    if text != original:
        path.write_text(text, encoding="utf-8", newline="")
(ADMIN / "localized-resources.json").write_text(json.dumps({"resources": resources, "changes": changes}, ensure_ascii=False, indent=2), encoding="utf-8")
print("Localized", len(resources), "unique resources in", len({c['file'] for c in changes}), "files; bytes", sum(r["bytes"] for r in resources.values()), flush=True)
