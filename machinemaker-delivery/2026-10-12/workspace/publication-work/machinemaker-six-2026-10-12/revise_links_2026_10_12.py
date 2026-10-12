"""Apply the user's October 12 decisions to the local delivery, preserving source snapshots."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import re
import sys

ROOT = Path(__file__).resolve().parent
SITE = ROOT / "html"
ADMIN = ROOT / "admin"
sys.path.insert(0, str(ROOT.parent / "audit-2026-10-08/tools/python"))
from bs4 import BeautifulSoup


def digest(data):
    return hashlib.sha256(data).hexdigest()


def write_json(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


ASSEMBLY = "https://kb.sprutcam.com/display/MMUMAU/Assembly+parameters"
KINEMATIC = "https://kb.sprutcam.com/display/MMUMAU15/Build+kinematic+schema"
CAD = "https://kb.sprutcam.com/display/MMUMAU15/Prepare+and+import+3D+objects"


def revise(text, action):
    if action == "assembly-local":
        pattern = r'<a\s+class="external-link" href="' + re.escape(ASSEMBLY) + r'"> </a>assembly settings panel'
        return re.subn(pattern, ' <a href="assembly-options.html">assembly settings panel</a>', text)
    if action == "assembly-unlink":
        pattern = r'<a\s+class="external-link" href="' + re.escape(ASSEMBLY) + r'"> </a>'
        return re.subn(pattern, " ", text)
    if action == "kinematic-local":
        pattern = r'<a\s+class="external-link" href="' + re.escape(KINEMATIC) + r'">kinematics panel</a>'
        return re.subn(pattern, '<a href="building-a-kinematic-scheme.html">kinematics panel</a>', text)
    if action == "cad-reference-remove":
        pattern = r'<p\b[^>]*>(?:(?!</p>).)*' + re.escape(CAD) + r'(?:(?!</p>).)*</p>'
        return re.subn(pattern, "", text, flags=re.DOTALL)
    if action == "video-remove":
        pattern = r'<li><a href="https://www\.youtube\.com/watch\?v=JHGeWdbgWj0[^\"]*">MachineMaker Custom Imported Robot Cell</a></li>\r?\n?'
        return re.subn(pattern, "", text)
    if action == "video-source-remove":
        return re.subn(r'^5\. \[MachineMaker Custom Imported Robot Cell\]\(https://www\.youtube\.com/watch\?v=JHGeWdbgWj0[^\n]*\)\r?\n?', "", text, flags=re.MULTILINE)
    raise ValueError(action)


def main():
    manifest_path = ADMIN / "content-changes.json"
    if manifest_path.exists():
        raise RuntimeError("This revision has already been applied; inspect content-changes.json instead of applying it again")
    targets = [
        ("html/milling/en/src/toolbar.html", "assembly-local"),
        ("html/milling/en/src/assemblies.html", "kinematic-local"),
        ("html/milling/en/src/grouping-elements-into-nodes.html", "cad-reference-remove"),
        ("html/turnmill/en/6.html", "assembly-unlink"),
        ("html/turnmill/en/14.html", "cad-reference-remove"),
        ("html/robots/en/src/content/129930510.html", "video-remove"),
        ("build-work/milling-en/docs/machinemaker/machines/src/toolbar.md", "assembly-local"),
        ("build-work/milling-en/docs/machinemaker/machines/src/assemblies.md", "kinematic-local"),
        ("build-work/milling-en/docs/machinemaker/machines/src/grouping-elements-into-nodes.md", "cad-reference-remove"),
        ("build-work/robots-en/main/src/content/129930510.md", "video-source-remove"),
    ]
    pending = []
    for relative, action in targets:
        path = ROOT / relative
        before = path.read_bytes()
        after_text, count = revise(before.decode("utf-8"), action)
        if count != 1:
            raise RuntimeError(f"Expected exactly one {action} change in {relative}, found {count}")
        pending.append((path, before, after_text.encode("utf-8"), action))
    # Save exact, reviewable changes before writing the delivery files.
    now = datetime.now(timezone.utc).isoformat()
    changes = []
    for path, before, after, action in pending:
        relative = path.relative_to(ROOT).as_posix()
        changes.append({"path": relative, "action": action, "before_sha256": digest(before), "after_sha256": digest(after)})
        baseline = ADMIN / "revision-baseline-2026-10-09" / relative
        baseline.parent.mkdir(parents=True, exist_ok=True)
        baseline.write_bytes(before)
    manifest = {
        "revised_at": now,
        "authorization": "User decisions of 2026-10-12 in this conversation",
        "changes": changes,
        "decisions": {
            "legacy_kb_links": "Replace with corresponding internal chapters where available; otherwise remove the obsolete referral",
            "restricted_video": "Remove the Custom Imported Robot Cell link and its list entry",
            "legacy_v16_examples": "Compatibility confirmed by the user; retain the archives and links unchanged",
            "kuka_download_center": "Retain the link and instructional text unchanged, as requested by the user",
        },
        "original_source_snapshots_modified": False,
    }
    write_json(manifest_path, manifest)
    for path, before, after, action in pending:
        path.write_bytes(after)

    # Keep the book search and shared search synchronized with the edited article.
    local_index_path = SITE / "robots/en/index.json"
    before = local_index_path.read_bytes()
    index = json.loads(before)
    item = index["src/content/129930510.html"]
    phrase = "MachineMaker Custom Imported Robot Cell"
    if phrase not in item["keywords"]:
        raise RuntimeError("The removed video was not found in the robot search index")
    item["keywords"] = item["keywords"].replace(" " + phrase, "")
    write_json(local_index_path, index)
    changes.append({"path": local_index_path.relative_to(ROOT).as_posix(), "action": "refresh-book-search", "before_sha256": digest(before), "after_sha256": digest(local_index_path.read_bytes())})
    milling_index_path = SITE / "milling/en/index.json"
    before = milling_index_path.read_bytes()
    index = json.loads(before)
    item = index["src/grouping-elements-into-nodes.html"]
    old_sentence = "If MachineMaker can't group elements correctly - see how to fix your CAD models . "
    if old_sentence not in item["keywords"]:
        raise RuntimeError("The removed CAD referral was not found in the milling search index")
    item["keywords"] = item["keywords"].replace(old_sentence, "")
    write_json(milling_index_path, index)
    changes.append({"path": milling_index_path.relative_to(ROOT).as_posix(), "action": "refresh-book-search", "before_sha256": digest(before), "after_sha256": digest(milling_index_path.read_bytes())})
    shared_path = SITE / "search-index.json"
    before = shared_path.read_bytes()
    index = json.loads(before)
    for item in index:
        path = SITE / item["href"]
        if any(change["path"] == "html/" + item["href"] for change in changes):
            soup = BeautifulSoup(path.read_text(encoding="utf-8-sig"), "html.parser")
            article = soup.select_one("article.content") or soup.select_one("#main-content")
            item["text"] = " ".join(article.get_text(" ", strip=True).split())
    shared_path.write_text(json.dumps(index, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    changes.append({"path": "html/search-index.json", "action": "refresh-shared-search", "before_sha256": digest(before), "after_sha256": digest(shared_path.read_bytes())})
    write_json(manifest_path, manifest)

    resources_path = ADMIN / "localized-resources.json"
    resources = json.loads(resources_path.read_text(encoding="utf-8"))
    for item in resources["resources"].values():
        if item.get("kind") == "legacy":
            item["legacy_version_compatibility_confirmed"] = True
            item["compatibility_confirmation"] = {"by": "user", "date": "2026-10-12", "method": "User confirmation; no new application test performed"}
    write_json(resources_path, resources)
    print("Revised 6 delivery articles, 4 isolated source copies and 2 search indexes; source snapshots preserved.")


if __name__ == "__main__":
    main()
