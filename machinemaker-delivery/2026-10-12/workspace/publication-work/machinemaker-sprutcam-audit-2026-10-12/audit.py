"""Read-only brand audit of the latest MachineMaker English delivery."""
from __future__ import annotations

import hashlib
import html
import json
import re
import sys
import unicodedata
import zipfile
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import unquote, urlsplit

AUDIT = Path(__file__).resolve().parent
WORKSPACE = AUDIT.parent.parent
sys.path.insert(0, str(WORKSPACE / 'publication-work/audit-2026-10-08/tools/python'))
from bs4 import BeautifulSoup
from PIL import Image

DELIVERY = WORKSPACE / 'publication-work/machinemaker-six-2026-10-12'
SITE = DELIVERY / 'html'
SNAPSHOT = WORKSPACE / 'publication-work/machinemaker-commit-2026-10-12/en/machinemaker-delivery/2026-10-12'
PATTERN = re.compile(r'sprut[\s_-]*cam|спрут[\s_-]*кам', re.I)
TEXT_SUFFIXES = {'.md', '.html', '.htm', '.css', '.js', '.json', '.map', '.yml', '.yaml', '.txt', '.xml', '.svg', '.partial', '.tmpl', '.config', '.ini', '.toml', '.py', '.ps1', '.sh'}


def relative(path):
    return Path(path).resolve().relative_to(WORKSPACE).as_posix()


def normalize(value):
    value = html.unescape(unquote(value))
    value = unicodedata.normalize('NFKC', value)
    return re.sub('[\u200b-\u200d\ufeff]', '', value)


def matches(value):
    value = normalize(value)
    return [{'match': m.group(), 'context': value[max(0, m.start()-90):m.end()+150].replace('\n', ' ')} for m in PATTERN.finditer(value)]


def scan_file(path):
    findings = []
    data = path.read_text(encoding='utf-8-sig')
    for number, line in enumerate(data.splitlines(), 1):
        for match in matches(line):
            findings.append({'path': relative(path), 'line': number, **match})
    if path.suffix.lower() in {'.json', '.map'}:
        try:
            decoded = json.dumps(json.loads(data), ensure_ascii=False)
        except ValueError:
            pass
        else:
            if not findings:
                findings.extend({'path': relative(path), 'line': None, 'decoded_json': True, **m} for m in matches(decoded))
    return findings


def scan_tree(root):
    files = sorted(p for p in root.rglob('*') if p.is_file() and p.suffix.lower() in TEXT_SUFFIXES)
    findings = [finding for path in files for finding in scan_file(path)]
    names = [{'path': relative(p), **m} for p in root.rglob('*') for m in matches(p.name)]
    return {'root': relative(root), 'text_files_checked': len(files), 'findings': findings, 'filename_findings': names}


def main():
    guides = [g for g in json.loads((DELIVERY / 'guides.json').read_text(encoding='utf-8-sig')) if g['language'] == 'en']
    report = {'checked_at_utc': datetime.now(timezone.utc).isoformat(), 'commits': json.loads((WORKSPACE / 'publication-work/machinemaker-commit-2026-10-12/commits.json').read_text(encoding='utf-8-sig')), 'guides': [], 'article_findings': [], 'missing_local_resources': [], 'text_scans': [], 'archive': {}, 'ocr_inputs': [], 'limits': ['Text inspection covers current English source projects and delivery files, with HTML entities, percent encoding and JSON escapes decoded.', 'Historical workspace notes and Russian manuals are outside the English manual scope.', 'OCR is a supporting check, not proof of absence; animations are sampled at first, middle and last frame. External videos and the contents of downloadable binary examples are not inspected.']}
    image_uses = {}
    shared = set()
    for guide in guides:
        root = SITE / guide['kind'] / 'en'
        report['guides'].append({'key': guide['key'], 'articles': len(guide['articles']), 'entry': relative(root / Path(guide['entry']).relative_to(Path(guide['kind']) / 'en'))})
        report['text_scans'].append({'scope': 'built_html', 'guide': guide['key'], **scan_tree(root)})
        for article in guide['articles']:
            path = root / article
            soup = BeautifulSoup(path.read_text(encoding='utf-8-sig'), 'html.parser')
            for tag in soup(['script', 'style']):
                tag.decompose()
            for match in matches(soup.get_text(' ', strip=True)):
                report['article_findings'].append({'path': relative(path), 'kind': 'visible_text', **match})
            for tag in soup.find_all(True):
                for name, value in tag.attrs.items():
                    for match in matches(' '.join(value) if isinstance(value, list) else str(value)):
                        report['article_findings'].append({'path': relative(path), 'kind': 'attribute', 'attribute': name, **match})
                for attr in ('src', 'href', 'poster'):
                    value = tag.get(attr)
                    if not value or urlsplit(value).scheme or value.startswith(('#', '//')):
                        continue
                    target = (path.parent / unquote(urlsplit(value).path)).resolve()
                    if not target.is_relative_to(SITE.resolve()):
                        continue
                    if not target.is_file():
                        report['missing_local_resources'].append({'article': relative(path), 'target': relative(target)})
                        continue
                    if not target.is_relative_to(root.resolve()):
                        shared.add(target)
                    if tag.name == 'img' and attr == 'src':
                        image_uses.setdefault(target, []).append(relative(path))
        report['text_scans'].append({'scope': 'build_source', 'guide': guide['key'], **scan_tree(DELIVERY / 'build-work' / guide['key'])})
        report['text_scans'].append({'scope': 'committed_source', 'guide': guide['key'], **scan_tree(SNAPSHOT / 'source' / guide['kind'])})

    global_index = json.loads((SITE / 'search-index.json').read_text(encoding='utf-8-sig'))
    english_index = [row for row in global_index if row.get('language') == 'en']
    report['global_search'] = {'english_entries': len(english_index), 'findings': matches(json.dumps(english_index, ensure_ascii=False))}
    report['shared_resource_findings'] = [finding for path in sorted(shared) if path.suffix.lower() in TEXT_SUFFIXES for finding in scan_file(path)]
    report['shared_resources_checked'] = len(shared)

    archive = DELIVERY / 'MachineMaker-six-manuals-2026-10-12.zip'
    with zipfile.ZipFile(archive) as package:
        selected = [info for info in package.infolist() if any(info.filename.startswith(f'html/{g["kind"]}/en/') for g in guides) and Path(info.filename).suffix.lower() in TEXT_SUFFIXES]
        archive_findings, mismatches = [], []
        for info in selected:
            raw = package.read(info)
            data = raw.decode('utf-8-sig')
            for number, line in enumerate(data.splitlines(), 1):
                archive_findings.extend({'member': info.filename, 'line': number, **m} for m in matches(line))
            if hashlib.sha256(raw).digest() != hashlib.sha256((DELIVERY / info.filename).read_bytes()).digest():
                mismatches.append(info.filename)
        archived_index = [row for row in json.loads(package.read('html/search-index.json')) if row.get('language') == 'en']
        report['archive'] = {'path': relative(archive), 'english_text_files_checked': len(selected), 'findings': archive_findings, 'different_from_loose_html': mismatches, 'english_search_entries': len(archived_index), 'english_search_findings': matches(json.dumps(archived_index, ensure_ascii=False))}

    ocr_dir = AUDIT / 'ocr-inputs'
    ocr_dir.mkdir(exist_ok=True)
    for index, (path, articles) in enumerate(sorted(image_uses.items())):
        if path.suffix.lower() == '.svg':
            continue  # SVG text has already been inspected by the text scan.
        with Image.open(path) as picture:
            total_frames = getattr(picture, 'n_frames', 1)
            frames = sorted({0, total_frames // 2, total_frames - 1})
            for frame in frames:
                picture.seek(frame)
                rgb = Image.new('RGB', picture.size, 'white')
                rgba = picture.convert('RGBA')
                rgb.paste(rgba, mask=rgba.getchannel('A'))
                if max(rgb.size) > 2400:
                    rgb.thumbnail((2400, 2400))
                if rgb.width < 100 and rgb.height < 100:
                    continue
                target = ocr_dir / f'{index:04d}-{frame:05d}.png'
                rgb.save(target)
                report['ocr_inputs'].append({'input': str(target), 'image': relative(path), 'frame': frame, 'total_frames': total_frames, 'articles': sorted(set(articles))})
    report['unique_article_images'] = len(image_uses)
    report['limits'].append('Images smaller than 100 by 100 pixels are omitted from OCR; SVG content is inspected as text.')
    (AUDIT / 'text-report.json').write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps({'guides': report['guides'], 'text_scan_summary': [{'scope': x['scope'], 'guide': x['guide'], 'text_files': x['text_files_checked'], 'hits': len(x['findings'])} for x in report['text_scans']], 'article_hits': len(report['article_findings']), 'global_search': report['global_search'], 'archive': report['archive'], 'unique_images': len(image_uses), 'ocr_frames': len(report['ocr_inputs']), 'missing_resources': len(report['missing_local_resources'])}, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
