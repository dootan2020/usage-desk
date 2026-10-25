"""Validate static release content, assets, privacy boundary and link metadata."""
import argparse
import gzip
import json
import os
import re
import shutil
import tempfile
import urllib.request
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids, self.fragments, self.assets = [], [], []
    def handle_starttag(self, tag, pairs):
        attrs = dict(pairs)
        if 'id' in attrs: self.ids.append(attrs['id'])
        if tag == 'a' and attrs.get('href', '').startswith('#'): self.fragments.append(attrs['href'][1:])
        if tag == 'script': self.assets.append(attrs['src'])
        if tag == 'img':
            assert 'alt' in attrs, 'Image lacks alt attribute'
            self.assets.append(attrs['src'])
        if tag == 'link' and attrs.get('rel') in ('stylesheet', 'icon'): self.assets.append(attrs['href'])
        if attrs.get('target') == '_blank': assert {'noopener', 'noreferrer'} <= set(attrs.get('rel', '').split()), 'Unsafe new-tab link'

def validate(root):
    html = (root / 'index.html').read_text(encoding='utf-8')
    page = Page(); page.feed(html)
    assert len(page.ids) == len(set(page.ids)), 'Duplicate HTML ID'
    assert set(page.fragments) <= set(page.ids), 'Broken navigation target'
    assert all((root / asset).is_file() for asset in page.assets), 'Missing local page asset'
    assert 'Released 25 Oct 2026' in html, 'Release date is not visible'
    assert 'v1.0.1-rc.17/UsageDeskSetup-1.0.1-rc.17-x64.exe' in html, 'Wrong release link'
    assert 'unsigned' in html.lower() and 'no account data' in html, 'Missing product disclosure'
    assert "connect-src 'none'" in html and 'Content-Security-Policy' in (root / '_headers').read_text(), 'Missing CSP'
    text = '\n'.join(p.read_text(encoding='utf-8') for p in root.rglob('*') if p.is_file() and p.suffix != '.png')
    secrets = re.compile(r'\bsk-ant-[A-Za-z0-9_-]{20,}|\bsk-(?:proj-)?[A-Za-z0-9]{20,}|\bgh[pousr]_[A-Za-z0-9]{36}|\bgithub_pat_[A-Za-z0-9_]{22,}|-----BEGIN [A-Z ]*PRIVATE KEY')
    assert not secrets.search(text), 'Secret-shaped content detected; value omitted'
    assert not any(s in text for s in ('127.0.0.1:17864', '195.87', '22,483.07', 'C:/Users/Admin')), 'Private data or local collector URL included'
    js = (root / 'app.js').read_text()
    assert not re.search(r'innerHTML|\beval\s*\(|new Function|\bfetch\s*\(', js), 'Unexpected dynamic content/network execution'
    size = sum(p.stat().st_size for p in root.rglob('*') if p.is_file())
    assert size < 1_000_000 and len(gzip.compress(js.encode())) < 150_000, 'Page weight budget exceeded'
    print(f'Landing passed: {size} bytes; local assets, navigation, privacy and security checks valid.')

def online():
    manifest = json.loads((ROOT / 'docs/release-manifest.json').read_text())
    headers = {'User-Agent': 'UsageDesk-release-check'}
    if os.environ.get('GITHUB_TOKEN'): headers['Authorization'] = 'Bearer ' + os.environ['GITHUB_TOKEN']
    request = urllib.request.Request('https://api.github.com/repos/dootan2020/usage-desk/releases/tags/v1.0.1-rc.17', headers=headers)
    with urllib.request.urlopen(request, timeout=45) as response: release = json.load(response)
    assert release['prerelease'] and not release['draft'], 'Release must remain a public prerelease'
    assets = {a['name']: a for a in release['assets']}
    assert assets[manifest['installer']]['size'] == manifest['size_bytes'], 'Published installer size mismatch'
    assert {'SHA256SUMS.txt', 'GETTING-STARTED.md', 'UsageDeskCleanWindows-1.0.1-rc.17.zip'} <= set(assets), 'Release asset missing'
    print('Public release metadata verified independently; no private API required by landing.')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--online', action='store_true')
    parser.add_argument('--self-test', action='store_true')
    args = parser.parse_args()
    validate(ROOT / 'landing')
    if args.self_test:
        with tempfile.TemporaryDirectory(prefix='usage-landing-check-') as temporary:
            fixture = Path(temporary) / 'landing'
            shutil.copytree(ROOT / 'landing', fixture)
            (fixture / 'assets/usage-desk.svg').unlink()
            try: validate(fixture)
            except AssertionError as error: print(f'Expected red case detected: {error}')
            else: raise AssertionError('Missing-asset test did not fail')
    if args.online: online()
