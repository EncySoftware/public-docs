"""Upload the reviewed package to a draft GitHub release using saved Git credentials."""
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import quote, urlsplit
import hashlib
import http.client
import json
import os
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
PUBLICATION = HERE.parent
GIT = PUBLICATION / 'audit-2026-10-08/tools/git/cmd/git.exe'
COLLECTION = PUBLICATION / 'machinemaker-six-2026-10-12'
REPOSITORY = '/repos/EncySoftware/public-docs'
TAG = 'machinemaker-six-manuals-2026-10-12'
sys.path.insert(0, str(PUBLICATION))
from hosting import api


def saved_credential():
    env = os.environ.copy()
    env.update(GIT_TERMINAL_PROMPT='0', GCM_INTERACTIVE='Never')
    result = subprocess.run([str(GIT), '-C', str(HERE / 'en'), 'credential', 'fill'], input='protocol=https\nhost=github.com\n\n', capture_output=True, text=True, encoding='utf-8', env=env, timeout=30)
    if result.returncode:
        raise RuntimeError('No saved GitHub credential is available.')
    values = dict(line.split('=', 1) for line in result.stdout.splitlines() if '=' in line)
    return values['password']


def sha256(path):
    value = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(2 * 1024 * 1024), b''):
            value.update(block)
    return value.hexdigest()


def safe_asset(asset):
    return {key: asset.get(key) for key in ('id', 'name', 'state', 'size', 'digest', 'browser_download_url')}


def upload_file(release, path, token):
    expected_size = path.stat().st_size
    expected_digest = 'sha256:' + sha256(path)
    assets = api('github', REPOSITORY + '/releases/' + str(release['id']) + '/assets?per_page=100', token=token)
    existing = next((item for item in assets if item['name'] == path.name), None)
    if existing:
        if existing['size'] == expected_size and existing.get('digest') == expected_digest and existing.get('state') == 'uploaded':
            print('Already verified:', path.name, flush=True)
            return safe_asset(existing)
        if existing.get('state') == 'starter' and existing.get('size', 0) == 0:
            api('github', REPOSITORY + '/releases/assets/' + str(existing['id']), 'DELETE', token=token)
        else:
            raise RuntimeError('An existing release asset differs from the reviewed local file: ' + path.name)
    parsed = urlsplit(release['upload_url'].split('{', 1)[0])
    assert parsed.scheme == 'https' and parsed.hostname == 'uploads.github.com'
    connection = http.client.HTTPSConnection(parsed.hostname, timeout=180)
    try:
        connection.putrequest('POST', parsed.path + '?name=' + quote(path.name))
        connection.putheader('Authorization', 'Bearer ' + token)
        connection.putheader('User-Agent', 'MachineMaker-reviewed-delivery')
        connection.putheader('Accept', 'application/vnd.github+json')
        connection.putheader('Content-Type', 'application/octet-stream')
        connection.putheader('Content-Length', str(expected_size))
        connection.endheaders()
        sent = 0
        checkpoint = 0
        started = time.monotonic()
        with path.open('rb') as stream:
            for block in iter(lambda: stream.read(1024 * 1024), b''):
                connection.send(block)
                sent += len(block)
                if sent - checkpoint >= 64 * 1024 * 1024:
                    print('UPLOAD', path.name, round(sent / expected_size * 100, 1), '%;', round(sent / 1024 / 1024), 'MiB;', round(sent / 1024 / 1024 / max(time.monotonic() - started, 0.001), 1), 'MiB/s', flush=True)
                    checkpoint = sent
        response = connection.getresponse()
        body = response.read()
        if response.status != 201:
            raise RuntimeError('GitHub upload returned HTTP ' + str(response.status) + ' for ' + path.name)
        uploaded = json.loads(body)
    finally:
        connection.close()
    assert uploaded['size'] == expected_size
    assert uploaded.get('state') == 'uploaded'
    if uploaded.get('digest') is None:
        uploaded = api('github', REPOSITORY + '/releases/assets/' + str(uploaded['id']), token=token)
    assert uploaded.get('digest') == expected_digest, 'Remote asset SHA256 does not match local file.'
    print('Uploaded and SHA256 verified:', path.name, flush=True)
    return safe_asset(uploaded)


def main():
    commits = json.loads((HERE / 'commits.json').read_text(encoding='utf-8-sig'))
    assert all(item['pushed'] for item in commits.values()), 'Push both reviewed branches first.'
    delivery = json.loads((COLLECTION / 'delivery-checks.json').read_text(encoding='utf-8'))
    package = COLLECTION / 'MachineMaker-six-manuals-2026-10-12.zip'
    assert package.stat().st_size == delivery['package_bytes']
    assert sha256(package) == delivery['package_sha256']
    token = saved_credential()
    releases = api('github', REPOSITORY + '/releases?per_page=100', token=token)
    release = next((item for item in releases if item['tag_name'] == TAG), None)
    if release is None:
        release = api('github', REPOSITORY + '/releases', 'POST', {
            'tag_name': TAG,
            'target_commitish': commits['en']['commit'],
            'name': 'MachineMaker — six reviewed manuals, 2026-10-12',
            'body': 'Reviewed static HTML and administrator handoff: six manuals, 208 pages, in English and Russian. Includes the approved ENCY captions in both Robots EN screenshots. The ZIP contains html/ and admin/ and is ready for the administrator to deploy. This draft release does not publish the documentation website.\n\nZIP SHA256: `' + delivery['package_sha256'] + '`\n\nEN source branch: `' + commits['en']['branch'] + '` at `' + commits['en']['commit'] + '`.\nRU source branch: `' + commits['ru']['branch'] + '` at `' + commits['ru']['commit'] + '`.',
            'draft': True,
            'prerelease': False,
        }, token=token)
    assert release['draft'], 'Do not change a published release through this handoff script.'
    record = {'checked_at': datetime.now(timezone.utc).isoformat(), 'repository': 'EncySoftware/public-docs', 'id': release['id'], 'tag': TAG, 'url': release['html_url'], 'draft': release['draft'], 'package_sha256': delivery['package_sha256'], 'package_bytes': delivery['package_bytes'], 'assets': []}
    status_path = HERE / 'server-delivery.json'
    status_path.write_text(json.dumps(record, ensure_ascii=False, indent=2), encoding='utf-8')
    for path in (package, COLLECTION / (package.name + '.sha256'), COLLECTION / 'admin/ADMIN-HANDOFF-RU.md'):
        record['assets'].append(upload_file(release, path, token))
        record['checked_at'] = datetime.now(timezone.utc).isoformat()
        status_path.write_text(json.dumps(record, ensure_ascii=False, indent=2), encoding='utf-8')
    print('DRAFT RELEASE READY:', release['html_url'], flush=True)
    print('Remote ZIP digest:', next(item['digest'] for item in record['assets'] if item['name'] == package.name), flush=True)


if __name__ == '__main__':
    main()
