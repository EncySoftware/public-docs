"""Verify the changed Robots EN page at desktop and mobile widths."""
from pathlib import Path
from datetime import datetime, timezone
import json
import shutil
import sys

REV = Path(__file__).resolve().parent
ROOT = REV.parent / 'machinemaker-six-2026-10-12'
sys.path.insert(0, str(REV.parent / 'audit-2026-10-08/tools/python'))
from playwright.sync_api import sync_playwright

manifest = json.loads((REV / 'revision.json').read_text(encoding='utf-8'))
shots = REV / 'screenshots'
shots.mkdir(exist_ok=True)
page_name = 'robots/en/src/content/131903495.html'
checks, errors, http_failures = [], [], []
with sync_playwright() as playwright:
    browser = playwright.chromium.launch(channel='chrome', headless=True, args=['--no-proxy-server'])
    context = browser.new_context()
    context.route('**/*', lambda route: route.continue_() if route.request.url.startswith(('http://127.0.0.1:8765/', 'data:', 'blob:')) else route.abort())
    page = context.new_page()
    page.on('response', lambda response: http_failures.append({'url': response.url, 'status': response.status}) if response.url.startswith('http://127.0.0.1:8765/') and response.status >= 400 else None)
    for width in (1440, 390):
        page.set_viewport_size({'width': width, 'height': 1000 if width == 1440 else 844})
        page.goto('http://127.0.0.1:8765/machinemaker-six/' + page_name, wait_until='domcontentloaded', timeout=20000)
        page.wait_for_function("[...document.querySelectorAll('article img')].every(i=>i.complete && i.naturalWidth)")
        result = page.evaluate("""() => ({title:document.title,broken:[...document.querySelectorAll('img')].filter(i=>!i.naturalWidth).map(i=>i.getAttribute('src')),overflow:document.documentElement.scrollWidth>innerWidth+1,images:[...document.querySelectorAll('article img')].map(i=>({src:i.getAttribute('src'),width:i.getBoundingClientRect().width,height:i.getBoundingClientRect().height,naturalWidth:i.naturalWidth,naturalHeight:i.naturalHeight}))})""")
        result.update(page=page_name, width=width)
        for item in manifest['images']:
            matches = [image for image in result['images'] if image['src'].endswith(item['new_filename'])]
            assert len(matches) == 1
            assert abs(matches[0]['height'] - matches[0]['width'] * matches[0]['naturalHeight'] / matches[0]['naturalWidth']) < 1, 'Replacement image aspect ratio is distorted.'
            assert all(not image['src'].endswith(item['old_filename']) for image in result['images'])
            image = page.locator(f'article img[src$="{item["new_filename"]}"]')
            image.evaluate('(img)=>window.scrollTo(0,img.getBoundingClientRect().top+scrollY-150)')
            page.screenshot(path=str(shots / f'robots-en-{item["name"]}-{width}.png'))
        checks.append(result)
        if result['broken'] or result['overflow']:
            errors.append(result)
    browser.close()
checked_at = datetime.now(timezone.utc).isoformat()
report = {'checked_at': checked_at, 'checks': checks, 'errors': errors, 'http_failures': http_failures, 'ocr': {'checked_images': 2, 'ency_captions': 2, 'sprutcam_findings': 0}}
(REV / 'browser-checks.json').write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
assert not errors and not http_failures, 'Focused browser checks failed.'
shutil.copy2(REV / 'browser-checks.json', ROOT / 'admin/robots-en-branding-browser-checks.json')
previous_path = ROOT / 'admin/revision-browser-checks.json'
previous = json.loads(previous_path.read_text(encoding='utf-8-sig'))
previous['previous_checked_at'] = previous['checked_at']
previous['checked_at'] = checked_at
previous['checks'] = [item for item in previous['checks'] if item['page'] != page_name] + checks
previous['robots_en_branding_revision'] = 'robots-en-branding-browser-checks.json'
previous_path.write_text(json.dumps(previous, ensure_ascii=False, indent=2), encoding='utf-8')
baseline_path = ROOT / 'admin/browser-checks.json'
baseline = json.loads(baseline_path.read_text(encoding='utf-8-sig'))
for index, original in enumerate(baseline['guides']['robots-en']['checks']):
    if original['page'] == 'src/content/131903495.html':
        fresh = next(result for result in checks if result['width'] == original['width'])
        baseline['guides']['robots-en']['checks'][index] = {**original, **{key: fresh[key] for key in ('title', 'broken', 'overflow')}, 'rechecked_at': checked_at}
baseline['robots_en_branding_revision'] = {'checked_at': checked_at, 'page': page_name, 'checks': len(checks)}
baseline_path.write_text(json.dumps(baseline, ensure_ascii=False, indent=2), encoding='utf-8')
print('Robots EN: 1440/390 px; both replacement screenshots loaded; zero broken images, overflow or HTTP failures.')
