"""Check English manual links without changing manuals or retaining signed URLs."""
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError
from urllib.parse import parse_qs, unquote, urlencode, urlsplit, urlunsplit
from urllib.request import HTTPRedirectHandler, Request, build_opener
import html
import json
import re
import sys

from audit import AUDIT, SITE, SNAPSHOT, BeautifulSoup, PATTERN, normalize, relative

references = {}
internal = []
brand_urls = []
other_schemes = []


def safe_url(value):
    parts = urlsplit(value)
    video_id = parse_qs(parts.query).get('v', [''])[0] if parts.hostname and parts.hostname.endswith('youtube.com') else ''
    return urlunsplit((parts.scheme, parts.netloc, parts.path, urlencode({'v': video_id}) if video_id else '', ''))


def add(path, raw, scope, kind):
    raw = html.unescape(raw).strip()
    if not raw:
        return
    location = {'path': relative(path), 'scope': scope, 'kind': kind}
    if PATTERN.search(normalize(raw)):
        brand_urls.append({'url': safe_url(raw), **location})
    parts = urlsplit(raw)
    if parts.scheme in {'http', 'https'} or parts.netloc:
        address = 'https:' + raw if raw.startswith('//') else raw
        references.setdefault(address, []).append(location)
    elif parts.scheme:
        other_schemes.append({'scheme': parts.scheme, **location})
    elif scope == 'built_html':
        internal.append({'raw': raw, **location})


def collect_html(path, scope):
    text = path.read_text(encoding='utf-8-sig')
    soup = BeautifulSoup(text, 'html.parser')
    for tag in soup.find_all(True):
        for attr in ('href', 'src', 'poster', 'data-src', 'data-href'):
            if tag.get(attr):
                add(path, tag[attr], scope, f'{tag.name}.{attr}')
        if tag.get('srcset'):
            for candidate in tag['srcset'].split(','):
                add(path, candidate.strip().split()[0], scope, f'{tag.name}.srcset')
        if tag.get('style'):
            for raw in re.findall(r'url\([\s\'"]*([^\)\'\"]+)', tag['style']):
                add(path, raw, scope, 'inline-css')
    if path.suffix.lower() == '.md':
        for raw in re.findall(r'\]\((https?://[^\s\)]+)', text):
            add(path, raw, scope, 'markdown-link')


def collect_json_links(path, value):
    if isinstance(value, dict):
        for key, item in value.items():
            if key in {'href', 'topicHref', 'tocHref', 'homepage', 'pdf'} and isinstance(item, str):
                add(path, item, 'built_html', 'json.' + key)
            else:
                collect_json_links(path, item)
    elif isinstance(value, list):
        for item in value:
            collect_json_links(path, item)


for kind in ('milling', 'robots', 'turnmill'):
    root = SITE / kind / 'en'
    for path in root.rglob('*.html'):
        collect_html(path, 'built_html')
    for path in root.rglob('*.css'):
        text = path.read_text(encoding='utf-8-sig')
        for raw in re.findall(r'url\([\s\'"]*([^\)\'\"]+)', text):
            add(path, raw, 'built_html', 'css-url')
    for path in root.rglob('*.json'):
        data = json.loads(path.read_text(encoding='utf-8-sig'))
        collect_json_links(path, data)
        if path.name == 'index.json' and isinstance(data, dict):
            for name in data:
                add(path, name, 'built_html', 'json.search-index-key')
    for path in (SNAPSHOT / 'source' / kind).rglob('*.md'):
        collect_html(path, 'committed_source')

for row in json.loads((SITE / 'search-index.json').read_text(encoding='utf-8-sig')):
    if row.get('language') == 'en':
        add(SITE / 'search-index.json', row['href'], 'built_html', 'shared-search')

errors = []
soups = {}
file_map = {relative(p).casefold(): relative(p) for p in SITE.rglob('*') if p.is_file()}
for item in internal:
    path = AUDIT.parent.parent / item['path']
    parts = urlsplit(item['raw'])
    target = (path.parent / unquote(parts.path)).resolve() if parts.path else path.resolve()
    if target.is_dir():
        target = target / 'index.html'
    if not target.is_relative_to(SITE.resolve()) or not target.is_file():
        errors.append({'error': 'missing-local-target', **item})
        continue
    spelling = relative(target)
    if file_map.get(spelling.casefold()) != spelling:
        errors.append({'error': 'path-case-mismatch', 'actual': file_map.get(spelling.casefold()), **item})
    if parts.fragment and unquote(parts.fragment).casefold() != 'top' and target.suffix.lower() == '.html':
        if target not in soups:
            soups[target] = BeautifulSoup(target.read_text(encoding='utf-8-sig'), 'html.parser')
        fragment = unquote(parts.fragment)
        if not soups[target].find(id=fragment) and not soups[target].find(attrs={'name': fragment}):
            errors.append({'error': 'missing-anchor', **item})


class TrackRedirect(HTTPRedirectHandler):
    def __init__(self):
        super().__init__()
        self.hops = []

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        self.hops.append({'status': code, 'to': safe_url(newurl)})
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def fetch(address, limit=200000):
    redirect = TrackRedirect()
    headers = {'User-Agent': 'Mozilla/5.0 MachineMaker English documentation link review'}
    if urlsplit(address).path.lower().endswith(('.zip', '.rar')):
        headers['Range'] = 'bytes=0-1023'
        limit = 1024
    result = {'url': safe_url(address), 'status': None, 'redirects': redirect.hops}
    try:
        with build_opener(redirect).open(Request(address, headers=headers), timeout=18) as response:
            result.update(status=response.status, final_url=safe_url(response.url), content_type=response.headers.get('Content-Type', ''))
            body = response.read(limit)
    except HTTPError as error:
        result.update(status=error.code, final_url=safe_url(error.url))
        body = b''
    except Exception as error:
        result['error_type'] = type(error).__name__
        body = b''
    return result, body


def check(address):
    youtube = urlsplit(address).hostname == 'www.youtube.com'
    result, body = fetch(address, 3000000 if youtube else 200000)
    result['references'] = references[address]
    text = body.decode('utf-8', errors='replace')
    title = re.search(r'<title[^>]*>(.*?)</title>', text, re.I | re.S)
    if title:
        result['title'] = html.unescape(re.sub(r'\s+', ' ', title.group(1)).strip())
    if youtube:
        video_id = parse_qs(urlsplit(address).query).get('v', [''])[0]
        meta, raw = fetch('https://www.youtube.com/oembed?' + urlencode({'url': 'https://www.youtube.com/watch?v=' + video_id, 'format': 'json'}))
        result['video_metadata_status'] = meta['status']
        if meta['status'] == 200:
            metadata = json.loads(raw)
            result['video_title'] = metadata.get('title')
            result['video_author'] = metadata.get('author_name')
        match = re.search(r'ytInitialPlayerResponse\s*=\s*', text)
        if match:
            try:
                player, _ = json.JSONDecoder().raw_decode(text[match.end():])
                state = player.get('playabilityStatus', {})
                result['playability_status'] = state.get('status')
                result['playability_reason'] = state.get('reason')
            except ValueError:
                pass
    brand_values = {key: value for key, value in result.items() if key in ('url', 'final_url', 'title', 'video_title', 'video_author') and isinstance(value, str) and PATTERN.search(normalize(value))}
    if brand_values:
        result['brand_findings'] = brand_values
    result['redirect_brand_findings'] = [hop for hop in result['redirects'] if PATTERN.search(normalize(hop['to']))]
    print(urlsplit(address).hostname, result['status'], result.get('video_metadata_status', ''), flush=True)
    return result


checked_at = datetime.now(timezone.utc).isoformat()
external_checked_at = checked_at
if '--reuse-external' in sys.argv:
    previous = json.loads((AUDIT / 'links-report.json').read_text(encoding='utf-8'))
    results = previous['external_results']
    assert {safe_url(address) for address in references} == {row['url'] for row in results}, 'External URL inventory changed; run without --reuse-external.'
    external_checked_at = previous.get('external_checked_at_utc', previous['checked_at_utc'])
else:
    results = []
    with ThreadPoolExecutor(max_workers=8) as executor:
        pending = [executor.submit(check, address) for address in sorted(references)]
        for task in as_completed(pending):
            results.append(task.result())
report = {'checked_at_utc': checked_at, 'external_checked_at_utc': external_checked_at, 'internal_references_checked': len(internal), 'internal_errors': errors, 'brand_url_references': brand_urls, 'external_unique_urls': len(references), 'external_built_urls': sum(any(r['scope'] == 'built_html' for r in uses) for uses in references.values()), 'external_source_only_urls': sum(not any(r['scope'] == 'built_html' for r in uses) for uses in references.values()), 'external_results': sorted(results, key=lambda row: row['url']), 'other_schemes': other_schemes, 'limits': ['Built English HTML links, resource attributes, CSS URLs, per-book navigation/search JSON and shared search entries are checked locally, including fragments and case-sensitive spelling.', 'All external addresses from those files and committed English Markdown are fetched with redirects followed. Query strings from remote responses are discarded; only public YouTube video IDs are retained.', 'Source-only addresses are reported separately from active delivered links.', 'Video metadata and player status are inspected; full video playback and downloadable binary project contents are outside this check.']}
(AUDIT / 'links-report.json').write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps({'internal_checked': len(internal), 'internal_errors': errors, 'external_unique': len(references), 'external_failed': [{'url': r['url'], 'status': r['status']} for r in results if not r['status'] or r['status'] >= 400], 'brand_external': [{'url': r['url'], 'findings': r.get('brand_findings')} for r in results if r.get('brand_findings') or r.get('redirect_brand_findings')]}, ensure_ascii=False, indent=2))
