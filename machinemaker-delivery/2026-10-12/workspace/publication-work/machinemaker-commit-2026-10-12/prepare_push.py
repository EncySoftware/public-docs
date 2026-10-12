"""Synchronize current delivery metadata before the explicitly requested commits/push."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import shutil
import sys

HERE = Path(__file__).resolve().parent
PUBLICATION = HERE.parent
WORKSPACE = PUBLICATION.parent
COLLECTION = PUBLICATION / 'machinemaker-six-2026-10-12'
sys.path.insert(0, str(PUBLICATION))
from commit_machinemaker_snapshot import git, stage_snapshot


def replace_text(path, transform):
    raw = path.read_bytes()
    bom = b'\xef\xbb\xbf' if raw.startswith(b'\xef\xbb\xbf') else b''
    newline = '\r\n' if b'\r\n' in raw else '\n'
    value = transform(raw.decode('utf-8-sig').replace('\r\n', '\n')).replace('\r\n', '\n').replace('\n', newline)
    path.write_bytes(bom + value.encode('utf-8'))


def main():
    guides = json.loads((COLLECTION / 'guides.json').read_text(encoding='utf-8'))
    delivery = json.loads((COLLECTION / 'delivery-checks.json').read_text(encoding='utf-8'))
    assert delivery['archive_crc_ok'] and delivery['page_count'] == 208
    internal = json.loads((COLLECTION / 'admin/internal-checks.json').read_text(encoding='utf-8'))
    branding = json.loads((COLLECTION / 'admin/robots-en-branding-browser-checks.json').read_text(encoding='utf-8'))
    assert not internal['errors'] and not branding['errors'] and not branding['http_failures']
    for language, expected_branch in [('en', 'v3/features/machinemaker-six-2026-10-12'), ('ru', 'v20/features/machinemaker-six-2026-10-12')]:
        repo = HERE / language
        assert git(repo, 'branch', '--show-current') == expected_branch
        snapshot = repo / 'machinemaker-delivery/2026-10-12'
        verification = snapshot / 'verification'
        for name in ('summary.json', 'internal-checks.json', 'browser-checks.json', 'revision-browser-checks.json', 'content-changes.json', 'files-sha256.json', 'ADMIN-HANDOFF-RU.md', 'robots-en-branding-revision.json', 'robots-en-branding-browser-checks.json'):
            shutil.copy2(COLLECTION / 'admin' / name, verification / name)
        shutil.copy2(COLLECTION / 'delivery-checks.json', verification / 'delivery-checks.json')
        shutil.copy2(COLLECTION / 'MachineMaker-six-manuals-2026-10-12.zip.sha256', verification / 'delivery.zip.sha256')
        if language == 'en':
            workspace = snapshot / 'workspace'
            for name in ('AGENTS.md', 'MachineMaker-session-handoff.md', 'MachineMaker-progress-2026-10-12.md'):
                shutil.copy2(WORKSPACE / name, workspace / name)
            shutil.copy2(COLLECTION / 'package_collection.py', workspace / 'publication-work/machinemaker-six-2026-10-12/package_collection.py')
            for folder, names in [
                ('machinemaker-sprutcam-audit-2026-10-12', ('audit.py', 'links.py', 'ocr.ps1', 'screenshots.py', 'REPORT-RU.md', 'text-report.json', 'links-report.json', 'ocr-report.json')),
                ('robots-en-ency-screenshots-2026-10-12', ('apply_revision.py', 'check_revision.py', 'finalize_revision.py', 'README-RU.md', 'prompts.md', 'revision.json', 'ocr-report.json', 'browser-checks.json', 'docfx-build.log')),
                ('machinemaker-commit-2026-10-12', ('prepare_push.py', 'server_delivery.py')),
            ]:
                target = workspace / 'publication-work' / folder
                target.mkdir(parents=True, exist_ok=True)
                for name in names:
                    shutil.copy2(PUBLICATION / folder / name, target / name)
        sha_line = 'The full delivery archive SHA256 is `' + delivery['package_sha256'] + '`.'
        replace_text(snapshot / 'README.md', lambda text: '\n'.join(sha_line if line.startswith('The full delivery archive SHA256 is ') else line for line in text.split('\n')).replace('This feature branch records local commits only.', 'This feature branch records the reviewed source and verification files.').replace('The source and verification files reflect this local revision, which has not been committed or pushed.', 'The source and verification files include this approved revision.') + '\n## Server handoff\n\nThe ready-made six-manual HTML/admin ZIP is supplied separately as a GitHub draft release asset, tag `machinemaker-six-manuals-2026-10-12`. It is not stored in Git. The checksum above is the current reviewed delivery. Static-site publication remains an administrator step.\n')
        stage_snapshot(repo, snapshot, language, [guide for guide in guides if guide['language'] == language])
        git(repo, '-c', 'core.whitespace=cr-at-eol', 'diff', '--cached', '--check')
    print('Both language snapshots are staged with exact source bytes and current delivery checks.', flush=True)


if __name__ == '__main__':
    main()
