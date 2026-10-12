"""Capture the actual manual page and exact source excerpts for the audit."""
from pathlib import Path
import html
import re
import sys

HERE = Path(__file__).resolve().parent
WORKSPACE = HERE.parent.parent
sys.path.insert(0, str(WORKSPACE / 'publication-work/audit-2026-10-08/tools/python'))
from playwright.sync_api import sync_playwright

OUT = HERE / 'screenshots'
OUT.mkdir(exist_ok=True)
PAGE = 'http://127.0.0.1:8765/machinemaker-six/robots/en/src/content/131903495.html'
SNAPSHOT = WORKSPACE / 'publication-work/machinemaker-commit-2026-10-12/en/machinemaker-delivery/2026-10-12'
SOURCE = SNAPSHOT / 'source/milling/docs/machinemaker/machines/src/3-axes-milling-machine.md'
CSS = WORKSPACE / 'publication-work/machinemaker-six-2026-10-12/html/turnmill/en/styles/main.css'


def excerpt(path, start, end):
    lines = path.read_text(encoding='utf-8-sig').splitlines()
    output = []
    for number in range(start, end + 1):
        escaped = html.escape(lines[number - 1])
        escaped = re.sub(r'(download\.sprutcam\.com|SPRUTCAM LIGHT THEME|sprut\.ru)', r'<mark>\1</mark>', escaped, flags=re.I)
        output.append(f'<div class="line"><span class="number">{number}</span><code>{escaped}</code></div>')
    return ''.join(output)


evidence = '''<!doctype html><html lang="ru"><meta charset="utf-8"><title>Упоминания в файлах</title>
<style>body{margin:0;padding:30px 40px;font:18px/1.45 "Segoe UI",sans-serif;color:#202124;background:#f2f4f7}h1{font-size:27px;margin:0 0 8px}p{margin:0 0 22px;color:#4d5563}section{background:white;border:1px solid #d9dde5;border-radius:10px;padding:22px;margin:0 0 22px}h2{font-size:21px;margin:0 0 8px}.path{font:14px/1.45 Consolas,monospace;color:#586174;overflow-wrap:anywhere;margin-bottom:16px}.line{display:flex;gap:16px;font:16px/1.7 Consolas,monospace}.number{color:#7a8290;min-width:36px;text-align:right;user-select:none}code{white-space:pre-wrap;overflow-wrap:anywhere;min-width:0}mark{background:#ffe7a0;color:#9e1b11;outline:2px solid #df4338;border-radius:2px;padding:0 2px}.note{margin:14px 0 0;font-size:16px;color:#4d5563}</style>
<h1>Упоминания SprutCAM в файлах</h1><p>Точные фрагменты текущих файлов; найденные слова выделены цветом.</p>
<section><h2>1. Milling EN → 3-Axes Milling Machine → исходник, строка 12</h2>
<div class="path">machinemaker-commit-2026-10-12/en/machinemaker-delivery/2026-10-12/source/milling/docs/machinemaker/machines/src/3-axes-milling-machine.md</div>'''
evidence += excerpt(SOURCE, 12, 12)
evidence += '<p class="note">Оба адреса находятся в href. В готовом HTML эти ссылки уже локальные.</p></section>'
evidence += '<section><h2>2. TurnMilling EN → styles/main.css → строка 667</h2><div class="path">machinemaker-six-2026-10-12/html/turnmill/en/styles/main.css</div>'
evidence += excerpt(CSS, 665, 669)
evidence += '<p class="note">Это комментарий CSS: на страницах учебника он не отображается.</p></section></html>'
(OUT / 'source-excerpts.html').write_text(evidence, encoding='utf-8')

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(channel='chrome', headless=True, args=['--no-proxy-server'])
    context = browser.new_context(viewport={'width': 1280, 'height': 900}, device_scale_factor=1)
    context.route('**/*', lambda route: route.continue_() if route.request.url.startswith(('http://127.0.0.1:8765/', 'data:', 'blob:', 'file:')) else route.abort())
    page = context.new_page()
    response = page.goto(PAGE, wait_until='domcontentloaded', timeout=20000)
    assert response.status == 200
    page.wait_for_function("[...document.querySelectorAll('article img')].every(i=>i.complete && i.naturalWidth)", timeout=15000)
    for name, filename, area in [
        ('robots-limits.png', '3575d6a240d0d00e23009b9abb76f3f16071aebbeeeea8d8bd895f743dad82a5.png', [82, 347, 254, 29]),
        ('robots-model-position.png', '3416680d67cea5b40aefd0fea069ff2eeafcecc7fa47ed5c8231fde19da3ff51.png', [363, 346, 277, 29]),
    ]:
        image = page.locator(f'article img[src$="{filename}"]')
        image.evaluate('(img)=>window.scrollTo(0,img.getBoundingClientRect().top+window.scrollY-190)')
        page.evaluate('''({filename, area}) => {
            document.querySelector('#audit-highlight')?.remove();
            const img = document.querySelector(`article img[src$="${filename}"]`);
            const rect = img.getBoundingClientRect(), scale = rect.width / img.naturalWidth;
            const mark = document.createElement('div'); mark.id = 'audit-highlight';
            Object.assign(mark.style, {position:'absolute',left:(rect.left+scrollX+area[0]*scale)+'px',top:(rect.top+scrollY+area[1]*scale)+'px',width:(area[2]*scale)+'px',height:(area[3]*scale)+'px',border:'3px solid #e12727',borderRadius:'4px',boxSizing:'border-box',pointerEvents:'none',zIndex:9999});
            document.body.appendChild(mark);
        }''', {'filename': filename, 'area': area})
        page.screenshot(path=str(OUT / name))
        print(name, flush=True)
    page.set_content(evidence, wait_until='load')
    page.screenshot(path=str(OUT / 'source-links-and-css.png'), full_page=True)
    print('source-links-and-css.png', flush=True)
    browser.close()
