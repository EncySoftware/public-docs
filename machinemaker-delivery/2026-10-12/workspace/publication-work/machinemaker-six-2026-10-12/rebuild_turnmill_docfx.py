"""Rebuild the converted English book and validate its original article text and resources."""
from collections import Counter
from pathlib import Path
import hashlib
import json
import sys

import build_collection

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT.parent / "audit-2026-10-08/tools/python"))
from bs4 import BeautifulSoup

guides = json.loads((ROOT / "guides.json").read_text(encoding="utf-8"))
guide = next(g for g in guides if g["key"] == "turnmill-en")
guide = build_collection.build(guide)
report_path = ROOT / "admin/turnmill-en-docfx-conversion.json"
report = json.loads(report_path.read_text(encoding="utf-8"))
for page in report["pages"]:
    path = ROOT / "html/turnmill/en" / page["file"]
    soup = BeautifulSoup(path.read_text(encoding="utf-8-sig"), "html.parser")
    content = soup.select_one("#main-content")
    text = " ".join(content.get_text(" ", strip=True).split())
    assert hashlib.sha256(text.encode("utf-8")).hexdigest() == page["body_sha256"], page["file"]
    assert [i.get("src") for i in content.select("img")] == page["image_sources"], page["file"]
    assert Counter(a.get("href") for a in content.select("a[href]") if a.get_text(strip=True)) == Counter(page["links"]), page["file"]
    page["rendered_sha256"] = hashlib.sha256(path.read_bytes()).hexdigest()
for relative, expected in report["resources"].items():
    assert hashlib.sha256((ROOT / "html/turnmill/en" / relative).read_bytes()).hexdigest() == expected["sha256"], relative
report["build_warnings"] = guide["warnings"]
report["build_errors"] = guide["errors"]
report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
(ROOT / "guides.json").write_text(json.dumps(guides, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
inputs_path = ROOT / "admin/inputs.json"
inputs = json.loads(inputs_path.read_text(encoding="utf-8"))
inputs["guides"] = guides
inputs_path.write_text(json.dumps(inputs, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("Converted text, links, image references and resource hashes verified after rebuild.")
