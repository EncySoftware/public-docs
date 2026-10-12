"""Make an index of the saved local MachineMaker materials."""
from html import escape
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent
AUDIT = HERE.parent / "audit-2026-10-08"
FRESH = HERE.parent / "mm-review-2026-10-09"
STYLE = """
body{font:16px/1.65 system-ui,sans-serif;color:#202631;background:#f5f7fa;margin:0}
main{max-width:1160px;margin:36px auto;padding:28px;background:white;border-radius:12px}
h1{margin-top:0}h2{margin-top:32px}a{color:#075db5}table{border-collapse:collapse;width:100%}
td,th{padding:12px;text-align:left;border-bottom:1px solid #dfe4eb;vertical-align:top}
.notice{padding:16px 20px;background:#fff4d8;border-left:4px solid #d29c17}
.table{overflow-x:auto}small{color:#5d6675}code{overflow-wrap:anywhere}pre{white-space:pre-wrap}
@media(max-width:700px){main{margin:0;padding:18px;border-radius:0}td,th{padding:9px}}
"""


def link(url, title):
    return f'<a href="{escape(url, quote=True)}">{escape(title)}</a>'


def page(title, body):
    return f'<!doctype html><html lang="ru"><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>{escape(title)}</title><style>{STYLE}</style><main>{body}</main></html>'


guides = [
    ("machines_en", "Фрезерные станки — English", "en", "v3", "machines", 31),
    ("robots_en", "Роботы — English", "en", "v3", "robots", 47),
    ("machines_ru", "Фрезерные станки — Русский", "ru", "v20", "machines", 33),
    ("robots_ru", "Роботы — Русский", "ru", "v20", "robots", 47),
]
rows = []
for key, title, lang, version, kind, count in guides:
    suffix = f"{version}/machinemaker/{kind}/src/index.html"
    cells = [f"<strong>{escape(title)}</strong><br><small>{count} глав</small>",
             link(f"/checked-{lang}/{suffix}", "Открыть"),
             link(f"/saved-{lang}/{suffix}", "Открыть"),
             link(f"/html-{kind}-{lang}/index.html", "Открыть HTML"),
             link(f"/archives/{key}.zip", "Скачать ZIP")]
    rows.append("<tr>" + "".join(f"<td>{cell}</td>" for cell in cells) + "</tr>")

body = """
<h1>MachineMaker — локальные материалы</h1>
<p>Роботы, фрезерные и токарно-фрезерные станки — каждое руководство на английском и русском.</p>
"""
collection = HERE.parent / "machinemaker-six-2026-10-09"
collection_ready = (collection / "admin/summary.json").exists() and (collection / "MachineMaker-six-manuals-2026-10-09.zip.sha256").exists()
if collection_ready:
    body += '<div class="notice"><strong>Готовый локальный комплект: 6 руководств, 209 страниц.</strong><p>' + link('/machinemaker-six/', 'Открыть все шесть руководств') + ' · ' + link('/machinemaker-six-package.zip', 'Скачать комплект для администратора') + ' · ' + link('/machinemaker-six-admin/', 'Инструкция и результаты проверок') + '</p><p>Английский токарно-фрезерный учебник включён в оригинальной версии. Публичную выкладку выполнит администратор после проверки пользователем.</p></div>'
original = HERE.parent / "turn-milling-en-recovered-2026-10-09"
original_ready = (original / "review/summary.json").exists()
if original_ready:
    body += '<div class="notice"><strong>Найден и восстановлен оригинальный английский учебник ENCY TurnMilling CNC — 26 страниц.</strong><p>' + link('/turn-milling-en-original/1.html', 'Открыть оригинальный английский токарно-фрезерный учебник') + ' · ' + link('/turn-milling-en-original-review/', 'Главы, проверки и HTML ZIP') + '</p><p>Это источник, который пользователь выбрал для дальнейшей работы. Публичное размещение ожидает проверки содержания.</p></div>'
draft = HERE.parent / "turn-milling-en-draft-2026-10-09"
if (draft / "review/summary.json").exists():
    label = "Прежний черновик по русскому образцу — архив" if original_ready else "Английский черновик по русскому образцу — 25 страниц"
    body += '<details><summary>' + label + '</summary><p>' + link('/turn-milling-en-draft/src/index.html', 'Открыть прежний черновик') + ' · ' + link('/turn-milling-en-draft-review/', 'Сравнить его с русским образцом') + '</p><p>После обнаружения оригинального английского учебника этот черновик сохраняется как предыдущий этап.</p></details>'
if (FRESH / "inventory-six.json").exists():
    inventory = json.loads((FRESH / "inventory-six.json").read_text(encoding="utf-8"))
    inventory_rows = []
    manuals = inventory["manuals"]
    if collection_ready:
        assembled = json.loads((collection / "admin/summary.json").read_text(encoding="utf-8"))
        manuals = [{"title": g["label"], "pages": g["pages"], "status": "Собрано и проверено локально", "url": "/machinemaker-six/" + g["entry"]} for g in assembled["guides"]]
    for manual in manuals:
        cells = [escape(manual["title"]), str(manual["pages"]), escape(manual["status"]), link(manual["url"], "Открыть")]
        inventory_rows.append("<tr>" + "".join("<td>" + cell + "</td>" for cell in cells) + "</tr>")
    body += "<h2>Шесть руководств: что доступно локально</h2>"
    body += "<p>Комплект собран из сохранённых фрезерных руководств EN/RU, снимков веток роботов EN/RU и токарно-фрезерного RU, а также восстановленного оригинального токарно-фрезерного EN. Источники и версии указаны в инструкции для администратора.</p>" if collection_ready else "<p class=\"notice\">Это инвентаризация материалов до сборки общего комплекта. В Gerrit найдено четыре ветки MachineMaker; фрезерные руководства сохранены отдельно.</p>"
    body += '<div class="table"><table><tr><th>Руководство</th><th>Страниц</th><th>Состояние материалов</th><th>Просмотр</th></tr>' + "".join(inventory_rows) + "</table></div>"
    body += "<p>Отдельный русский экспорт токарно-фрезерного руководства от 6 октября: " + link("/html-turn-milling-ru/index.html", "открыть исходный HTML") + " · " + link("/archives/turn-milling-ru-20261006.zip", "скачать ZIP") + ".</p>"
if (FRESH / "gerrit-branches.json").exists():
    branches = json.loads((FRESH / "gerrit-branches.json").read_text(encoding="utf-8"))
    current_rows = []
    for key, branch in zip(["machines-en", "machines-ru", "robots-en", "robots-ru"], branches):
        repo = FRESH / key
        profile = json.loads((repo / "main/doc-profile.json").read_text(encoding="utf-8-sig"))
        title = json.loads((repo / "main/docfx.json").read_text(encoding="utf-8-sig"))["build"]["globalMetadata"]["_appTitle"]
        count = len(json.loads((repo / "main/manifest.json").read_text(encoding="utf-8-sig"))["pages"])
        cells = [escape(title), "<code>" + escape(branch["ref"].removeprefix("refs/heads/")) + "</code><br><small>" + branch["revision"][:12] + "</small>", str(count), link("/" + key + "/src/index.html", "Открыть руководство"), link("/current-sources-" + key + "/", "Исходники")]
        current_rows.append("<tr>" + "".join("<td>" + cell + "</td>" for cell in cells) + "</tr>")
    body += "<h2>Снимки четырёх найденных веток docs-work — 9 октября 2026</h2>"
    body += "<p>Исходники получены из Gerrit по зафиксированным коммитам. Все четыре HTML-сборки DocFX завершены без ошибок и предупреждений. Вложения Git LFS восстановлены с проверкой SHA256.</p>"
    body += '<div class="table"><table><tr><th>Руководство</th><th>Ветка и коммит</th><th>Страниц</th><th>Локальная сборка</th><th>Markdown и файлы</th></tr>' + "".join(current_rows) + "</table></div>"
    body += "<p class=\"notice\">" + link("/current-report.html", "Проверка текущих веток: ссылки, изображения и замечания") + ". Успешная HTML-сборка сама по себе не означает готовность к публикации.</p>"
body += """
<details><summary><strong>Сентябрьские версии, исходные HTML и архивы</strong></summary>
<p>Ниже находятся сохранённые материалы прежней публикации. Сборка от 8 октября проверяла сентябрьскую версию.</p>
<div class="table"><table><thead><tr><th>Руководство</th><th>Сборка 8 октября</th>
<th>Сохранённый портал 22 сентября</th><th>Исходный HTML-экспорт</th><th>Архив экспорта</th>
</tr></thead><tbody>
""" + "".join(rows) + "</tbody></table></div></details>"
body += """
<p>В колонке «Сборка 8 октября» доступны оглавление и поиск. Изображения общей медиатеки
показываются из локально сохранённых файлов; исходные HTML и DocFX-файлы не изменены.</p>
<h2>Проверка старых ссылок</h2>
<p>В проверке от 8 октября три старых адреса <code>kb.sprutcam.com</code> вернули HTTP 404.
Они встречаются в пяти местах английских руководств. Патч с предложенными заменами сохранён, но не применён.</p>
<p>""" + link("/report.html", "Открыть отчёт и пять проблемных переходов") + "</p>"
body += "<h2>Исходники прежних feature-веток</h2><ul>"
for alias, title in [
    ("sources-en", "EN — v3/features/machinemaker-manuals"),
    ("sources-ru", "RU — v20/features/machinemaker-publication"),
    ("sources-en-develop", "EN — v3/features/machinemaker-develop"),
    ("sources-ru-develop", "RU — v20/features/machinemaker-develop"),
]:
    body += "<li>" + link("/" + alias + "/", title) + "</li>"
body += "</ul><h2>Архивы сайтов, модели и примеры</h2><ul>"
for url, title in [
    ("/archives/preview-en.zip", "Полный английский preview — около 460 МБ"),
    ("/archives/preview-ru.zip", "Полный русский preview — около 108 МБ"),
    ("/examples/", "45 архивов примеров MachineMaker"),
    ("/archives/Hanwha-XD10.zip", "3D-модели Hanwha XD10"),
    ("/archives/MachineSchema.zip", "Конфигурация MachineSchema"),
]:
    body += "<li>" + link(url, title) + "</li>"
body += "</ul><p><small>Старый архив v5-20260921_1012-Swiss содержит смешанные языки и не является русским руководством для публикации.</small></p>"
(HERE / "index.html").write_text(page("MachineMaker — локальные материалы", body), encoding="utf-8")

legacy = json.loads((AUDIT / "legacy-links.json").read_text(encoding="utf-8-sig"))
report_rows = []
for item in legacy:
    if "kb.sprutcam.com" not in item["url"]:
        continue
    kind, lang = item["guide"].split("_")
    filename = Path(item["page"]).with_suffix(".html").name
    target = f"/checked-en/v3/machinemaker/{kind}/src/{filename}"
    report_rows.append("<tr><td>" + escape(item["guide"]) + "</td><td>" +
                       link(target, item["page"]) + f"<br>Строка исходника: {item['line']}</td><td>" +
                       escape(item["url"]) + "</td></tr>")
report = "<p>" + link("/", "← Все локальные руководства") + "</p><h1>Старые ссылки — сохранённая проверка</h1>"
report += "<p>Результаты от 8 октября 2026 года относятся к сентябрьским исходникам, а не к новым веткам MachineMaker/*.</p>"
report += '<div class="table"><table><tr><th>Руководство</th><th>Глава с проблемной ссылкой</th><th>Адрес, вернувший 404</th></tr>' + "".join(report_rows) + "</table></div>"
report += "<p>" + link("/reports/proposed-legacy-fixes-en.patch", "Предложенный патч (не применён)") + "</p>"
report += "<h2>Полный сохранённый отчёт</h2><pre>" + escape((AUDIT / "REVIEW-RU.md").read_text(encoding="utf-8-sig")) + "</pre>"
report += "<h2>Данные проверки</h2><ul>"
for filename in ["summary.json", "legacy-links.json", "built-checks.json", "browser-checks.json", "external-checks-verified.json", "build-en.log", "build-ru.log"]:
    report += "<li>" + link("/reports/" + filename, filename) + "</li>"
report += "</ul>"
(HERE / "report.html").write_text(page("MachineMaker — проверка старых ссылок", report), encoding="utf-8")
print("Created index.html and report.html for the saved snapshots.")
