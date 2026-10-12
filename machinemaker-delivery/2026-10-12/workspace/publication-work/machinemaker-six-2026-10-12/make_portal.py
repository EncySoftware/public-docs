"""Create a clean six-manual portal and a shared full-text search index."""
from pathlib import Path
from html import escape
import json
import shutil
import sys

ROOT = Path(__file__).resolve().parent
SITE = ROOT / "html"
guides = json.loads((ROOT / "guides.json").read_text(encoding="utf-8"))
page_count = sum(guide["pages"] for guide in guides)
sys.path.insert(0, str(ROOT.parent / "audit-2026-10-08/tools/python"))
from bs4 import BeautifulSoup

entries = []
for guide in guides:
    folder = SITE / guide["kind"] / guide["language"]
    for relative in guide["articles"]:
        path = folder / relative
        soup = BeautifulSoup(path.read_text(encoding="utf-8-sig"), "html.parser")
        article = soup.select_one("article.content") or soup.select_one("#main-content")
        heading = soup.select_one("article.content h1") or soup.select_one("article#ht-content .ht-content-header h1")
        title = heading.get_text(" ", strip=True) if heading else soup.title.get_text(" ", strip=True)
        text = " ".join(article.get_text(" ", strip=True).split())
        entries.append({"guide": guide["key"], "kind": guide["kind"], "language": guide["language"], "book": guide["label"],
                        "title": title, "href": guide["kind"] + "/" + guide["language"] + "/" + relative, "text": text})
(SITE / "search-index.json").write_text(json.dumps(entries, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
(SITE / "assets").mkdir(exist_ok=True)
shutil.copy2(ROOT.parent / "turn-milling-en-recovered-2026-10-09/site/MMUM18TurnMill.png", SITE / "assets/machinemaker.png")
cards = []
for kind, name, en_name, description in [
    ("robots", "Роботы", "Robots", "Модели роботов, ячейки, инструменты и калибровка."),
    ("milling", "Фрезерные станки", "Milling machines", "Модели станков, кинематика, оборудование и примеры настройки."),
    ("turnmill", "Токарно-фрезерные станки", "Turn-milling machines", "Шпиндели, револьверы, инструментальные блоки и сборка станка."),
]:
    links = []
    for lang, label in [("en", "English"), ("ru", "Русский")]:
        guide = next(g for g in guides if g["kind"] == kind and g["language"] == lang)
        links.append('<a class="language" href="' + guide["entry"] + '" data-guide="' + guide["key"] + '"><strong>' + label + '</strong><span>' + str(guide["pages"]) + ' стр.</span></a>')
    cards.append('<article class="card"><div class="eyebrow">' + en_name + '</div><h2>' + name + '</h2><p>' + description + '</p><div class="languages">' + ''.join(links) + '</div></article>')
html = """<!doctype html><html lang="ru"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>MachineMaker — шесть руководств</title>
<style>*{box-sizing:border-box}body{font:16px/1.65 system-ui,sans-serif;margin:0;background:#f4f5f7;color:#242a33}main{max-width:1240px;margin:auto;padding:42px 24px}.brand{display:flex;align-items:center;gap:18px}.brand img{width:65px;height:65px;object-fit:contain}h1{font-size:36px;line-height:1.2;margin:0}h2{font-size:23px;line-height:1.3;margin:8px 0 12px}.intro{color:#596273;margin:18px 0 28px}.cards{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:20px}.card{background:white;border:1px solid #e1e4e9;border-radius:14px;padding:26px;display:flex;flex-direction:column}.eyebrow{color:#80641c;font-size:13px;font-weight:650;letter-spacing:.04em}.card p{color:#596273;margin:0 0 24px;flex:1}.languages{display:flex;gap:12px;flex-wrap:wrap}.language{display:flex;flex-direction:column;background:#faf7ec;border:1px solid #e9dcae;border-radius:8px;padding:10px 15px;color:#242a33;text-decoration:none;min-width:112px}.language:hover{background:#f4e9be}.language span{font-size:13px;color:#656c76}.search{margin-top:32px;background:white;padding:25px;border:1px solid #e1e4e9;border-radius:14px}.filters{display:grid;grid-template-columns:minmax(0,1fr) 220px 160px;gap:12px}input,select{width:100%;font:inherit;padding:12px;border:1px solid #cdd3dc;border-radius:7px;background:white;color:inherit}.results{margin:20px 0 0;padding:0;list-style:none}.results li{padding:15px 0;border-top:1px solid #e9ecf0}.results a{color:#075db5;font-weight:650;text-decoration:none}.results p{margin:5px 0;color:#596273;font-size:14px}.tag{font-size:12px;color:#776735}#search-status{font-size:14px;color:#68717e;margin:14px 0 0}.footer{margin-top:28px;color:#7b8490;font-size:13px}@media(max-width:1000px){.cards{grid-template-columns:1fr}.card{padding:22px}.filters{grid-template-columns:1fr 1fr}.filters input{grid-column:1/-1}h1{font-size:29px}}@media(max-width:500px){main{padding:24px 14px}.filters{grid-template-columns:1fr}.filters input{grid-column:auto}.search{padding:18px}.brand img{width:48px;height:48px}.brand{gap:12px}h1{font-size:26px}}</style>
<main><header class="brand"><img src="assets/machinemaker.png" alt="MachineMaker"><h1>MachineMaker</h1></header><p class="intro">Шесть руководств: три типа оборудования, каждый на английском и русском языке.</p><section class="cards">""" + ''.join(cards) + """</section>
<section class="search"><h2>Поиск по всем руководствам</h2><div class="filters"><input id="query" type="search" placeholder="Название функции или тема" aria-label="Поиск по тексту"><select id="kind" aria-label="Тип оборудования"><option value="">Все разделы</option><option value="robots">Роботы</option><option value="milling">Фрезерные станки</option><option value="turnmill">Токарно-фрезерные станки</option></select><select id="language" aria-label="Язык"><option value="">Все языки</option><option value="en">English</option><option value="ru">Русский</option></select></div><p id="search-status">Введите запрос для поиска по 209 страницам.</p><ul id="results" class="results"></ul></section><p class="footer">MachineMaker · Documentation</p></main>
<script>let index=[];const query=document.getElementById('query'),kind=document.getElementById('kind'),language=document.getElementById('language'),results=document.getElementById('results'),status=document.getElementById('search-status');const norm=s=>s.normalize('NFKC').toLocaleLowerCase();function search(){results.replaceChildren();const terms=norm(query.value.trim()).split(/\s+/).filter(Boolean);if(!terms.length){status.textContent='Введите запрос для поиска по 209 страницам.';return}const matches=index.filter(p=>(!kind.value||p.kind===kind.value)&&(!language.value||p.language===language.value)&&terms.every(t=>norm(p.title+' '+p.text).includes(t))).map(p=>({p,score:terms.reduce((s,t)=>s+(norm(p.title).includes(t)?10:0),0)})).sort((a,b)=>b.score-a.score);status.textContent=matches.length?'Найдено страниц: '+matches.length:'Совпадений не найдено';matches.slice(0,50).forEach(({p})=>{const li=document.createElement('li'),tag=document.createElement('div'),a=document.createElement('a'),snippet=document.createElement('p');tag.className='tag';tag.textContent=p.book;a.href=p.href;a.textContent=p.title;snippet.textContent=p.text.slice(0,240)+(p.text.length>240?'…':'');li.append(tag,a,snippet);results.append(li)})}let timer;query.addEventListener('input',()=>{clearTimeout(timer);timer=setTimeout(search,120)});kind.addEventListener('change',search);language.addEventListener('change',search);fetch('search-index.json').then(r=>r.json()).then(data=>{index=data;search()}).catch(()=>{status.textContent='Не удалось загрузить поиск. Обновите страницу.'});</script></html>"""
(SITE / "index.html").write_text(html.replace("209", str(page_count)), encoding="utf-8")
print("Portal has", len(guides), "guide links and", len(entries), "searchable pages.")
