"""Save the reviewed six-manual sources in local feature branches of the existing public-docs repos."""
from datetime import datetime, timezone
from pathlib import Path
import argparse
import hashlib
import json
import shutil
import subprocess

WORKSPACE = Path(__file__).resolve().parent.parent
PUBLICATION = WORKSPACE / "publication-work"
COLLECTION = PUBLICATION / "machinemaker-six-2026-10-12"
CHECKOUTS = PUBLICATION / "machinemaker-commit-2026-10-12"
GIT = PUBLICATION / "audit-2026-10-08/tools/git/cmd/git.exe"
SNAPSHOT = Path("machinemaker-delivery/2026-10-12")


def git(repo, *args):
    result = subprocess.run([str(GIT), "-C", str(repo), *args], capture_output=True, text=True, encoding="utf-8", errors="replace")
    if result.returncode:
        raise RuntimeError("Git " + args[0] + " failed: " + result.stderr[:1500])
    return result.stdout.strip()


def checksums(path):
    size = path.stat().st_size
    sha256 = hashlib.sha256()
    blob = hashlib.sha1(b"blob " + str(size).encode("ascii") + b"\0")
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(2 * 1024 * 1024), b""):
            sha256.update(block)
            blob.update(block)
    return {"bytes": size, "sha256": sha256.hexdigest(), "git_blob": blob.hexdigest()}


def copy_source(source, target):
    shutil.copytree(source, target, ignore=shutil.ignore_patterns(".git", "obj", "out", "build", "__pycache__", "*.pyc"))


def stage_snapshot(repo, target, language, selected):
    files = []
    for path in sorted(target.rglob("*")):
        if path.is_file() and path.name != "snapshot-manifest.json":
            files.append({"path": path.relative_to(target).as_posix(), **checksums(path)})
    (target / "snapshot-manifest.json").write_text(json.dumps({"saved_at": datetime.now(timezone.utc).isoformat(), "language": language,
        "pages": sum(g["pages"] for g in selected), "files": files}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    git(repo, "add", "--", SNAPSHOT.as_posix())
    # NUL-delimited paths preserve Unicode image names without Git's display quoting.
    staged = git(repo, "ls-files", "--stage", "-z", "--", SNAPSHOT.as_posix())
    blobs = {line.split("\t", 1)[1]: line.split()[1] for line in staged.split("\0") if line}
    for item in files:
        if blobs.get((SNAPSHOT / item["path"]).as_posix()) != item["git_blob"]:
            raise RuntimeError("Staged bytes differ from the copied snapshot: " + item["path"])
    print(language.upper(), git(repo, "branch", "--show-current"), len(files) + 1, "staged files;", sum(g["pages"] for g in selected), "articles; staged source bytes verified", flush=True)
    print(git(repo, "diff", "--cached", "--shortstat"), flush=True)


def prepare():
    guides = json.loads((COLLECTION / "guides.json").read_text(encoding="utf-8"))
    summary = json.loads((COLLECTION / "admin/summary.json").read_text(encoding="utf-8"))
    delivery = json.loads((COLLECTION / "delivery-checks.json").read_text(encoding="utf-8"))
    if summary["page_count"] != 208 or summary["internal_errors"] or summary["browser_errors"] or not delivery["archive_crc_ok"]:
        raise RuntimeError("The delivery must pass its checks before it can be committed")
    for language, version, family in [("en", "v3", "ency-docs"), ("ru", "v20", "sprutcam-docs")]:
        repo = CHECKOUTS / language
        target = repo / SNAPSHOT
        branch = version + "/features/machinemaker-six-2026-10-12"
        selected = [g for g in guides if g["language"] == language]
        if target.exists():
            if git(repo, "branch", "--show-current") != branch or not (target / "snapshot-manifest.json").exists():
                raise RuntimeError("An unrelated snapshot directory already exists: " + str(target))
            if language == "en":
                shutil.copy2(PUBLICATION / "commit_machinemaker_snapshot.py", target / "workspace/publication-work/commit_machinemaker_snapshot.py")
            stage_snapshot(repo, target, language, selected)
            continue
        if git(repo, "status", "--porcelain"):
            raise RuntimeError("The isolated checkout is not empty: " + str(repo))
        git(repo, "switch", "-c", branch)
        old_gitdir = WORKSPACE / "documenti i public gerrit/Hybrid kniga/publication-work" / family / ".git/worktrees" / family
        for key in ["user.name", "user.email"]:
            result = subprocess.run([str(GIT), "--git-dir=" + str(old_gitdir), "config", "--get", key], capture_output=True, text=True, encoding="utf-8")
            if result.returncode or not result.stdout.strip():
                raise RuntimeError("The existing repository has no configured " + key)
            git(repo, "config", key, result.stdout.strip())
        target.mkdir(parents=True)
        for guide in selected:
            copy_source(COLLECTION / "build-work" / guide["key"], target / "source" / guide["kind"])
        # Keep exactly the bytes that were compiled and verified, including legacy HTML-in-Markdown.
        (target / ".gitattributes").write_text("# Reviewed source snapshot: preserve original bytes and SHA256 values.\n* -text\n", encoding="utf-8")
        (target / ".gitignore").write_text("**/obj/\n**/out/\n**/__pycache__/\n*.pyc\n/generated/\nMachineMaker-six-manuals-*.zip\n", encoding="utf-8")
        verification = target / "verification"
        verification.mkdir()
        for name in ["summary.json", "internal-checks.json", "browser-checks.json", "revision-browser-checks.json", "external-checks.json",
                     "content-changes.json", "localized-resources.json", "turnmill-en-docfx-conversion.json", "files-sha256.json", "ADMIN-HANDOFF-RU.md"]:
            shutil.copy2(COLLECTION / "admin" / name, verification / name)
        for guide in selected:
            shutil.copy2(COLLECTION / "admin" / (guide["key"] + "-build.log"), verification / (guide["key"] + "-build.log"))
        shutil.copy2(COLLECTION / "delivery-checks.json", verification / "delivery-checks.json")
        shutil.copy2(COLLECTION / "MachineMaker-six-manuals-2026-10-12.zip.sha256", verification / "delivery.zip.sha256")
        portable_guides = []
        for guide in selected:
            item = dict(guide)
            suffix = "docs/machinemaker/machines" if guide["kind"] == "milling" else "main"
            item["source"] = "source/" + guide["kind"] + "/" + suffix
            portable_guides.append(item)
        (target / "guides.json").write_text(json.dumps(portable_guides, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        if language == "en":
            # Shared delivery resources are canonical in the English repo, as in the previous publication.
            copy_source(COLLECTION / "html/_shared", target / "shared-resources")
            saved_workspace = target / "workspace"
            saved_workspace.mkdir()
            for name in ["AGENTS.md", "MachineMaker-session-handoff.md", "MachineMaker-progress-2026-10-09.md", "MachineMaker-progress-2026-10-12.md"]:
                shutil.copy2(WORKSPACE / name, saved_workspace / name)
            saved_publication = saved_workspace / "publication-work"
            saved_publication.mkdir()
            for name in ["prepare_six_rebuild_2026_10_12.py", "commit_machinemaker_snapshot.py"]:
                shutil.copy2(PUBLICATION / name, saved_publication / name)
            assembly = saved_publication / COLLECTION.name
            assembly.mkdir()
            for script in COLLECTION.glob("*.py"):
                shutil.copy2(script, assembly / script.name)
            review = saved_publication / "local-machinemaker-review"
            review.mkdir()
            for name in ["serve.py", "start.ps1", "make_index.py"]:
                shutil.copy2(PUBLICATION / "local-machinemaker-review" / name, review / name)
        readme = f"""# Reviewed MachineMaker source snapshot — 2026-10-12 ({language.upper()})

This snapshot preserves the reviewed local DocFX sources in the existing public-docs repository.
It is separate from the portal's docs/ tree, whose moved guide sections were removed upstream.

## Manuals

""" + "\n".join(f"- {g['label']}: {g['pages']} articles, project `{g['source']}/docfx.json`." for g in portable_guides) + f"""

The two language snapshots together contain six manuals and 208 articles. English TurnMilling
uses the shared DocFX template, retains the original numeric article URLs and excludes Trevisan.
The obsolete KB referrals and restricted Custom Imported Robot Cell video link were removed.
The user confirmed the legacy v16 examples; the KUKA link was retained.

## Build and evidence

Use DocFX 2.78.2 and .NET to build an individual project at the path listed above, writing output
outside source/. The project files and referenced binary resources are retained as verified.
Some Milling source links use the previously published shared resource URLs; the English snapshot
contains the canonical shared-resources/ cache used to localize them in the complete delivery.

verification/ records the complete six-book delivery checks, original source provenance,
article/resource hashes, and the delivery archive checksum. The generated HTML and 1.07 GB
delivery ZIP remain in the local workspace and are not duplicated in Git.

The English snapshot also archives the session notes and scripts at their original relative paths
under workspace/. Those scripts document the original local workspace layout; they are not a new
deployment pipeline. Each source project can be built independently using its own docfx.json.

The previous local checks passed: 208 article/link checks, 416 browser page checks, all six book
searches and shared search, original English article-text/resource comparisons, and ZIP CRC.
The full delivery archive SHA256 is `{delivery['package_sha256']}`.

This feature branch records local commits only. Publication routes and CI integration are a
separate administrator step. No stable or develop branch is changed by this snapshot commit.
"""
        (target / "README.md").write_text(readme, encoding="utf-8")
        stage_snapshot(repo, target, language, selected)


def commit():
    results = {}
    for language in ["en", "ru"]:
        repo = CHECKOUTS / language
        title = "Save reviewed MachineMaker " + language.upper() + " sources and delivery snapshot"
        git(repo, "commit", "-m", title, "-m", "Preserve the three reviewed DocFX manuals for this language, their resources and validation evidence. Record the October 12 link corrections and original English TurnMilling migration without Trevisan. Keep the snapshot separate from the portal sections moved upstream.")
        if git(repo, "status", "--porcelain"):
            raise RuntimeError("The committed checkout is not clean: " + language)
        results[language] = {"path": str(repo), "branch": git(repo, "branch", "--show-current"),
                             "commit": git(repo, "rev-parse", "HEAD"), "pushed": False}
        print(language.upper(), results[language]["commit"], results[language]["branch"], "clean", flush=True)
    (CHECKOUTS / "commits.json").write_text(json.dumps(results, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("action", choices=["prepare", "commit"])
    args = parser.parse_args()
    prepare() if args.action == "prepare" else commit()
