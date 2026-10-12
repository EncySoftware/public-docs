"""Record the finished local revision and synchronize EN delivery evidence."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import shutil

REV = Path(__file__).resolve().parent
WORKSPACE = REV.parent.parent
DELIVERY = REV.parent / 'machinemaker-six-2026-10-12'
SNAPSHOT = REV.parent / 'machinemaker-commit-2026-10-12/en/machinemaker-delivery/2026-10-12'


def update_text(path, transform):
    raw = path.read_bytes()
    bom = b'\xef\xbb\xbf' if raw.startswith(b'\xef\xbb\xbf') else b''
    newline = '\r\n' if b'\r\n' in raw else '\n'
    value = raw.decode('utf-8-sig').replace('\r\n', '\n')
    value = transform(value).replace('\r\n', '\n').replace('\n', newline)
    path.write_bytes(bom + value.encode('utf-8'))


def main():
    revision = json.loads((REV / 'revision.json').read_text(encoding='utf-8'))
    delivery = json.loads((DELIVERY / 'delivery-checks.json').read_text(encoding='utf-8'))
    assert delivery['archive_crc_ok']
    revision['delivery'] = delivery
    revision['local_changes_committed'] = False
    revision['remote_publication_performed'] = False
    (REV / 'revision.json').write_text(json.dumps(revision, ensure_ascii=False, indent=2), encoding='utf-8')
    package_hash = delivery['package_sha256']
    package_bytes = f'{delivery["package_bytes"]:,}'.replace(',', ' ')
    previous_hash = revision['old_delivery']['package_sha256']
    previous_bytes = f'{revision["old_delivery"]["package_bytes"]:,}'.replace(',', ' ')
    progress = WORKSPACE / 'MachineMaker-progress-2026-10-12.md'
    update_text(progress, lambda text: text.replace(previous_hash, package_hash).replace(previous_bytes, package_bytes).replace('Изменения от 12 октября:\n', 'Изменения от 12 октября:\n\n- На двух иллюстрациях Robots EN в Building a kinematic scheme (Limits и Model Position) слово SprutCAM заменено на ENCY. Обновлены рабочие английские исходники, HTML и ZIP; страница повторно проверена на 1440 / 390 px. Эта правка пока не закоммичена.\n', 1))
    heading = '## Последняя правка: надпись ENCY на двух иллюстрациях Robots EN\n\n'
    note = heading + (
        'По прямому поручению пользователя на двух скриншотах главы Building a kinematic scheme\n'
        '(131903495.html), подразделы Limits и Model Position, SprutCAM заменён на ENCY.\n'
        'Надпись теперь: `ENCY axes map compatibility mode`. Использован built-in image_gen.\n'
        'Изменены английские исходники в рабочей копии `machinemaker-commit-2026-10-12/en/`\n'
        'и в `machinemaker-six-2026-10-12/build-work/robots-en/main/`, готовый HTML и ZIP.\n'
        'Оригиналы сохранены вне публикуемого дерева; новые PNG имеют имена по SHA256.\n'
        'Ширина отображения сохранена, высота адаптивна. Текст главы, якоря и текстовые ссылки сохранены.\n'
        'DocFX: 0 ошибок / 0 предупреждений; OCR: ENCY на обеих картинках, SprutCAM не найден;\n'
        'браузер 1440 / 390 px: 0 ошибок; внутренние ссылки 208 страниц: 0 ошибок; ZIP CRC пройден.\n'
        f'Текущий ZIP: {package_bytes} байт, SHA256 `{package_hash}`.\n'
        'Правки EN остаются НЕЗАКОММИЧЕННЫМИ поверх cc468c0; RU не менялся. Push и публикации не было.\n'
        'Доказательства и промпт: `publication-work/robots-en-ency-screenshots-2026-10-12/`.\n'
        'Текущие отчёты также включены в admin/ ZIP и verification/ английской рабочей копии.\n\n'
        'Уточнение по фрезерному EN: упоминания остаются только в двух адресах download.sprutcam.com\n'
        'в исходнике 3-axes-milling-machine.md:12. В готовом HTML обе ссылки уже локальные.\n'
        'Эти исходные адреса и комментарий SPRUTCAM LIGHT THEME в CSS TurnMilling EN в этой правке не менялись.\n'
        'Аудит до исправления: `publication-work/machinemaker-sprutcam-audit-2026-10-12/REPORT-RU.md`.\n\n'
    )
    handoff = WORKSPACE / 'MachineMaker-session-handoff.md'
    update_text(handoff, lambda text: text.replace('# MachineMaker — сохранённый процесс работы\n\n', '# MachineMaker — сохранённый процесс работы\n\n' + note, 1).replace('## Последнее действие: изменения сохранены двумя локальными Git-коммитами', '## Предыдущий этап: изменения сохранены двумя локальными Git-коммитами', 1))
    audit = WORKSPACE / 'publication-work/machinemaker-sprutcam-audit-2026-10-12/REPORT-RU.md'
    update_text(audit, lambda text: text.replace('# Проверка английских руководств MachineMaker — 12 октября 2026\n\n', '# Проверка английских руководств MachineMaker — 12 октября 2026\n\n**Обновление после аудита:** по поручению пользователя SprutCAM заменён на ENCY на обеих иллюстрациях Robots EN. Обновлены исходники, HTML и ZIP. [Сведения об исправлении](E:/astra/video/publication-work/robots-en-ency-screenshots-2026-10-12/README-RU.md). Ниже сохранён результат проверки ДО этой правки; два адреса в исходнике Milling EN и комментарий CSS пока остаются.\n\n', 1).replace('machinemaker-six-2026-10-12/html/robots/en/src/assets/3575d6a240d0d00e23009b9abb76f3f16071aebbeeeea8d8bd895f743dad82a5.png', 'robots-en-ency-screenshots-2026-10-12/before/html-assets/3575d6a240d0d00e23009b9abb76f3f16071aebbeeeea8d8bd895f743dad82a5.png').replace('machinemaker-six-2026-10-12/html/robots/en/src/assets/3416680d67cea5b40aefd0fea069ff2eeafcecc7fa47ed5c8231fde19da3ff51.png', 'robots-en-ency-screenshots-2026-10-12/before/html-assets/3416680d67cea5b40aefd0fea069ff2eeafcecc7fa47ed5c8231fde19da3ff51.png'))
    readme = (
        '# Robots EN — замена надписи на иллюстрациях\n\n'
        'По поручению пользователя на двух иллюстрациях SprutCAM заменён на ENCY. Надпись: `ENCY axes map compatibility mode`.\n\n'
        '[Открыть изменённую главу](http://127.0.0.1:8765/machinemaker-six/robots/en/src/content/131903495.html#limits). Подразделы: Limits и Model Position.\n\n'
        'Использован built-in image_gen; [точный промпт](prompts.md). Оба результата сохранены в рабочем пространстве:\n\n'
        '- [Limits — ENCY](images/limits-ency.png).\n'
        '- [Model Position / axis options — ENCY](images/axis-options-ency.png).\n\n'
        'Новые PNG включены в рабочие английские исходники, HTML и ZIP под именами по SHA256. Старые изображения сохранены в before/ вне публикуемых деревьев.\n\n'
        'Текст статьи, якоря и ссылки сохранены. DocFX: 0 ошибок и предупреждений. OCR подтверждает ENCY в обеих надписях и не находит SprutCAM. Страница проверена на 1440 и 390 px; пропорции картинок проверены. Все 208 статей прошли проверку внутренних ссылок. ZIP прошёл CRC.\n\n'
        f'ZIP: {package_bytes} байт; SHA256 `{package_hash}`.\n\n'
        'Правки в английской feature-ветке пока не закоммичены. Push и публикация не выполнялись. Русские исходники не менялись.\n\n'
        'По фрезерному EN: слово SprutCAM остаётся только в домене двух исходных ссылок download.sprutcam.com в 3-axes-milling-machine.md:12. В готовой странице эти ссылки локальные. Комментарий CSS TurnMilling EN в этой правке также не менялся.\n\n'
        'Доказательства: revision.json, ocr-report.json, browser-checks.json, docfx-build.log и screenshots/.\n'
    )
    (REV / 'README-RU.md').write_text(readme, encoding='utf-8')
    verification = SNAPSHOT / 'verification'
    for filename in ('content-changes.json', 'internal-checks.json', 'browser-checks.json', 'revision-browser-checks.json', 'files-sha256.json', 'summary.json', 'ADMIN-HANDOFF-RU.md', 'robots-en-branding-revision.json', 'robots-en-branding-browser-checks.json'):
        shutil.copy2(DELIVERY / 'admin' / filename, verification / filename)
    shutil.copy2(DELIVERY / 'delivery-checks.json', verification / 'delivery-checks.json')
    shutil.copy2(DELIVERY / 'MachineMaker-six-manuals-2026-10-12.zip.sha256', verification / 'delivery.zip.sha256')
    shutil.copy2(REV / 'docfx-build.log', verification / 'robots-en-build.log')
    update_text(SNAPSHOT / 'README.md', lambda text: text.replace(previous_hash, package_hash) + '\n## Local screenshot revision after the snapshot commit\n\nTwo Robots EN screenshots in Building a kinematic scheme now read "ENCY axes map compatibility mode", as explicitly requested by the user. The source and verification files reflect this local revision, which has not been committed or pushed. Originals are archived outside this source tree. Focused browser checks at 1440/390 px, OCR and the standalone DocFX build passed. The delivery archive and its SHA256 are updated in verification/.\n')
    manifest_path = SNAPSHOT / 'snapshot-manifest.json'
    saved = json.loads(manifest_path.read_text(encoding='utf-8-sig'))
    saved['revised_at'] = datetime.now(timezone.utc).isoformat()
    saved['local_revision'] = 'Robots EN screenshot text: SprutCAM -> ENCY; uncommitted.'
    saved['files'] = []
    for path in sorted(SNAPSHOT.rglob('*')):
        if not path.is_file() or path == manifest_path:
            continue
        raw = path.read_bytes()
        saved['files'].append({'path': path.relative_to(SNAPSHOT).as_posix(), 'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest(), 'git_blob': hashlib.sha1(b'blob ' + str(len(raw)).encode('ascii') + b'\0' + raw).hexdigest()})
    update_text(manifest_path, lambda text: json.dumps(saved, ensure_ascii=False, indent=2) + '\n')
    print('Progress, handoff, audit history and EN snapshot verification synchronized.')


if __name__ == '__main__':
    main()
