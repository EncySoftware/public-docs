"""Open every page of the final six-manual package and check all search interfaces."""
from pathlib import Path
from datetime import datetime, timezone
import argparse
import json
import sys

ROOT = Path(__file__).resolve().parent
ADMIN = ROOT / "admin"
SHOTS = ADMIN / "screenshots"
SHOTS.mkdir(exist_ok=True)
sys.path.insert(0, str(ROOT.parent / "audit-2026-10-08/tools/python"))
from playwright.sync_api import sync_playwright

base = "http://127.0.0.1:8765/machinemaker-six/"
guides = json.loads((ROOT / "guides.json").read_text(encoding="utf-8"))
parser = argparse.ArgumentParser()
parser.add_argument("--guide", choices=[g["key"] for g in guides])
args = parser.parse_args()
previous = json.loads((ADMIN / "browser-checks.json").read_text(encoding="utf-8")) if args.guide else {}
results = {key: value for key, value in previous.get("guides", {}).items() if key != args.guide}
errors = [e for e in previous.get("errors", []) if e.get("guide") != args.guide]
http_failures = []
search_terms = {"milling-en": "Swiss", "milling-ru": "станок", "robots-en": "robot", "robots-ru": "робот", "turnmill-en": "turret", "turnmill-ru": "шпиндель"}
with sync_playwright() as p:
    browser = p.chromium.launch(channel="chrome", headless=True, args=["--no-proxy-server"])
    context = browser.new_context()
    context.route("**/*", lambda route: route.continue_() if route.request.url.startswith("http://127.0.0.1:8765/") or route.request.url.startswith(("data:", "blob:")) else route.abort())
    page = context.new_page()
    page.on("response", lambda response: http_failures.append({"url": response.url, "status": response.status}) if response.url.startswith(base) and response.status >= 400 else None)
    for guide in guides:
        if args.guide and guide["key"] != args.guide:
            continue
        checks = []
        prefix = base + guide["kind"] + "/" + guide["language"] + "/"
        for width in [1440, 390]:
            page.set_viewport_size({"width": width, "height": 1000 if width == 1440 else 844})
            for relative in guide["articles"]:
                try:
                    page.goto(prefix + relative, wait_until="domcontentloaded", timeout=20000)
                    page.locator("article details").evaluate_all("els=>els.forEach(el=>el.open=true)")
                    page.wait_for_function("[...document.querySelectorAll('article img')].every(i=>i.complete)", timeout=15000)
                    result = page.evaluate("""() => ({title:document.title,broken:[...document.querySelectorAll('img')].filter(i=>!i.naturalWidth).map(i=>i.getAttribute('src')),overflow:document.documentElement.scrollWidth>innerWidth+1})""")
                    result.update({"page": relative, "width": width})
                    checks.append(result)
                    if result["broken"] or result["overflow"]:
                        errors.append({"guide": guide["key"], **result})
                    if guide["entry"].endswith(relative):
                        page.screenshot(path=str(SHOTS / (guide["key"] + "-" + str(width) + ".png")))
                except Exception as exc:
                    errors.append({"guide": guide["key"], "page": relative, "width": width, "error": str(exc)[:500]})
            print("BROWSER", guide["key"], width, len(guide["articles"]), flush=True)
        page.set_viewport_size({"width": 1440, "height": 1000})
        term = search_terms[guide["key"]]
        try:
            if guide["format"] == "original-html":
                page.goto(prefix + "search.html?query=" + term, wait_until="domcontentloaded")
                selector = "#search-results a"
            else:
                page.goto(base + guide["entry"], wait_until="domcontentloaded")
                page.locator("#search-query").fill(term)
                selector = "#search-results a"
            page.wait_for_function("document.querySelectorAll('#search-results a').length>0", timeout=12000)
            local_search = page.locator(selector).count()
        except Exception as exc:
            local_search = 0
            errors.append({"guide": guide["key"], "type": "local-search", "error": str(exc)[:500]})
        results[guide["key"]] = {"checks": checks, "search_term": term, "search_results": local_search, "checked_at": datetime.now(timezone.utc).isoformat()}
        (ADMIN / "browser-checks.json").write_text(json.dumps({"guides": results, "errors": errors, "http_failures": http_failures}, ensure_ascii=False, indent=2), encoding="utf-8")
    portal = {}
    page.goto(base, wait_until="domcontentloaded")
    if page.locator("a[data-guide]").count() != 6:
        errors.append({"type": "portal", "error": "expected-six-guide-links"})
    page.locator("#query").fill("turret")
    page.locator("#kind").select_option("turnmill")
    page.locator("#language").select_option("en")
    page.wait_for_function("document.querySelectorAll('#results a').length>0")
    portal["english_turnmill_results"] = page.locator("#results a").count()
    if not any("30_1.html" in href for href in page.locator("#results a").evaluate_all("els=>els.map(a=>a.href)")):
        errors.append({"type": "portal-search", "error": "dual-row-original-page-not-found"})
    page.locator("#query").fill("револьвер")
    page.locator("#language").select_option("ru")
    page.wait_for_function("[...document.querySelectorAll('#results a')].some(a=>a.href.includes('turnmill/ru/'))")
    portal["russian_turnmill_results"] = page.locator("#results a").count()
    for width in [1440, 390]:
        page.set_viewport_size({"width": width, "height": 1000 if width == 1440 else 844})
        if page.evaluate("document.documentElement.scrollWidth>innerWidth+1"):
            errors.append({"type": "portal-overflow", "width": width})
        page.screenshot(path=str(SHOTS / ("portal-" + str(width) + ".png")))
    browser.close()
(ADMIN / "browser-checks.json").write_text(json.dumps({"guides": results, "portal": portal, "errors": errors, "http_failures": http_failures,
    "updated_guide": args.guide, "unchanged_guides_prior_checks_retained": [g["key"] for g in guides if args.guide and g["key"] != args.guide]}, ensure_ascii=False, indent=2), encoding="utf-8")
print("Browser page checks", sum(len(g["checks"]) for g in results.values()), "errors", len(errors), "HTTP failures", len(http_failures), flush=True)
sys.exit(bool(errors or http_failures))
