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


def _redirect_html(rel):
    return (
        '<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">'
        '<meta http-equiv="refresh" content="0; url=./%s">'
        '<link rel="canonical" href="./%s"><title>Documentation</title>'
        '</head><body><a href="./%s">Open the documentation</a></body></html>\n'
        % (rel, rel, rel)
    )


def _find_home(out_html):
    """The home is the built src/index.html. Simple units put it at src/index.html;
    posts units (built from the posts root to resolve the shared cldata links) put
    it one level deeper, e.g. sppx/src/index.html."""
    direct = os.path.join(out_html, "src", "index.html")
    if os.path.isfile(direct):
        return direct
    import glob
    hits = sorted(glob.glob(os.path.join(out_html, "*", "src", "index.html")))
    return hits[0] if hits else os.path.join(out_html, "index.html")


def _build_html(unit):
    """Build the HTML site and drop a redirect at the site root so the root URL
    (e.g. https://host/<unit>/) opens the home page wherever it landed."""
    _run([_docfx(), "build", "docfx.json"], unit)
    out_html = os.path.join(unit, "out", "html")
    home = _find_home(out_html)
    if os.path.isfile(home):
        rel = os.path.relpath(home, out_html).replace("\\", "/")
        if rel != "index.html":
            with open(os.path.join(out_html, "index.html"), "w", encoding="utf-8") as f:
                f.write(_redirect_html(rel))
    return out_html, home


def build_html(unit, open_after):
    out_html, home = _build_html(unit)
    index = home if os.path.isfile(home) else os.path.join(out_html, "index.html")
    print("HTML:", index)
    if open_after and os.path.isfile(index) and hasattr(os, "startfile"):
        os.startfile(index)


def build_pdf(unit, name):
    _run([sys.executable, os.path.join(HERE, "gen_toc.py"), unit], HERE)
    _run([_docfx(), "build", "pdf_docfx.json"], unit)
    _run([_docfx(), "pdf", "pdf_docfx.json"], unit)
    out_pdf = os.path.join(unit, "out", "pdf")
    # docfx names the file toc.pdf under the pdf-toc's output dir, which varies
    # with the content dest (e.g. pdf/ or sppx/pdf/); find it wherever it landed.
    import glob
    hits = glob.glob(os.path.join(out_pdf, "**", "toc.pdf"), recursive=True)
    if not hits:
        raise SystemExit("no toc.pdf produced under " + out_pdf)
    name = name or ("CAM-" + os.path.basename(os.path.normpath(unit)) + ".pdf")
    dest = os.path.join(out_pdf, name)
    shutil.copyfile(hits[0], dest)
    print("PDF:", dest)


def serve_html(unit, port):
    # Full-text search needs the site served over HTTP: browsers block the
    # search web worker and the index.json fetch under file://.
    _build_html(unit)
    url = "http://localhost:%d/" % port
    print("Serving on", url, "(Ctrl+C to stop)")
    try:
        import webbrowser
        webbrowser.open(url)
    except Exception:
        pass
    _run([_docfx(), "serve", os.path.join(unit, "out", "html"), "-p", str(port)], unit)


def main():
    ap = argparse.ArgumentParser(description="Build a documentation unit.")
    ap.add_argument("unit", help="path to the unit directory")
    ap.add_argument("target", choices=["html", "pdf", "serve"])
    ap.add_argument("--name", help="output PDF file name (pdf target)")
    ap.add_argument("--open", action="store_true", help="open the HTML after building")
    ap.add_argument("--port", type=int, default=8080, help="port for the serve target")
    a = ap.parse_args()
    unit = os.path.abspath(a.unit)
    if a.target == "html":
        build_html(unit, a.open)
    elif a.target == "serve":
        serve_html(unit, a.port)
    else:
        build_pdf(unit, a.name)


if __name__ == "__main__":
    main()
