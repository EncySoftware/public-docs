"""Prepare the six-manual static site and a concrete administrator handoff."""
from datetime import datetime, timezone
from html import escape
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
import hashlib
import json

ROOT = Path(__file__).resolve().parent
HTML = ROOT / "html"
ADMIN = ROOT / "admin"
PACKAGE = ROOT / "MachineMaker-six-manuals-2026-10-12.zip"
guides = json.loads((ROOT / "guides.json").read_text(encoding="utf-8"))
internal = json.loads((ADMIN / "internal-checks.json").read_text(encoding="utf-8"))
browser = json.loads((ADMIN / "browser-checks.json").read_text(encoding="utf-8"))
external = json.loads((ADMIN / "external-checks.json").read_text(encoding="utf-8"))
resources = json.loads((ADMIN / "localized-resources.json").read_text(encoding="utf-8"))
revision_path = ADMIN / "content-changes.json"
revision = json.loads(revision_path.read_text(encoding="utf-8")) if revision_path.exists() else None
revision_browser_path = ADMIN / "revision-browser-checks.json"
revision_browser = json.loads(revision_browser_path.read_text(encoding="utf-8")) if revision_browser_path.exists() else None
conversion_path = ADMIN / "turnmill-en-docfx-conversion.json"
conversion = json.loads(conversion_path.read_text(encoding="utf-8")) if conversion_path.exists() else None
branding_path = ADMIN / "robots-en-branding-revision.json"
branding = json.loads(branding_path.read_text(encoding="utf-8")) if branding_path.exists() else None
if internal["errors"] or browser["errors"] or browser["http_failures"]:
    raise RuntimeError("The local collection has unresolved verification failures")
if revision and (not revision_browser or revision_browser["errors"] or revision_browser["http_failures"]):
    raise RuntimeError("The approved content revision needs successful focused browser checks")


def sha256(path):
    value = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(2 * 1024 * 1024), b""):
            value.update(block)
    return value.hexdigest()


files = sorted(path for path in HTML.rglob("*") if path.is_file())
file_manifest = []
for number, path in enumerate(files, 1):
    file_manifest.append({"path": path.relative_to(HTML).as_posix(), "bytes": path.stat().st_size, "sha256": sha256(path)})
    if number % 250 == 0:
        print("CHECKSUMS", number, "of", len(files), flush=True)
(ADMIN / "files-sha256.json").write_text(json.dumps(file_manifest, ensure_ascii=False, indent=2), encoding="utf-8")

http_issues = [r for r in external["results"] if not r.get("status") or r["status"] >= 400]
video_issues = [r for r in external["results"] if r.get("video_metadata_status") not in [None, 200]]
summary = {"assembled_at": datetime.now(timezone.utc).isoformat(), "guide_count": len(guides), "page_count": sum(g["pages"] for g in guides),
           "guides": [{"key": g["key"], "label": g["label"], "entry": g["entry"], "pages": g["pages"], "source_ref": g["source_ref"], "source_sha": g["source_sha"]} for g in guides],
           "html_files": len(files), "html_bytes": sum(f["bytes"] for f in file_manifest),
           "browser_page_checks": sum(len(g["checks"]) for g in browser["guides"].values()),
           "internal_errors": internal["errors"], "browser_errors": browser["errors"], "http_resource_failures": browser["http_failures"],
           "localized_resource_count": len(resources["resources"]), "external_http_issues": http_issues, "video_metadata_issues": video_issues,
           "local_collection_ready": True, "remote_publication_performed": False,
           "publication_owner": "Administrator, after the user's handoff and content review"}
if revision:
    summary["content_revision"] = revision["revised_at"]
    summary["user_decisions"] = revision["decisions"]
    summary["revision_browser_page_checks"] = len(revision_browser["checks"])
if conversion:
    summary["turnmill_en_docfx_conversion"] = {"pages": len(conversion["pages"]), "removed_chapters": conversion["removed"],
                                              "errors": conversion["build_errors"], "warnings": conversion["build_warnings"]}
if branding:
    summary["robots_en_branding_revision"] = {"revised_at": branding["revised_at"], "images": len(branding["images"]), "caption": "ENCY axes map compatibility mode", "evidence": "robots-en-branding-revision.json", "browser_checks": "robots-en-branding-browser-checks.json"}
(ADMIN / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")

text = ["# Администратору: локальный комплект из шести руководств MachineMaker", "",
        "Подготовлен готовый статический HTML-комплект. Публичная выкладка выполняется администратором; в ходе подготовки серверы, CI и удалённые репозитории не менялись.", "",
        "## Что передать", "",
        "- MachineMaker-six-manuals-2026-10-12.zip — полный комплект.",
        "- MachineMaker-six-manuals-2026-10-12.zip.sha256 — контрольная сумма архива.",
        "- Этот файл ADMIN-HANDOFF-RU.md.", "",
        "После распаковки готовый сайт находится в html/, информация о сборке и проверках — в admin/.",
        "Локальная итоговая папка в рабочем пространстве: E:/astra/video/publication-work/machinemaker-six-2026-10-12/html/.",
        "Папки build-work/ и site/ в рабочем пространстве являются служебными промежуточными материалами и в архив не входят.", "",
        "## Состав: 6 руководств, 209 страниц", "",
        "| Руководство | Страниц | Папка внутри html/ | Главная страница |", "| --- | ---: | --- | --- |"]
for guide in guides:
    folder = guide["kind"] + "/" + guide["language"] + "/"
    text.append(f"| {guide['label']} | {guide['pages']} | {folder} | {guide['entry']} |")
text += ["", "Главная всего комплекта — html/index.html. Она содержит ровно шесть ссылок на руководства и общий поиск по 209 страницам.", "",
         "## Как посмотреть и разместить", "",
         "Для локального просмотра из папки распакованного архива:", "",
         "```powershell", "python -m http.server 8000 --bind 127.0.0.1", "```", "",
         "Открыть http://127.0.0.1:8000/html/ . Информация о проверке доступна через http://127.0.0.1:8000/admin/ .",
         "Для публикации скопировать СОДЕРЖИМОЕ html/ в согласованный каталог статического HTTP-сервера. Структуру milling/, turnmill/, robots/, _shared/ и assets/ сохранять целиком. Общий поисковый индекс search-index.json находится в корне сайта.",
         "Маршруты и ресурсы относительные: весь комплект можно разместить под одним HTTP-префиксом. Содержимое admin/ не является частью публичного сайта.",
         "При размещении EN и RU на разных доменах потребуется настроить межъязыковые ссылки главной страницы и разместить необходимые _shared-ресурсы рядом с книгами на каждом хосте. Сам комплект не назначает новый публичный URL и не перезаписывает существующие адреса.", "",
         "## Источники", ""]
for guide in guides:
    text += ["- " + guide["label"] + ": " + guide["source_ref"],
             "  - SHA: " + (guide["source_sha"] or "см. контрольные суммы восстановленного HTML"),
             "  - Дата / тип: " + guide["source_date"]]
text += ["", "Фрезерные EN/RU взяты из сохранённых проверенных исходников сентябрьской публикации (31/33 страницы). Они не выдаются за новую отдельную пару веток docs-work.",
         "Роботы EN/RU и токарно-фрезерный RU собраны из зафиксированных снимков docs-work. English TurnMilling — найденный пользователем оригинал на docs.encycam.com, 26 статей; прежний 25-страничный переводной черновик и ошибочно названная 30-страничная EN-ветка в комплект не включены.",
         "При последующем импорте English TurnMilling уникальные ID брать из js/lunr-data.js: исходный body pageid одинаков у всех статей. Числовые HTML-адреса оригинала сохранены.",
         "В текущей истории docs-work найдено четыре MachineMaker-ветки, а книг в комплекте шесть. Существующие четыре Jenkins-job/ветки нельзя автоматически считать публикацией всех шести книг. Для CI-публикации нужно отдельно назначить входы и раздельные маршруты Milling / TurnMill / Robots для обоих языков.", "",
         "## Проверки", "",
         "- Пять HTML-сборок DocFX 2.78.2: 0 ошибок / 0 предупреждений. English TurnMilling скопирован из восстановленного оригинала.",
         "- Полная повторная проверка 12 октября: 6 руководств, 209 страниц, 418 открытий Chrome на 1440 и 390 px.",
         "- Битых локальных файлов, ссылок, якорей, картинок и ответов HTTP 404 нет. Регистр путей проверен для размещения на Linux.",
         "- Поиск работает в каждой из шести книг и на общей главной странице, включая кириллицу.",
         ("- English TurnMilling: 24 статьи сохранены побайтово; в 6.html и 14.html удалены устаревшие ссылки по решению пользователя от 12 октября. Точные изменения и исходные контрольные суммы записаны в content-changes.json. Изображения не перекодировались." if revision else "- Все 26 HTML-статей оригинального English TurnMilling сохранены побайтово. Изображения не перекодировались."),
         "- 140 общих изображений и примеров локализованы. Локальные картинки и файлы примеров не зависят от GitHub Pages / GitHub Release.",
         "- Внешние видео и сторонние сайты остаются внешними ссылками. HTML-пакет не содержит сами видеопотоки. PDF в этот комплект не собирался.", "",
         "## Замечания перед публичной выкладкой", ""]
for issue in http_issues:
    text.append(f"- HTTP {issue.get('status')}: {issue['url']}")
    for ref in issue["references"]:
        text.append("  - " + ref["guide"] + ": " + ref["page"])
for issue in video_issues:
    text.append("- Видео требует проверки: " + issue["url"] + "; metadata HTTP " + str(issue.get("video_metadata_status")) + "; " + str(issue.get("video_reason", issue.get("playability_status", ""))))
    for ref in issue["references"]:
        text.append("  - " + ref["guide"] + ": " + ref["page"])
if revision:
    text += ["", "## Решения пользователя от 12 октября 2026", "",
             "- Три старых адреса kb.sprutcam.com устранены во всех пяти местах. В Milling EN ссылки на параметры сборки и кинематику заменены соответствующими внутренними главами. В TurnMilling EN удалена пустая ссылка в Toolbar; в обеих книгах удалена отсылка fix your CAD models к недоступной статье.",
             "- Ссылка MachineMaker Custom Imported Robot Cell удалена из Getting Started книги Robots EN и из поисковых индексов. Остальные видеоссылки сохранены.",
             "- Совместимость двух дополнительных примеров версии 16 подтверждена пользователем. Архивы и ссылки сохранены без изменений; повторная проверка в приложении в этом этапе не выполнялась.",
             "- Ссылка KUKA Download Center и описание Model Position сохранены по решению пользователя. Доступ к конкретным моделям в этом этапе не проверялся; изменения по этому пункту не требуются.",
             "- Исходные снимки от 9 октября сохранены. Правки выполнены в итоговом HTML и изолированных рабочих копиях; content-changes.json содержит перечень и контрольные суммы до/после, revision-baseline-2026-10-09/ — исходные версии изменённых файлов.",
             "- После правок повторно проверены все внутренние ссылки 209 страниц, а в браузере — изменённые страницы, новые переходы и поиск. Результаты: internal-checks.json и revision-browser-checks.json.", "",
             "## Оставшиеся проверки содержания", "",
             "- Полное воспроизведение всех видео и соответствие их содержания инструкциям не проверялись. Видео остаются внешними ресурсами."]
else:
    text += ["- Два старых ZIP-примера версии 16 сохранены локально в _shared/examples/legacy-v16/. Их актуальность и совместимость с текущим приложением не подтверждены.",
             "- Получение моделей с внешнего KUKA Download Center и соответствие всех видео инструкциям не проверялись.",
             "- Эти замечания относятся к исходному содержанию; при сборке книги не переписывались."]
if conversion:
    text += ["", "## English TurnMilling: единое оформление DocFX", "",
             "- По дополнительному поручению пользователя английская книга собрана в DocFX 2.78.2 с тем же шаблоном, что и русская токарно-фрезерная книга.",
             "- Глава Trevisan Machine (73.html) исключена из этой книги, оглавления и поиска. В других книгах главы Trevisan сохранены.",
             "- Осталось 25 страниц; числовые адреса оставшихся глав, включая 1.html, 30.html и 30_1.html, сохранены.",
             "- Текст, текстовые ссылки, якоря и изображения оставшихся статей сверены с предыдущей проверенной HTML-версией. Изображения и файлы примеров скопированы без перекодирования и проверены по SHA256.",
             "- Исходники нового DocFX-проекта: build-work/turnmill-en/main/ в рабочей папке. Сведения о переносе: turnmill-en-docfx-conversion.json; сборка: turnmill-en-build.log."]
text += ["",
         "## Доказательства", "",
         "inputs.json — исходные снимки; internal-checks.json — локальные ссылки и контроль исходных/согласованно изменённых статей; browser-checks.json — исходная полная проверка браузером; revision-browser-checks.json — проверка правок от 12 октября; content-changes.json — согласованные изменения; external-checks.json — внешние ссылки и история устранённых замечаний; localized-resources.json — локальные копии общих файлов и подтверждение совместимости примеров; files-sha256.json — все файлы сайта и SHA256; *-build.log — логи исходных сборок."]
if branding:
    text += ["", "## Robots EN: надпись на иллюстрациях", "",
             "По поручению пользователя на двух иллюстрациях главы Building a kinematic scheme (131903495.html), разделы Limits и Model Position, слово SprutCAM заменено на ENCY. Новая надпись: ENCY axes map compatibility mode.",
             "Исходные изображения сохранены вне публикуемого сайта. Новые изображения включены в английские исходники и HTML; ширина отображения сохранена, высота адаптируется к узкому экрану. Текст главы, якоря и текстовые ссылки сохранены.",
             "Доказательства: robots-en-branding-revision.json, robots-en-branding-browser-checks.json и content-changes.json. OCR подтверждает ENCY в обеих надписях; страница проверена на 1440 и 390 px."]
text = [line.replace("209", str(summary["page_count"])).replace("418", str(summary["browser_page_checks"])) for line in text]
if conversion:
    text = [
        ("- Шесть HTML-сборок DocFX 2.78.2: 0 ошибок / 0 предупреждений; последняя сборка — перенос English TurnMilling в общий шаблон." if line.startswith("- Пять HTML-сборок") else
         "- English TurnMilling: исходные тексты 25 оставшихся статей сохранены и проверены; глава Trevisan исключена по решению пользователя. Разметка страниц собрана DocFX. Подробности — turnmill-en-docfx-conversion.json." if line.startswith("- English TurnMilling: 24") else
         "При повторном импорте исходного HTML English TurnMilling нельзя использовать одинаковый body pageid как уникальный ID. Исходная карта страниц сохранена в восстановленном оригинале; новый DocFX-проект сохраняет числовые имена файлов и якоря. Подробности переноса — turnmill-en-docfx-conversion.json." if line.startswith("При последующем импорте English TurnMilling") else
         line.replace("English TurnMilling — найденный пользователем оригинал на docs.encycam.com, 26 статей;", "English TurnMilling — найденный пользователем оригинал на docs.encycam.com, перенесённый в DocFX: 25 статей после исключения Trevisan;")
        ) for line in text]
if not http_issues and not video_issues:
    text = [line for line in text if line != "## Замечания перед публичной выкладкой"]
(ADMIN / "ADMIN-HANDOFF-RU.md").write_text("\n".join(text) + "\n", encoding="utf-8-sig", newline="\r\n")

rows = []
for guide in guides:
    rows.append('<tr><td>' + escape(guide["label"]) + '</td><td>' + str(guide["pages"]) + '</td><td><a data-book="' + guide["entry"] + '" href="../html/' + guide["entry"] + '">Открыть</a></td></tr>')
admin_html = '<!doctype html><html lang="ru"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>MachineMaker — пакет для администратора</title><style>body{font:16px/1.65 system-ui;max-width:1160px;margin:auto;padding:25px;color:#242a33}a{color:#075db5}table{width:100%;border-collapse:collapse}td,th{padding:12px;border-bottom:1px solid #ddd;text-align:left}pre{white-space:pre-wrap;overflow-wrap:anywhere}.notice{padding:16px;background:#fff4d8}.table{overflow:auto}</style><h1>MachineMaker — локальный комплект из шести руководств</h1><p class="notice">Сайт собран и проверен локально. Архив и инструкция подготовлены для передачи администратору. Публичная выкладка не выполнялась.</p><p id="package"><a href="/machinemaker-six-package.zip">Скачать полный пакет</a></p><p><a href="ADMIN-HANDOFF-RU.md">Инструкция для администратора</a> · <a href="summary.json">Результаты</a> · <a href="files-sha256.json">Контрольные суммы файлов</a></p><div class="table"><table><tr><th>Руководство</th><th>Страниц</th><th>Просмотр</th></tr>' + ''.join(rows) + '</table></div><h2>Инструкция и замечания</h2><pre>' + escape('\n'.join(text)) + '</pre><script>const local=location.pathname.startsWith("/machinemaker-six-admin");document.getElementById("package").hidden=!local;if(local){document.querySelectorAll("a[data-book]").forEach(a=>a.href="/machinemaker-six/"+a.dataset.book)}</script></html>'
(ADMIN / "index.html").write_text(admin_html, encoding="utf-8")

pending_package = PACKAGE.with_suffix(".pending.zip")
with ZipFile(pending_package, "w", compression=ZIP_DEFLATED, compresslevel=1, allowZip64=True) as bundle:
    zipped = 0
    for path in files:
        bundle.write(path, "html/" + path.relative_to(HTML).as_posix())
        zipped += path.stat().st_size
        if zipped // (100 * 1024 * 1024) != (zipped - path.stat().st_size) // (100 * 1024 * 1024):
            print("ZIP HTML", round(zipped / 1024 / 1024), "MiB of", round(summary["html_bytes"] / 1024 / 1024), flush=True)
    for path in sorted(ADMIN.rglob("*")):
        if path.is_file():
            bundle.write(path, "admin/" + path.relative_to(ADMIN).as_posix())
with ZipFile(pending_package) as archive:
    names = archive.namelist()
    for guide in guides:
        if "html/" + guide["entry"] not in names:
            raise RuntimeError("Package lacks the main page of " + guide["key"])
    if any(name.startswith(("site/", "build-work/")) for name in names):
        raise RuntimeError("Intermediate output was accidentally packaged")
    bad_file = archive.testzip()
    if bad_file:
        raise RuntimeError("Archive CRC failed: " + bad_file)
    for path in sorted(ADMIN.rglob("*")):
        if path.is_file() and archive.read("admin/" + path.relative_to(ADMIN).as_posix()) != path.read_bytes():
            raise RuntimeError("Archive administrator file differs from delivery: " + str(path))
archive_hash = sha256(pending_package)
pending_package.replace(PACKAGE)
(ROOT / (PACKAGE.name + ".sha256")).write_text(archive_hash + "  " + PACKAGE.name + "\n", encoding="ascii")
delivery = {"checked_at": datetime.now(timezone.utc).isoformat(), "archive_entries": len(names), "site_files": len(files),
            "archive_crc_ok": True, "guide_count": len(guides), "page_count": sum(g["pages"] for g in guides),
            "package_bytes": PACKAGE.stat().st_size, "package_sha256": archive_hash}
(ROOT / "delivery-checks.json").write_text(json.dumps(delivery, ensure_ascii=False, indent=2), encoding="utf-8")
print("PACKAGE READY", PACKAGE, PACKAGE.stat().st_size, "bytes", archive_hash, flush=True)
