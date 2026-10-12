# Проверка английских руководств MachineMaker — 12 октября 2026

**Обновление после аудита:** по поручению пользователя SprutCAM заменён на ENCY на обеих иллюстрациях Robots EN. Обновлены исходники, HTML и ZIP. [Сведения об исправлении](E:/astra/video/publication-work/robots-en-ency-screenshots-2026-10-12/README-RU.md). Ниже сохранён результат проверки ДО этой правки; два адреса в исходнике Milling EN и комментарий CSS пока остаются.

**Отсутствие упоминаний SprutCAM не подтверждено: найдены два скриншота с названием продукта, два адреса в исходнике и комментарий в CSS.**

Проверен актуальный комплект `machinemaker-six-2026-10-12`: Milling EN — 31 статья, Robots EN — 47, TurnMilling EN — 25. Всего 103 английские статьи. Проверены рабочие исходники сборки, исходники последнего английского коммита, готовый HTML и английские текстовые файлы ZIP. Исторические экспорты и русские руководства в эту проверку не входят.

## Последние коммиты

| Язык | Коммит | Ветка | Время, Москва |
| --- | --- | --- | --- |
| EN | `cc468c0aeadb5db3fc65e2468a4a684408f08852` | `v3/features/machinemaker-six-2026-10-12` | 12.10.2026 10:33:58 |
| RU | `2785faddf7d3546034d253a07af10fe8bf7a1e1b` | `v20/features/machinemaker-six-2026-10-12` | 12.10.2026 10:34:00 |

Рабочие копии `publication-work/machinemaker-commit-2026-10-12/en/` и `ru/` чистые. Проверка `git ls-remote` подтвердила: соответствующие feature-ветки отсутствуют на origin; develop остаются на `d2f8b1392cd06f1a847c2ef70ea52fb46988a61c` и `958d24b96096c7699d2bc3132949847cda7fdf4d`. Коммиты сохранены локально; публикация этого комплекта не выполнялась.

Сводка коммитов: [commits.json](E:/astra/video/publication-work/machinemaker-commit-2026-10-12/commits.json).

## Найденные упоминания

1. **Две иллюстрации в Robots EN, «Building a kinematic scheme».** На обеих видна надпись `SprutCAM axes map compatibility mode`. Совпадения OCR подтверждены визуальным просмотром. Иллюстрации присутствуют в готовом сайте, в закоммиченном исходнике и в ZIP; байты во всех трёх местах совпадают.

   Страница: [131903495.html](E:/astra/video/publication-work/machinemaker-six-2026-10-12/html/robots/en/src/content/131903495.html:288). Исходник: [131903495.md](E:/astra/video/publication-work/machinemaker-commit-2026-10-12/en/machinemaker-delivery/2026-10-12/source/robots/main/src/content/131903495.md:49).

   [Первая иллюстрация](E:/astra/video/publication-work/robots-en-ency-screenshots-2026-10-12/before/html-assets/3575d6a240d0d00e23009b9abb76f3f16071aebbeeeea8d8bd895f743dad82a5.png), [вторая иллюстрация](E:/astra/video/publication-work/robots-en-ency-screenshots-2026-10-12/before/html-assets/3416680d67cea5b40aefd0fea069ff2eeafcecc7fa47ed5c8231fde19da3ff51.png).

2. **Две ссылки `download.sprutcam.com` в Milling EN, «3-Axes Milling Machine».** Они сохранены в [закоммиченном исходнике](E:/astra/video/publication-work/machinemaker-commit-2026-10-12/en/machinemaker-delivery/2026-10-12/source/milling/docs/machinemaker/machines/src/3-axes-milling-machine.md:12) и рабочей копии сборки:

   - `https://download.sprutcam.com/download/sprutcam/MachineMaker/version_16/examples/3AxesMillingMachine/Milling_machine_3ax.zip`
   - `https://download.sprutcam.com/download/sprutcam/MachineMaker/version_16/examples/3AxesMillingMachine/Milling_machine.zip`

   Оба адреса доступны: HTTP 206 при запросе части файла. В готовом HTML и ZIP ссылки заменены локальными `../../../_shared/examples/legacy-v16/Milling_machine_3ax.zip` и `Milling_machine.zip`; файлов на месте хватает для работы этих ссылок.

3. **Комментарий `SPRUTCAM LIGHT THEME` в CSS TurnMilling EN.** На странице он не отображается, но входит в готовый сайт и ZIP: [styles/main.css:667](E:/astra/video/publication-work/machinemaker-six-2026-10-12/html/turnmill/en/styles/main.css:667). Такой же комментарий есть в [шаблоне закоммиченного исходника](E:/astra/video/publication-work/machinemaker-commit-2026-10-12/en/machinemaker-delivery/2026-10-12/source/turnmill/main/template/custom/styles/main.css:667). Следующая строка ссылается на оформление `sprut.ru`.

## Проверка всех ссылок

- Проверены **6 362 внутренних вхождения ссылок и адресов ресурсов**: HTML, изображения, скрипты, стили, CSS `url()`, оглавления JSON, поисковые индексы. Проверены наличие файлов, регистр путей и якоря. Ошибок нет. Число включает повторяющиеся адреса на разных страницах.
- Проверены **37 различных внешних адресов**: 25 используются готовым сайтом, ещё 12 присутствуют только в закоммиченных исходниках. Все доступны: HTTP 200 для страниц и HTTP 206 для архивов, проверенных частичным запросом.
- Перенаправления прослежены. В действующих адресах готового английского сайта и их перенаправлениях SprutCAM не найден. Два прямых адреса SprutCAM перечислены выше; они остались только в исходнике.
- Для всех 23 YouTube-ссылок получены метаданные HTTP 200 и анонимный статус плеера `OK`. В названиях видео и авторов SprutCAM не обнаружен. Полное воспроизведение и содержание роликов не проверялись.

## Остальные результаты и границы проверки

В отображаемом тексте 103 статей, HTML-атрибутах, английских записях общего и локальных поисковых индексов упоминаний SprutCAM не найдено. Поиск учитывает регистр, пробелы и дефисы, HTML-сущности, URL-кодирование и JSON-экранирование.

Проверены 158 английских текстовых файлов ZIP: они побайтово совпадают с текущим HTML. Единственное текстовое совпадение в них — комментарий CSS, указанный выше.

OCR обработал 577 кадров из 363 растровых иллюстраций без ошибок. Для анимаций взяты первый, средний и последний кадры; маленькие значки менее 100 × 100 пикселей пропущены, SVG проверены как текст. OCR помогает найти надписи и не доказывает отсутствие всех возможных упоминаний. Содержимое скачиваемых двоичных примеров и внешних видео не исследовалось.

Документация, исходники репозиториев, готовый HTML и ZIP не изменялись. Созданы только материалы этой проверки.

Подробные данные: [текстовая проверка](E:/astra/video/publication-work/machinemaker-sprutcam-audit-2026-10-12/text-report.json), [ссылки](E:/astra/video/publication-work/machinemaker-sprutcam-audit-2026-10-12/links-report.json), [OCR](E:/astra/video/publication-work/machinemaker-sprutcam-audit-2026-10-12/ocr-report.json).

Для повторения проверки выполнить `python audit.py`, затем `powershell.exe -NoProfile -ExecutionPolicy Bypass -File ocr.ps1` и `python links.py` из этой папки. Временные PNG для OCR создаются первым скриптом; после проверки их можно удалить.
