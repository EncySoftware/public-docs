#!/usr/bin/env python3
"""Build the HTML or PDF representation of a documentation unit with docfx.

A "unit" is a self-contained documentation subsystem laid out as:
    <unit>/docfx.json         HTML build config      -> <unit>/out/html/index.html
    <unit>/pdf_docfx.json     PDF build config       -> <unit>/out/pdf/<name>.pdf
    <unit>/src/               content (md, images/, attachments/) + src/toc.yml
    <unit>/pdf/toc.yml        PDF spine (generated from src/toc.yml by gen_toc.py)

Usage:
    python build.py <unit_dir> html [--open]
    python build.py <unit_dir> pdf  [--name NAME.pdf]

The per-unit build/generateHTML.cmd / build/generatePDF.cmd scripts are thin
wrappers around this shared entry point.
"""
import argparse
import os
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def _docfx():
    return shutil.which("docfx") or shutil.which("docfx.exe") or "docfx"


def _run(args, cwd):
    print("+", " ".join(str(a) for a in args))
    subprocess.check_call(args, cwd=cwd)


def build_html(unit, open_after):
    _run([_docfx(), "build", "docfx.json"], unit)
    # Home is src/index.html (content lives under src/); fall back to the root.
    index = os.path.join(unit, "out", "html", "src", "index.html")
    if not os.path.isfile(index):
        index = os.path.join(unit, "out", "html", "index.html")
    print("HTML:", index)
    if open_after and os.path.isfile(index) and hasattr(os, "startfile"):
        os.startfile(index)


def build_pdf(unit, name):
    _run([sys.executable, os.path.join(HERE, "gen_toc.py"), unit], HERE)
    _run([_docfx(), "build", "pdf_docfx.json"], unit)
    _run([_docfx(), "pdf", "pdf_docfx.json"], unit)
    produced = os.path.join(unit, "out", "pdf", "pdf", "toc.pdf")
    name = name or ("CAM-" + os.path.basename(os.path.normpath(unit)) + ".pdf")
    dest = os.path.join(unit, "out", "pdf", name)
    shutil.copyfile(produced, dest)
    print("PDF:", dest)


def main():
    ap = argparse.ArgumentParser(description="Build a documentation unit.")
    ap.add_argument("unit", help="path to the unit directory")
    ap.add_argument("target", choices=["html", "pdf"])
    ap.add_argument("--name", help="output PDF file name (pdf target)")
    ap.add_argument("--open", action="store_true", help="open the HTML after building")
    a = ap.parse_args()
    unit = os.path.abspath(a.unit)
    if a.target == "html":
        build_html(unit, a.open)
    else:
        build_pdf(unit, a.name)


if __name__ == "__main__":
    main()
