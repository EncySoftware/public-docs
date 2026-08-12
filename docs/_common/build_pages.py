#!/usr/bin/env python3
"""Build and add one documentation version to a Pages staging site.

Usage:
    python build_pages.py <repo> <output> <config.json> [--latest]
"""
import argparse
from concurrent.futures import ThreadPoolExecutor
import html
import json
import os
import re
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
UNITS = ("dotnet", "sppx")


def _write(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as stream:
        stream.write(content)


def _page(title, body, language):
    return """<!DOCTYPE html>
<html lang="{language}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <style>
    body {{ font-family: system-ui, sans-serif; max-width: 60rem; margin: 3rem auto; padding: 0 1.5rem; line-height: 1.6; }}
    a {{ color: #0969da; }}
  </style>
</head>
<body>
  <h1>{title}</h1>
  {body}
</body>
</html>
""".format(language=html.escape(language, quote=True), title=html.escape(title), body=body)


def _redirect(target, title, language):
    escaped_target = html.escape(target, quote=True)
    return """<!DOCTYPE html>
<html lang="{language}">
<head>
  <meta charset="utf-8">
  <meta http-equiv="refresh" content="0; url={target}">
  <link rel="canonical" href="{target}">
  <title>{title}</title>
</head>
<body><a href="{target}">{title}</a></body>
</html>
""".format(language=html.escape(language, quote=True), target=escaped_target,
           title=html.escape(title))


def _build_unit(repo, unit):
    unit_dir = os.path.join(repo, "docs", "posts", unit)
    subprocess.check_call([sys.executable, os.path.join(HERE, "build.py"), unit_dir, "html"])
    source = os.path.join(unit_dir, "out", "html")
    if not os.path.isfile(os.path.join(source, "index.html")):
        raise SystemExit("missing built entry point: " + os.path.join(source, "index.html"))
    return unit, source


def _load_config(path):
    with open(path, encoding="utf-8-sig") as stream:
        config = json.load(stream)
    required = ("version", "language", "siteTitle", "versionTitle", "sectionTitle", "unitTitles")
    missing = [key for key in required if key not in config]
    if missing:
        raise SystemExit("missing Pages config keys: " + ", ".join(missing))
    if set(config["unitTitles"]) != set(UNITS):
        raise SystemExit("unitTitles must define: " + ", ".join(UNITS))
    if not re.match(r"^v[1-9][0-9]*$", config["version"]):
        raise SystemExit("version must have the form v<major>, for example v3")
    return config


def _write_site_index(output, title, language):
    versions = sorted(
        name for name in os.listdir(output)
        if re.match(r"^v[1-9][0-9]*$", name) and os.path.isdir(os.path.join(output, name)))
    body = "<ul>" + "".join(
        '<li><a href="{0}/">{0}</a></li>'.format(html.escape(version, quote=True))
        for version in versions) + "</ul>"
    _write(os.path.join(output, "index.html"), _page(title, body, language))


def build_site(repo, output, config_path, latest):
    repo = os.path.abspath(repo)
    output = os.path.abspath(output)
    config = _load_config(config_path)
    version = config["version"]
    version_dir = os.path.join(output, version)
    if os.path.exists(version_dir):
        raise SystemExit("version already exists in staging site: " + version_dir)

    with ThreadPoolExecutor(max_workers=len(UNITS)) as executor:
        built = dict(executor.map(lambda unit: _build_unit(repo, unit), UNITS))

    section = os.path.join(version_dir, "postprocessing")
    for unit in UNITS:
        shutil.copytree(built[unit], os.path.join(section, unit))

    version_body = '<p><a href="postprocessing/">{0}</a></p>'.format(
        html.escape(config["sectionTitle"]))
    section_body = "<ul>" + "".join(
        '<li><a href="{0}/">{1}</a></li>'.format(
            html.escape(unit, quote=True), html.escape(config["unitTitles"][unit]))
        for unit in UNITS) + "</ul>"

    _write(os.path.join(version_dir, "index.html"),
           _page(config["versionTitle"], version_body, config["language"]))
    _write(os.path.join(section, "index.html"),
           _page(config["sectionTitle"], section_body, config["language"]))
    os.makedirs(output, exist_ok=True)
    _write_site_index(output, config["siteTitle"], config["language"])
    _write(os.path.join(output, ".nojekyll"), "")

    if latest:
        latest_dir = os.path.join(output, "latest")
        if os.path.exists(latest_dir):
            raise SystemExit("latest already exists in staging site: " + latest_dir)
        _write(os.path.join(latest_dir, "index.html"),
               _redirect("../{0}/".format(version), config["versionTitle"], config["language"]))

    print("Pages site:", output)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("repo", help="documentation repository root")
    parser.add_argument("output", help="staging directory for the complete Pages site")
    parser.add_argument("config", help="JSON configuration for this documentation version")
    parser.add_argument("--latest", action="store_true", help="point /latest/ at this version")
    args = parser.parse_args()
    build_site(args.repo, args.output, args.config, args.latest)


if __name__ == "__main__":
    main()
