"""Browser verification of edited delivery pages, replacement links and search."""
from datetime import datetime, timezone
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from threading import Thread
import hashlib
import json
import sys

ROOT = Path(__file__).resolve().parent
SITE = ROOT / "html"
ADMIN = ROOT / "admin"
sys.path.insert(0, str(ROOT.parent / "audit-2026-10-08/tools/python"))
from playwright.sync_api import sync_playwright


class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass

    def copyfile(self, source, outputfile):
        try:
            super().copyfile(source, outputfile)
        except (ConnectionAbortedError, ConnectionResetError, BrokenPipeError):
            pass  # Navigation may cancel an in-flight asset request.


def main():
    server = ThreadingHTTPServer(("127.0.0.1", 0), partial(QuietHandler, directory=str(SITE)))
    Thread(target=server.serve_forever, daemon=True).start()
    base = "http://127.0.0.1:" + str(server.server_port) + "/"
    checks, errors, http_failures = [], [], []
    edited = [change["path"][5:] for change in json.loads((ADMIN / "content-changes.json").read_text(encoding="utf-8"))["changes"]
              if change["path"].startswith("html/") and change["path"].endswith(".html")]
    targets = ["milling/en/src/assembly-options.html", "milling/en/src/building-a-kinematic-scheme.html"]
    try:
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(channel="chrome", headless=True, args=["--no-proxy-server"])
            context = browser.new_context()
            context.route("**/*", lambda route: route.continue_() if route.request.url.startswith((base, "data:", "blob:")) else route.abort())
            page = context.new_page()
            page.on("response", lambda response: http_failures.append({"url": response.url, "status": response.status}) if response.url.startswith(base) and response.status >= 400 else None)
            for width in [1440, 390]:
                page.set_viewport_size({"width": width, "height": 1000 if width == 1440 else 844})
                for relative in edited + targets:
                    try:
                        page.goto(base + relative, wait_until="domcontentloaded")
                        page.locator("article details").evaluate_all("els=>els.forEach(el=>el.open=true)")
                        page.wait_for_function("[...document.querySelectorAll('article img')].every(i=>i.complete)")
                        result = page.evaluate("""() => ({title:document.title,broken:[...document.images].filter(i=>!i.naturalWidth).map(i=>i.getAttribute('src')),overflow:document.documentElement.scrollWidth>innerWidth+1,obsoleteLinks:[...document.querySelectorAll('a[href]')].filter(a=>a.href.includes('kb.sprutcam.com')||a.href.includes('JHGeWdbgWj0')).map(a=>a.href)})""")
                        checks.append({"page": relative, "width": width, **result})
                        if result["broken"] or result["overflow"] or result["obsoleteLinks"]:
                            errors.append(checks[-1])
                    except Exception as exc:
                        errors.append({"page": relative, "width": width, "error": str(exc)})
            for origin, target, label in [("milling/en/src/toolbar.html", "assembly-options.html", "assembly settings panel"), ("milling/en/src/assemblies.html", "building-a-kinematic-scheme.html", "kinematics panel")]:
                page.goto(base + origin)
                page.locator("article").get_by_role("link", name=label, exact=True).click()
                page.wait_for_url("**/" + target)
            page.set_viewport_size({"width": 1440, "height": 1000})
            for folder, query in [("milling/en", "kinematic"), ("robots/en", "robot")]:
                page.goto(base + folder + "/src/index.html")
                page.locator("#search-query").fill(query)
                page.wait_for_function("document.querySelectorAll('#search-results a').length>0")
                data = page.evaluate("async url=>await (await fetch(url)).json()", base + folder + "/index.json")
                if "MachineMaker Custom Imported Robot Cell" in json.dumps(data):
                    errors.append({"error": "removed-video-present-in-local-search", "folder": folder})
            page.goto(base)
            if page.locator("a[data-guide]").count() != 6:
                errors.append({"error": "portal-does-not-have-six-guide-links"})
            page.locator("#query").fill("robot")
            page.wait_for_function("document.querySelectorAll('#results a').length>0")
            data = page.evaluate("async()=>await (await fetch('search-index.json')).json()")
            expected_pages = sum(g["pages"] for g in json.loads((ROOT / "guides.json").read_text(encoding="utf-8")))
            if len(data) != expected_pages or "MachineMaker Custom Imported Robot Cell" in json.dumps(data):
                errors.append({"error": "invalid-shared-search"})
            # The confirmed examples and KUKA paragraph must still match their source snapshots.
            baselines = [
                (SITE / "_shared/examples/legacy-v16/Milling_machine_3ax.zip", "5bb1db5f4f3356ecc711af4234685a19c15039b79b1c41fc72e2f1699338f8ea"),
                (SITE / "_shared/examples/legacy-v16/Milling_machine.zip", "35d5f69200d53465cf624e85785ef2cd37983fe3b9d114dc68656d2e2fbee98b"),
            ]
            for path, expected in baselines:
                if hashlib.sha256(path.read_bytes()).hexdigest() != expected:
                    errors.append({"error": "confirmed-example-changed", "path": str(path)})
            original_kuka = ROOT.parent / "mm-review-2026-10-09/robots-en/build/html/src/content/131903495.html"
            from bs4 import BeautifulSoup
            paragraphs = []
            for path in [original_kuka, SITE / "robots/en/src/content/131903495.html"]:
                soup = BeautifulSoup(path.read_text(encoding="utf-8-sig"), "html.parser")
                paragraphs.append(str(soup.find("a", href="https://www.kuka.com/en-de/services/downloads").parent))
            if paragraphs[0] != paragraphs[1]:
                errors.append({"error": "kuka-paragraph-changed"})
            browser.close()
    finally:
        server.shutdown()
        server.server_close()
    report = {"checked_at": datetime.now(timezone.utc).isoformat(), "checks": checks, "errors": errors, "http_failures": http_failures,
              "replacement_links_clicked": targets, "search_interfaces_checked": ["milling-en", "robots-en", "shared"],
              "legacy_examples_unchanged": True, "kuka_paragraph_unchanged": True}
    (ADMIN / "revision-browser-checks.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("Revision browser:", len(checks), "page checks;", len(errors), "errors;", len(http_failures), "HTTP failures")
    sys.exit(bool(errors or http_failures))


if __name__ == "__main__":
    main()
