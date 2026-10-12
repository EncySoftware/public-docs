# Robots EN — замена надписи на иллюстрациях

По поручению пользователя на двух иллюстрациях SprutCAM заменён на ENCY. Надпись: `ENCY axes map compatibility mode`.

[Открыть изменённую главу](http://127.0.0.1:8765/machinemaker-six/robots/en/src/content/131903495.html#limits). Подразделы: Limits и Model Position.

Использован built-in image_gen; [точный промпт](prompts.md). Оба результата сохранены в рабочем пространстве:

- [Limits — ENCY](images/limits-ency.png).
- [Model Position / axis options — ENCY](images/axis-options-ency.png).

Новые PNG включены в рабочие английские исходники, HTML и ZIP под именами по SHA256. Старые изображения сохранены в before/ вне публикуемых деревьев.

Текст статьи, якоря и ссылки сохранены. DocFX: 0 ошибок и предупреждений. OCR подтверждает ENCY в обеих надписях и не находит SprutCAM. Страница проверена на 1440 и 390 px; пропорции картинок проверены. Все 208 статей прошли проверку внутренних ссылок. ZIP прошёл CRC.

ZIP: 1 068 825 428 байт; SHA256 `513241f4f0ab16743274fb5d22238056b040f9a56ef10558ecc654cd6eea7e15`.

Правки в английской feature-ветке пока не закоммичены. Push и публикация не выполнялись. Русские исходники не менялись.

По фрезерному EN: слово SprutCAM остаётся только в домене двух исходных ссылок download.sprutcam.com в 3-axes-milling-machine.md:12. В готовой странице эти ссылки локальные. Комментарий CSS TurnMilling EN в этой правке также не менялся.

Доказательства: revision.json, ocr-report.json, browser-checks.json, docfx-build.log и screenshots/.
