"""Serve selected MachineMaker snapshots on this computer without changing them."""
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from io import BytesIO
from pathlib import Path
from urllib.parse import unquote, urlsplit
import argparse
import json

HERE = Path(__file__).resolve().parent
WORKSPACE = HERE.parent.parent
PUBLICATION = HERE.parent
AUDIT = PUBLICATION / "audit-2026-10-08"
FRESH = PUBLICATION / "mm-review-2026-10-09"
DRAFT = PUBLICATION / "turn-milling-en-draft-2026-10-09"
ORIGINAL = PUBLICATION / "turn-milling-en-recovered-2026-10-09"
COLLECTION = PUBLICATION / "machinemaker-six-2026-10-12"
INPUTS = json.loads((WORKSPACE / "artifacts/publication-inputs.json").read_text(encoding="utf-8-sig"))
DIRECTORIES = {
    "machinemaker-six": COLLECTION / "html",
    "machinemaker-six-admin": COLLECTION / "admin",
    "turn-milling-en-original": ORIGINAL / "site",
    "turn-milling-en-original-review": ORIGINAL / "review",
    "turn-milling-en-draft": DRAFT / "source/build/html",
    "turn-milling-en-draft-review": DRAFT / "review",
    "turn-milling-en-draft-sources": DRAFT / "source/main",
    "machines-en": FRESH / "machines-en/build/html",
    "machines-ru": FRESH / "machines-ru/build/html",
    "robots-en": FRESH / "robots-en/build/html",
    "robots-ru": FRESH / "robots-ru/build/html",
    "current-sources-machines-en": FRESH / "machines-en/main",
    "current-sources-machines-ru": FRESH / "machines-ru/main",
    "current-sources-robots-en": FRESH / "robots-en/main",
    "current-sources-robots-ru": FRESH / "robots-ru/main",
    "checked-en": AUDIT / "site-en",
    "checked-ru": AUDIT / "site-ru",
    "saved-en": PUBLICATION / "preview-ency-docs",
    "saved-ru": PUBLICATION / "preview-sprutcam-docs",
    "html-machines-en": WORKSPACE / "MachineMaker User Manual-v5-English",
    "html-machines-ru": WORKSPACE / "MachineMaker-RU",
    "html-robots-en": Path(INPUTS["robots_en"]).parent / "Robots-EN",
    "html-robots-ru": Path(INPUTS["robots_ru"]).parent / "Robots-RU",
    "html-turn-milling-ru": WORKSPACE / "токарно фрезер/MachineMaker руководство пользователя-v1-20261006_1114",
    "sources-en": PUBLICATION / "ency-docs/docs/machinemaker",
    "sources-ru": PUBLICATION / "sprutcam-docs/docs/machinemaker",
    "sources-en-develop": PUBLICATION / "ency-docs-develop/docs/machinemaker",
    "sources-ru-develop": PUBLICATION / "sprutcam-docs-develop/docs/machinemaker",
    "shared-media": AUDIT / "site-en/v3/machinemaker/media",
    "examples": PUBLICATION / "release-assets",
}
FILES = {"": HERE / "index.html", "report.html": HERE / "report.html",
         "current-report.html": FRESH / "REVIEW.html"}
FILES["machinemaker-six-package.zip"] = COLLECTION / "MachineMaker-six-manuals-2026-10-12.zip"
FILES["machinemaker-six-package.zip.sha256"] = COLLECTION / "MachineMaker-six-manuals-2026-10-12.zip.sha256"
for name in ["summary.json", "built-checks.json", "browser-checks.json", "external-checks.json",
             "video-checks.json", "content-comparison.json", "source-links.json", "gerrit-branches.json",
             "gerrit-branches-final.json", "lfs-local-restoration.json", "REVIEW-RU.md"]:
    FILES["current-reports/" + name] = FRESH / name
for name in ["inventory-six.json", "all-gerrit-branches.json", "turn-milling-ru-export.json"]:
    FILES["current-reports/" + name] = FRESH / name
for guide in ["machines-en", "machines-ru", "robots-en", "robots-ru"]:
    for width in [1440, 390]:
        name = guide + "-" + str(width) + ".png"
        FILES["current-reports/" + name] = FRESH / name
    for check in ["validate", "brand", "build"]:
        name = guide + "-" + check + ".log"
        FILES["current-reports/" + name] = FRESH / name
for key, filename in INPUTS.items():
    FILES["archives/" + key + ".zip"] = Path(filename)
FILES.update({
    "archives/preview-en.zip": PUBLICATION / "github-preview-machinemaker.zip",
    "archives/preview-ru.zip": PUBLICATION / "gitverse-preview-machinemaker.zip",
    "archives/Hanwha-XD10.zip": WORKSPACE / "3D_models_Hanwha_XD10.zip",
    "archives/MachineSchema.zip": WORKSPACE / "MachineSchema.zip",
    "archives/turn-milling-ru-20261006.zip": WORKSPACE / "токарно фрезер/MachineMaker руководство пользователя-v1-20261006_1114.zip",
})
for name in ["REVIEW-RU.md", "summary.json", "legacy-links.json", "proposed-legacy-fixes-en.patch",
             "build-en.log", "build-ru.log", "built-checks.json", "browser-checks.json",
             "external-checks-verified.json", "workspace-audit.json"]:
    FILES["reports/" + name] = AUDIT / name


class ReviewHandler(SimpleHTTPRequestHandler):
    def translate_path(self, path):
        relative = unquote(urlsplit(path).path).lstrip("/")
        if relative in FILES:
            return str(FILES[relative])
        alias, _, suffix = relative.partition("/")
        if alias in DIRECTORIES:
            root = DIRECTORIES[alias].resolve()
            candidate = (root / suffix).resolve()
            if candidate.is_relative_to(root):
                return str(candidate)
        return str(HERE / "__not_found__")

    def send_head(self):
        path = Path(self.translate_path(self.path))
        if path.is_file() and path.suffix.lower() == ".html":
            content = path.read_bytes().replace(
                b"https://encysoftware.github.io/public-docs/v3/machinemaker/media/",
                b"/shared-media/",
            )
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(content)))
            self.send_header("Cache-Control", "no-cache")
            self.end_headers()
            return BytesIO(content)
        return super().send_head()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--port", type=int, default=8765)
    args = parser.parse_args()
    server = ThreadingHTTPServer(("127.0.0.1", args.port), partial(ReviewHandler, directory=str(HERE)))
    print(f"MachineMaker local review: http://127.0.0.1:{args.port}/", flush=True)
    server.serve_forever()
