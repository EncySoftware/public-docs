"""Apply the explicitly requested Robots EN screenshot branding replacement."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import shutil

REV = Path(__file__).resolve().parent
WORKSPACE = REV.parent.parent
DELIVERY = WORKSPACE / 'publication-work/machinemaker-six-2026-10-12'
SNAPSHOT = WORKSPACE / 'publication-work/machinemaker-commit-2026-10-12/en/machinemaker-delivery/2026-10-12'
PROJECTS = {'build-source': DELIVERY / 'build-work/robots-en/main', 'git-source': SNAPSHOT / 'source/robots/main'}
HTML = DELIVERY / 'html/robots/en'
GENERATED = Path('C:/Users/xTAGx/.codex/generated_images/01a12f9d-a107-7272-bd54-7dc12d0d1085')
JOBS = [
    ('limits', '3575d6a240d0d00e23009b9abb76f3f16071aebbeeeea8d8bd895f743dad82a5', 'exec-986b32ef-f136-4582-b10b-0e4ed0d9c697.png', 414, 503),
    ('axis-options', '3416680d67cea5b40aefd0fea069ff2eeafcecc7fa47ed5c8231fde19da3ff51', 'exec-dd51ad8b-9a58-43ac-aa9a-f732677b5a2f.png', 692, 501),
]
PROMPT = "Use case: text-localization. Edit target: the supplied existing MachineMaker interface screenshot. Make exactly one text substitution in the checkbox caption near the bottom: replace the word 'SprutCAM' with 'ENCY', so the complete caption reads verbatim 'ENCY axes map compatibility mode'. Match the original small dark-gray UI font, weight, baseline and antialiasing; move the following words left naturally after the shorter brand name. Leave the checkbox in its exact original position. Preserve the entire screenshot, original dimensions and framing, panels, all other text, all numeric values and signs, tabs, controls, colored indicators, existing red annotation if present, background and every other pixel as faithfully as possible. Do not redraw or redesign the interface. Do not add callouts, watermarks, extra text, borders or labels. The only requested visual change is SprutCAM to ENCY in that one caption."


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def backup(path, label):
    target = REV / 'before' / label / path.name
    target.parent.mkdir(parents=True, exist_ok=True)
    assert not target.exists(), 'Revision backup already exists; do not apply twice.'
    shutil.copy2(path, target)


def main():
    assert not (REV / 'revision.json').exists(), 'This revision has already been applied.'
    for root in [*PROJECTS.values(), HTML]:
        for _, old_hash, _, _, _ in JOBS:
            assert digest(root / 'src/assets' / (old_hash + '.png')) == old_hash
    page = HTML / 'src/content/131903495.html'
    backup(page, 'html-page')
    manifest = {'revised_at': datetime.now(timezone.utc).isoformat(), 'authorization': 'User asked to replace SprutCAM with ENCY in both Robots EN screenshots.', 'tool': 'built-in image_gen', 'prompt': PROMPT, 'old_page_sha256': digest(page), 'old_delivery': json.loads((DELIVERY / 'delivery-checks.json').read_text(encoding='utf-8')), 'images': []}
    for name, old_hash, generated_name, width, height in JOBS:
        output = REV / 'images' / (name + '-ency.png')
        output.parent.mkdir(exist_ok=True)
        shutil.copy2(GENERATED / generated_name, output)
        new_hash = digest(output)
        manifest['images'].append({'name': name, 'old_filename': old_hash + '.png', 'old_sha256': old_hash, 'new_filename': new_hash + '.png', 'new_sha256': new_hash, 'generated_copy': str(output), 'rendered_width': width, 'rendered_height': height, 'caption': 'ENCY axes map compatibility mode'})
        for label, root in {**PROJECTS, 'html-assets': HTML}.items():
            assets = root / 'src/assets'
            source = assets / (old_hash + '.png')
            archived = REV / 'before' / label / source.name
            archived.parent.mkdir(parents=True, exist_ok=True)
            assert source.resolve().is_relative_to(root.resolve())
            assert archived.resolve().is_relative_to(REV.resolve())
            assert not archived.exists()
            shutil.copy2(output, assets / (new_hash + '.png'))
            source.replace(archived)  # Preserve originals outside every live source/site tree.
    for label, root in PROJECTS.items():
        source = root / 'src/content/131903495.md'
        backup(source, label + '-page')
        raw = source.read_bytes()
        for item in manifest['images']:
            old = f'![Building a kinematic scheme](../assets/{item["old_filename"]})'.encode()
            new = f'<img src="../assets/{item["new_filename"]}" alt="Building a kinematic scheme" width="{item["rendered_width"]}" style="height:auto">'.encode()
            assert raw.count(old) == 1
            raw = raw.replace(old, new)
        source.write_bytes(raw)
    (REV / 'revision.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding='utf-8')
    (REV / 'prompts.md').write_text('# Image edit prompt\n\nTool: built-in image_gen. Applied separately to each of the two input screenshots.\n\n' + PROMPT + '\n', encoding='utf-8')
    print(json.dumps(manifest['images'], indent=2))


if __name__ == '__main__':
    main()
