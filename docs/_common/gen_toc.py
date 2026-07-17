#!/usr/bin/env python3
"""Generate a unit's PDF table of contents from its HTML one.

Single source of truth is the HTML nav `<unit>/src/toc.yml` (standard docfx TOC,
hrefs relative to `src/`). This produces the PDF spine `<unit>/pdf/toc.yml`
(`pdf: true`, the same tree, hrefs re-pointed to `../src/...`) so both output
representations come from one tree.

Usage: python gen_toc.py <unit_dir> [<unit_dir> ...]
"""
import os
import posixpath
import sys


def gen(unit):
    src = os.path.join(unit, "src", "toc.yml")
    if not os.path.isfile(src):
        raise SystemExit("no src/toc.yml in " + unit)
    with open(src, encoding="utf-8-sig") as f:
        lines = f.read().splitlines()

    out = ["pdf: true", "items:"]
    for ln in lines:
        if not ln.strip():
            out.append("")
            continue
        i = ln.find("href:")
        if i != -1:
            href = ln[i + 5:].strip()
            # src/toc.yml hrefs are relative to src/; the PDF toc lives in pdf/
            # (sibling of src/), so re-base and normalize (keeps embedded entries
            # that escape src/, e.g. ../../cldata/..., clean).
            if href and not href.startswith(("http:", "https:", "#")):
                href = posixpath.normpath(posixpath.join("../src", href))
            out.append("  " + ln[:i + 5] + " " + href)
        else:
            out.append("  " + ln)

    pdfdir = os.path.join(unit, "pdf")
    os.makedirs(pdfdir, exist_ok=True)
    dst = os.path.join(pdfdir, "toc.yml")
    with open(dst, "w", encoding="utf-8-sig", newline="\r\n") as f:
        f.write("\n".join(out) + "\n")
    print("wrote", dst)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)
    for u in sys.argv[1:]:
        gen(u)
