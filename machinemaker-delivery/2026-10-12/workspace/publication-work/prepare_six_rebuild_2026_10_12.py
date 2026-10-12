"""Prepare a separate reproducible local six-manual build from the selected snapshots."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import shutil

PUBLICATION = Path(__file__).resolve().parent
PREVIOUS = PUBLICATION / "machinemaker-six-2026-10-09"
TARGET = PUBLICATION / "machinemaker-six-2026-10-12"
if TARGET.exists():
    raise RuntimeError("The rebuild directory already exists; inspect it before continuing")
TARGET.mkdir()
(TARGET / "admin").mkdir()
scripts = ["build_collection.py", "localize_resources.py", "make_portal.py", "revise_links_2026_10_12.py",
           "check_local.py", "check_browser.py", "check_revision_2026_10_12.py", "package_collection.py"]
for name in scripts:
    shutil.copy2(PREVIOUS / name, TARGET / name)
shutil.copytree(PREVIOUS / "build-work", TARGET / "build-work")
revision = json.loads((PREVIOUS / "admin/content-changes.json").read_text(encoding="utf-8"))
restored = []
for item in revision["changes"]:
    if not item["path"].startswith("build-work/"):
        continue
    baseline = PREVIOUS / "admin/revision-baseline-2026-10-09" / item["path"]
    if hashlib.sha256(baseline.read_bytes()).hexdigest() != item["before_sha256"]:
        raise RuntimeError("A selected source baseline differs from the approved record: " + item["path"])
    shutil.copy2(baseline, TARGET / item["path"])
    restored.append(item["path"])
# The two legacy examples are already local and confirmed by the user; do not download them again.
cache = TARGET / "html/_shared/examples/legacy-v16"
cache.mkdir(parents=True)
for path in (PREVIOUS / "html/_shared/examples/legacy-v16").glob("*.zip"):
    shutil.copy2(path, cache / path.name)
# Existing external checks remain dated October 9. Only their current references will be reconciled.
shutil.copy2(PREVIOUS / "admin/external-checks.json", TARGET / "admin/external-checks.json")
package = TARGET / "package_collection.py"
text = package.read_text(encoding="utf-8")
text = text.replace("MachineMaker-six-manuals-2026-10-09.zip", "MachineMaker-six-manuals-2026-10-12.zip")
text = text.replace("E:/astra/video/publication-work/machinemaker-six-2026-10-09/html/", "E:/astra/video/publication-work/machinemaker-six-2026-10-12/html/")
text = text.replace("- 6 руководств, 209 страниц, 418 открытий Chrome на 1440 и 390 px.", "- Полная повторная проверка 12 октября: 6 руководств, 209 страниц, 418 открытий Chrome на 1440 и 390 px.")
package.write_text(text, encoding="utf-8")
report = {"prepared_at": datetime.now(timezone.utc).isoformat(), "previous_delivery": str(PREVIOUS),
          "source_policy": "Same six selected snapshots; no Gerrit update requested or imported",
          "restored_baselines_before_build": restored, "user_corrections": "Apply revise_links_2026_10_12.py after rendering and resource localization",
          "external_check_policy": "Retain original check dates; reconcile references locally"}
(TARGET / "admin/rebuild-provenance.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("Prepared separate local build:", TARGET, flush=True)
