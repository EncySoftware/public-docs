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
SLUG_RE = re.compile(r"^[a-z0-9][a-z0-9-]*$")
COLOR_RE = re.compile(r"^#[0-9a-fA-F]{6}$")

ICONS = {
    "code": (
        '<path d="m9 18-6-6 6-6"/><path d="m15 6 6 6-6 6"/>'
        '<path d="m14 4-4 16"/>'
    ),
    "integration": (
        '<rect x="3" y="3" width="7" height="7" rx="2"/>'
        '<rect x="14" y="14" width="7" height="7" rx="2"/>'
        '<path d="M10 6.5h4a3.5 3.5 0 0 1 3.5 3.5v4"/>'
        '<path d="m14.5 11 3 3 3-3"/>'
    ),
    "settings": (
        '<path d="M4 7h10"/><path d="M18 7h2"/><circle cx="16" cy="7" r="2"/>'
        '<path d="M4 17h2"/><path d="M10 17h10"/><circle cx="8" cy="17" r="2"/>'
        '<path d="M4 12h4"/><path d="M12 12h8"/><circle cx="10" cy="12" r="2"/>'
    ),
    "link": (
        '<path d="M10 13a5 5 0 0 0 7.1.1l2-2a5 5 0 0 0-7.1-7.1l-1.1 1.1"/>'
        '<path d="M14 11a5 5 0 0 0-7.1-.1l-2 2A5 5 0 0 0 12 20l1.1-1.1"/>'
    ),
    "help": (
        '<circle cx="12" cy="12" r="9"/>'
        '<path d="M9.8 9a2.4 2.4 0 1 1 3.4 2.2c-.8.4-1.2.9-1.2 1.8"/>'
        '<path d="M12 17h.01"/>'
    ),
    "book": (
        '<path d="M4 5.5A2.5 2.5 0 0 1 6.5 3H11v16H6.5A2.5 2.5 0 0 0 4 21.5z"/>'
        '<path d="M20 5.5A2.5 2.5 0 0 0 17.5 3H13v16h4.5a2.5 2.5 0 0 1 2.5 2.5z"/>'
    ),
}

CSS = r"""
:root {
  --brand: __PRIMARY__;
  --brand-deep: __DEEP__;
  --accent: __ACCENT__;
  --ink: #152033;
  --muted: #667085;
  --line: #dfe5ee;
  --surface: #ffffff;
  --canvas: #f4f7fb;
  --shadow: 0 18px 50px rgba(20, 32, 51, .10);
}
* { box-sizing: border-box; }
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border: 0;
}
html { scroll-behavior: smooth; }
body {
  margin: 0;
  overflow-x: hidden;
  color: var(--ink);
  background:
    radial-gradient(circle at 15% -10%, color-mix(in srgb, var(--brand) 13%, transparent), transparent 35rem),
    var(--canvas);
  font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  line-height: 1.55;
  -webkit-font-smoothing: antialiased;
}
a { color: inherit; }
.site-header {
  position: relative;
  z-index: 10;
  border-bottom: 1px solid rgba(223, 229, 238, .82);
  background: rgba(255, 255, 255, .88);
  backdrop-filter: blur(18px);
}
.site-header__inner,
.page,
.site-footer__inner {
  width: min(1180px, calc(100% - 40px));
  margin: 0 auto;
}
.site-header__inner {
  min-height: 76px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 24px;
}
.brand {
  display: inline-flex;
  align-items: center;
  gap: 12px;
  text-decoration: none;
}
.brand__logo-shell {
  min-width: 44px;
  height: 44px;
  display: grid;
  place-items: center;
}
.brand__logo { display: block; width: auto; max-width: 108px; max-height: 34px; }
.brand__copy { display: grid; line-height: 1.15; }
.brand__copy strong { font-size: 15px; letter-spacing: .01em; }
.brand__copy span { margin-top: 4px; color: var(--muted); font-size: 12px; }
.site-search {
  position: relative;
  flex: 1 1 320px;
  max-width: 360px;
  margin-left: auto;
}
.site-search__field {
  height: 42px;
  display: flex;
  align-items: center;
  gap: 9px;
  padding: 0 13px;
  border: 1px solid var(--line);
  border-radius: 12px;
  background: #f8fafc;
  transition: border-color .18s ease, box-shadow .18s ease, background .18s ease;
}
.site-search:focus-within .site-search__field {
  border-color: var(--brand);
  background: white;
  box-shadow: 0 0 0 3px color-mix(in srgb, var(--brand) 15%, transparent);
}
.site-search__field svg { width: 18px; height: 18px; flex: 0 0 auto; color: var(--muted); }
.site-search input {
  width: 100%;
  min-width: 0;
  padding: 0;
  border: 0;
  outline: 0;
  color: var(--ink);
  background: transparent;
  font: inherit;
  font-size: 14px;
}
.site-search input::placeholder { color: #87909f; }
.site-search__results {
  position: absolute;
  top: calc(100% + 10px);
  right: 0;
  z-index: 30;
  width: min(520px, calc(100vw - 32px));
  max-height: min(540px, calc(100vh - 110px));
  overflow-y: auto;
  border: 1px solid var(--line);
  border-radius: 16px;
  background: white;
  box-shadow: 0 24px 60px rgba(20, 32, 51, .18);
}
.site-search__results[hidden] { display: none; }
.site-search__summary { padding: 12px 15px; color: var(--muted); font-size: 12px; font-weight: 750; }
.site-search__result {
  display: grid;
  gap: 3px;
  padding: 12px 15px;
  border-top: 1px solid #edf0f4;
  text-decoration: none;
}
.site-search__result:hover,
.site-search__result:focus,
.site-search__result.is-active { outline: 0; background: color-mix(in srgb, var(--brand) 8%, white); }
.site-search__result strong { color: var(--ink); font-size: 14px; line-height: 1.35; }
.site-search__result span { color: var(--muted); font-size: 12px; }
.site-nav { flex: 0 0 auto; display: flex; align-items: center; gap: 8px; }
.site-nav a {
  padding: 9px 13px;
  color: #475467;
  border-radius: 10px;
  font-size: 14px;
  font-weight: 650;
  text-decoration: none;
}
.site-nav a:hover { color: var(--brand-deep); background: #f0f4f8; }
.page { padding: 34px 0 84px; }
.breadcrumbs {
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  gap: 8px;
  margin: 0 0 20px;
  color: var(--muted);
  font-size: 13px;
}
.breadcrumbs a { color: var(--brand-deep); text-decoration: none; font-weight: 650; }
.breadcrumbs svg { width: 14px; height: 14px; opacity: .55; }
.hero {
  position: relative;
  min-height: 370px;
  padding: clamp(34px, 6vw, 72px);
  overflow: hidden;
  display: grid;
  align-items: center;
  border-radius: 30px;
  color: white;
  background:
    linear-gradient(118deg, var(--brand-deep) 0%, color-mix(in srgb, var(--brand-deep) 70%, var(--brand)) 54%, var(--brand) 130%);
  box-shadow: 0 26px 70px color-mix(in srgb, var(--brand-deep) 25%, transparent);
}
.hero--compact { min-height: 300px; }
.hero::before,
.hero::after {
  content: "";
  position: absolute;
  border-radius: 999px;
  pointer-events: none;
}
.hero::before {
  width: 430px;
  height: 430px;
  top: -230px;
  right: -80px;
  border: 1px solid rgba(255,255,255,.19);
  box-shadow: 0 0 0 70px rgba(255,255,255,.04), 0 0 0 140px rgba(255,255,255,.025);
}
.hero::after {
  width: 240px;
  height: 240px;
  right: 15%;
  bottom: -190px;
  background: var(--accent);
  filter: blur(3px);
  opacity: .16;
}
.hero__content { position: relative; z-index: 1; width: 100%; min-width: 0; max-width: 770px; }
.hero__brand-art {
  position: absolute;
  z-index: 0;
  width: min(33vw, 390px);
  right: 6%;
  top: 50%;
  transform: translateY(-50%);
  opacity: .09;
  pointer-events: none;
}
.hero__brand-art img { display: block; width: 100%; max-height: 250px; object-fit: contain; }
.eyebrow {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 18px;
  color: rgba(255,255,255,.82);
  font-size: 12px;
  font-weight: 800;
  letter-spacing: .13em;
  text-transform: uppercase;
}
.eyebrow::before {
  content: "";
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: var(--accent);
  box-shadow: 0 0 0 5px color-mix(in srgb, var(--accent) 18%, transparent);
}
.hero h1 {
  max-width: 820px;
  margin: 0;
  font-size: clamp(38px, 6vw, 68px);
  line-height: 1.02;
  letter-spacing: -.045em;
}
.hero--compact h1 { font-size: clamp(34px, 5vw, 56px); }
.hero__lead {
  max-width: 700px;
  margin: 22px 0 0;
  color: rgba(255,255,255,.78);
  font-size: clamp(17px, 2vw, 20px);
  line-height: 1.65;
}
.hero__actions { display: flex; flex-wrap: wrap; gap: 12px; margin-top: 30px; }
.button {
  min-height: 46px;
  padding: 0 18px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 9px;
  border: 1px solid transparent;
  border-radius: 13px;
  font-size: 14px;
  font-weight: 780;
  text-decoration: none;
  transition: transform .18s ease, background .18s ease, border-color .18s ease;
}
.button:hover { transform: translateY(-2px); }
.button--primary { color: var(--brand-deep); background: white; }
.button--ghost { color: white; border-color: rgba(255,255,255,.26); background: rgba(255,255,255,.08); }
.button--ghost:hover { background: rgba(255,255,255,.14); }
.button svg { width: 17px; height: 17px; }
.hero__stats {
  position: relative;
  z-index: 1;
  align-self: end;
  display: flex;
  gap: 12px;
  margin-top: 38px;
}
.stat {
  min-width: 120px;
  padding: 14px 16px;
  border: 1px solid rgba(255,255,255,.15);
  border-radius: 15px;
  background: rgba(255,255,255,.08);
}
.stat strong { display: block; font-size: 21px; }
.stat span { color: rgba(255,255,255,.66); font-size: 12px; }
.content-section { padding-top: 64px; }
.section-heading {
  max-width: 720px;
  margin-bottom: 25px;
}
.section-heading h2 { margin: 0; font-size: clamp(27px, 4vw, 38px); letter-spacing: -.03em; }
.section-heading p { margin: 10px 0 0; color: var(--muted); font-size: 16px; }
.section-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 18px;
}
.section-card,
.guide-card {
  position: relative;
  min-height: 260px;
  padding: 27px;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  border: 1px solid var(--line);
  border-radius: 22px;
  background: var(--surface);
  box-shadow: 0 4px 18px rgba(20,32,51,.035);
  text-decoration: none;
  transition: transform .2s ease, box-shadow .2s ease, border-color .2s ease;
}
.section-card:hover,
.guide-card:hover {
  transform: translateY(-5px);
  border-color: color-mix(in srgb, var(--brand) 42%, var(--line));
  box-shadow: var(--shadow);
}
.card-top { display: flex; justify-content: space-between; align-items: flex-start; gap: 18px; }
.card-icon {
  width: 48px;
  height: 48px;
  flex: 0 0 auto;
  display: grid;
  place-items: center;
  border-radius: 15px;
  color: var(--brand-deep);
  background: color-mix(in srgb, var(--brand) 12%, white);
}
.card-icon svg { width: 25px; height: 25px; }
.card-count,
.guide-card__meta {
  padding: 6px 9px;
  border-radius: 999px;
  color: var(--muted);
  background: #f3f5f8;
  font-size: 11px;
  font-weight: 800;
  letter-spacing: .03em;
}
.section-card h3,
.guide-card h3 { margin: 20px 0 8px; font-size: 22px; line-height: 1.2; letter-spacing: -.02em; }
.section-card > p,
.guide-card > p { margin: 0; color: var(--muted); font-size: 14px; }
.mini-list {
  margin: 18px 0 0;
  padding: 0;
  display: flex;
  flex-wrap: wrap;
  gap: 7px;
  list-style: none;
}
.mini-list li {
  padding: 5px 9px;
  border: 1px solid #e5eaf1;
  border-radius: 8px;
  color: #475467;
  background: #fafbfc;
  font-size: 12px;
}
.card-link {
  margin-top: auto;
  padding-top: 22px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  color: var(--brand-deep);
  font-size: 13px;
  font-weight: 800;
}
.card-link svg { width: 18px; height: 18px; transition: transform .18s ease; }
.section-card:hover .card-link svg,
.guide-card:hover .card-link svg { transform: translateX(4px); }
.guide-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 18px;
}
.guide-card { min-height: 250px; }
.versions {
  padding: 24px;
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
  border: 1px solid var(--line);
  border-radius: 20px;
  background: white;
}
.version-chip {
  min-width: 112px;
  padding: 12px 15px;
  display: grid;
  border: 1px solid var(--line);
  border-radius: 13px;
  text-decoration: none;
  transition: border-color .18s ease, background .18s ease;
}
.version-chip strong { font-size: 16px; }
.version-chip span { margin-top: 2px; color: var(--muted); font-size: 11px; }
.version-chip:hover,
.version-chip--current { border-color: var(--brand); background: color-mix(in srgb, var(--brand) 7%, white); }
.site-footer { border-top: 1px solid var(--line); background: white; }
.site-footer__inner {
  min-height: 88px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 20px;
  color: var(--muted);
  font-size: 13px;
}
.site-footer a { color: var(--brand-deep); font-weight: 700; text-decoration: none; }
.site-footer__links { display: flex; flex-wrap: wrap; gap: 18px; }

/* Dark graphite composition with a turquoise-to-blue signature gradient. */
.theme-dark {
  --ink: #252935;
  --muted: #68707f;
  --line: #dfe2e7;
  --canvas: #eeeff1;
  --shadow: 0 24px 60px rgba(37, 41, 53, .14);
  font-family: Montserrat, "Segoe UI", Arial, sans-serif;
}
.theme-dark .site-header { background: rgba(255,255,255,.94); border-bottom-color: #e4e7eb; }
.theme-dark .brand__logo-shell { min-width: 90px; justify-content: start; }
.theme-dark .brand__logo { width: 82px; max-width: 82px; }
.theme-dark .site-nav a { border-radius: 999px; }
.theme-dark .site-nav a:last-child { padding-inline: 20px; color: white; background: #252935; }
.theme-dark .site-nav a:last-child:hover { background: #13151b; }
.theme-dark .hero { min-height: 480px; background: #252935; box-shadow: 0 30px 75px rgba(37,41,53,.2); }
.theme-dark .hero::before {
  width: 100%; height: 6px; left: 0; right: 0; top: auto; bottom: 0;
  border: 0; border-radius: 0; background: linear-gradient(90deg, #00cb9a, #1269d9); box-shadow: none;
}
.theme-dark .hero::after {
  width: 520px; height: 520px; right: -150px; bottom: -280px;
  border: 1px solid rgba(255,255,255,.09); background: transparent;
  box-shadow: 0 0 0 76px rgba(255,255,255,.025), 0 0 0 152px rgba(255,255,255,.018);
  filter: none; opacity: 1;
}
.theme-dark .hero__brand-art { right: 5%; opacity: .115; filter: saturate(.8); }
.theme-dark .eyebrow { padding: 7px 12px; border: 1px solid rgba(255,255,255,.14); border-radius: 999px; letter-spacing: .05em; text-transform: none; }
.theme-dark .hero h1 { max-width: 790px; font-weight: 650; }
.theme-dark .button { border-radius: 999px; }
.theme-dark .button--primary { color: white; background: linear-gradient(95deg, #00cb9a, #1269d9); }
.theme-dark .button--primary:hover { box-shadow: 0 12px 28px rgba(0,203,154,.2); }
.theme-dark .card-icon { color: #1269d9; background: linear-gradient(135deg, rgba(0,203,154,.14), rgba(18,105,217,.13)); }
.theme-dark .section-card:hover,
.theme-dark .guide-card:hover { border-color: #00cb9a; }
.theme-dark .card-link,
.theme-dark .breadcrumbs a,
.theme-dark .site-footer a { color: #1269d9; }

/* Light modular composition with the red product accent. */
.theme-light {
  --ink: #1f1f1f;
  --muted: #68727b;
  --line: #e1e5e7;
  --surface: #ffffff;
  --canvas: #f4f6f7;
  --shadow: 0 24px 65px rgba(9,8,9,.09);
  font-family: Onest, "Segoe UI", Arial, sans-serif;
  background: #f4f6f7;
}
.theme-light .site-header { padding-top: 8px; border: 0; background: transparent; backdrop-filter: none; }
.theme-light .site-header__inner { width: min(1280px, calc(100% - 40px)); }
.theme-light .brand { padding: 6px 18px 6px 7px; border-radius: 15px; background: #eceff0; }
.theme-light .brand__logo-shell { width: 48px; min-width: 48px; height: 48px; border-radius: 12px; background: white; }
.theme-light .brand__logo { width: 28px; max-height: 31px; }
.theme-light .site-nav { padding: 5px; border-radius: 15px; background: #eceff0; }
.theme-light .site-nav a { min-height: 42px; padding-inline: 16px; display: inline-flex; align-items: center; border-radius: 11px; }
.theme-light .site-nav a:hover { color: #1f1f1f; background: white; }
.theme-light .site-nav a:last-child { padding-inline: 20px; color: white; background: #ff3333; }
.theme-light .site-nav a:last-child:hover { color: white; background: #e72424; }
.theme-light .page { padding-top: 44px; }
.theme-light .breadcrumbs { margin-bottom: 4px; }
.theme-light .breadcrumbs a { color: #1f1f1f; }
.theme-light .hero {
  min-height: 455px; padding-top: 60px; padding-bottom: 60px; justify-items: center;
  color: #1f1f1f; background: transparent; border-radius: 0; box-shadow: none; text-align: center;
}
.theme-light .hero::before {
  width: 410px; height: 410px; top: 16px; right: -130px;
  border: 1px solid rgba(9,30,51,.08);
  box-shadow: 0 0 0 58px rgba(255,255,255,.42), 0 0 0 116px rgba(9,30,51,.025);
}
.theme-light .hero::after {
  width: 14px; height: 14px; right: 8%; bottom: 18%; background: #ff3333;
  box-shadow: 0 0 0 16px rgba(255,51,51,.09); filter: none; opacity: 1;
}
.theme-light .hero__content { max-width: 900px; }
.theme-light .hero__brand-art { width: 240px; right: 2%; opacity: .045; }
.theme-light .eyebrow { margin-bottom: 24px; padding: 8px 14px; color: #4c555c; background: #eceff0; border-radius: 999px; letter-spacing: .02em; text-transform: none; }
.theme-light .eyebrow::before { background: #ff3333; box-shadow: none; }
.theme-light .hero h1 { max-width: 970px; font-weight: 500; letter-spacing: -.035em; }
.theme-light .hero__lead { margin-inline: auto; color: #59636c; }
.theme-light .hero__actions,
.theme-light .hero__stats { justify-content: center; }
.theme-light .button { min-height: 52px; padding-inline: 22px; border-radius: 14px; }
.theme-light .button--primary { color: white; background: #ff3333; }
.theme-light .button--primary:hover { background: #e72424; }
.theme-light .button--ghost { color: #1f1f1f; border-color: #d8dddf; background: white; }
.theme-light .button--ghost:hover { background: #eceff0; }
.theme-light .stat { color: #1f1f1f; border-color: #dfe3e5; background: white; }
.theme-light .stat span { color: #68727b; }
.theme-light .content-section { padding-top: 54px; }
.theme-light .section-heading { max-width: 830px; }
.theme-light .section-heading h2 { font-weight: 500; }
.theme-light .section-card,
.theme-light .guide-card { border-color: transparent; border-radius: 20px; box-shadow: none; }
.theme-light .section-card:hover,
.theme-light .guide-card:hover { border-color: #ff3333; box-shadow: var(--shadow); }
.theme-light .card-icon { color: #1f1f1f; background: #eceff0; border-radius: 13px; }
.theme-light .card-count,
.theme-light .guide-card__meta { color: #5b646b; background: #eceff0; }
.theme-light .card-link,
.theme-light .site-footer a { color: #e72424; }
.theme-light .versions { border: 0; border-radius: 20px; }
.theme-light .version-chip:hover,
.theme-light .version-chip--current { border-color: #ff3333; background: #fff5f5; }
@media (max-width: 980px) {
  .site-header__inner { gap: 12px; }
  .site-nav a:first-child { display: none; }
  .site-search { flex-basis: 250px; }
}
@media (max-width: 760px) {
  .site-header__inner, .page, .site-footer__inner { width: min(1180px, calc(100% - 24px)); }
  .site-header__inner { min-height: 66px; }
  .brand__copy { display: none; }
  .site-search { max-width: none; }
  .site-nav a { padding: 8px; }
  .page { padding-top: 20px; }
  .hero { min-height: 0; padding: 34px 25px; border-radius: 22px; }
  .theme-dark .hero, .theme-light .hero { min-height: 0; }
  .theme-light .hero { padding: 42px 20px; border-radius: 0; }
  .hero__brand-art { display: none; }
  .hero__stats { flex-wrap: wrap; }
  .stat { min-width: 105px; }
  .content-section { padding-top: 46px; }
  .section-grid, .guide-grid { grid-template-columns: 1fr; }
  .section-card, .guide-card { min-height: 235px; padding: 23px; }
  .site-footer__inner { padding: 22px 0; align-items: flex-start; flex-direction: column; justify-content: center; }
}
@media (max-width: 520px) {
  .site-nav { display: none; }
  .site-search { margin-left: 0; }
  .brand__copy strong { font-size: 14px; }
  .hero__actions { display: grid; grid-template-columns: minmax(0, 1fr); }
  .hero__actions .button { width: 100%; max-width: 100%; }
  .hero h1, .hero__lead { overflow-wrap: anywhere; }
}
"""

PORTAL_JS = r"""
(function () {
  "use strict";

  var form = document.querySelector(".site-search[data-search-index]");
  if (!form || !window.fetch) return;

  var input = form.querySelector("input[type=search]");
  var panel = form.querySelector(".site-search__results");
  var indexPromise = null;
  var activeIndex = -1;
  var visibleLinks = [];

  function loadIndex() {
    if (!indexPromise) {
      indexPromise = fetch(form.getAttribute("data-search-index"), { credentials: "same-origin" })
        .then(function (response) {
          if (!response.ok) throw new Error("Search index: " + response.status);
          return response.json();
        })
        .then(function (payload) { return Array.isArray(payload.items) ? payload.items : []; });
    }
    return indexPromise;
  }

  function normalize(value) {
    return String(value || "").toLocaleLowerCase();
  }

  function find(items, query) {
    var terms = normalize(query).split(/\s+/).filter(Boolean);
    if (!terms.length) return [];
    return items.map(function (item) {
      var title = normalize(item.title);
      var guide = normalize(item.guide);
      var keywords = normalize(item.keywords);
      var score = 0;
      for (var i = 0; i < terms.length; i++) {
        var term = terms[i];
        if (title.indexOf(term) !== -1) score += title.indexOf(term) === 0 ? 80 : 45;
        else if (guide.indexOf(term) !== -1) score += 18;
        else if (keywords.indexOf(term) !== -1) score += 4;
        else return null;
      }
      return { item: item, score: score };
    }).filter(Boolean).sort(function (left, right) {
      return right.score - left.score || left.item.title.localeCompare(right.item.title);
    }).slice(0, 24);
  }

  function clearPanel() {
    panel.hidden = true;
    panel.textContent = "";
    activeIndex = -1;
    visibleLinks = [];
  }

  function render(results) {
    panel.textContent = "";
    activeIndex = -1;
    visibleLinks = [];

    var summary = document.createElement("div");
    summary.className = "site-search__summary";
    summary.textContent = results.length
      ? form.getAttribute("data-search-results")
      : form.getAttribute("data-search-empty");
    panel.appendChild(summary);

    var root = new URL(form.getAttribute("data-search-root"), window.location.href);
    results.forEach(function (result) {
      var item = result.item;
      var link = document.createElement("a");
      link.className = "site-search__result";
      link.href = new URL(item.href, root).href;

      var title = document.createElement("strong");
      title.textContent = item.title;
      var guide = document.createElement("span");
      guide.textContent = item.guide;
      link.appendChild(title);
      link.appendChild(guide);
      panel.appendChild(link);
      visibleLinks.push(link);
    });
    panel.hidden = false;
  }

  function runSearch() {
    var query = input.value.trim();
    if (query.length < 2) {
      clearPanel();
      return;
    }
    form.setAttribute("aria-busy", "true");
    loadIndex().then(function (items) {
      if (input.value.trim() === query) render(find(items, query));
    }).catch(function () {
      if (input.value.trim() === query) render([]);
    }).then(function () {
      form.removeAttribute("aria-busy");
    });
  }

  function selectResult(next) {
    if (!visibleLinks.length) return;
    if (activeIndex >= 0) visibleLinks[activeIndex].classList.remove("is-active");
    activeIndex = (next + visibleLinks.length) % visibleLinks.length;
    visibleLinks[activeIndex].classList.add("is-active");
    visibleLinks[activeIndex].scrollIntoView({ block: "nearest" });
  }

  var timer = null;
  input.addEventListener("input", function () {
    window.clearTimeout(timer);
    timer = window.setTimeout(runSearch, 180);
  });
  input.addEventListener("keydown", function (event) {
    if (event.key === "Escape") clearPanel();
    else if (event.key === "ArrowDown") { event.preventDefault(); selectResult(activeIndex + 1); }
    else if (event.key === "ArrowUp") { event.preventDefault(); selectResult(activeIndex - 1); }
    else if (event.key === "Enter" && activeIndex >= 0) {
      event.preventDefault();
      visibleLinks[activeIndex].click();
    }
  });
  form.addEventListener("submit", function (event) {
    event.preventDefault();
    if (visibleLinks.length) visibleLinks[Math.max(activeIndex, 0)].click();
  });
  document.addEventListener("click", function (event) {
    if (!form.contains(event.target)) clearPanel();
  });
})();
"""


def _write(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as stream:
        stream.write(content)


def _prepare_docfx_html(directory, config):
    language = _attr(config["language"])
    portal_label = _attr(config["labels"]["home"])
    marker = 'name="documentation-portal-label"'

    for root, _, files in os.walk(directory):
        for name in files:
            if not name.lower().endswith(".html"):
                continue

            path = os.path.join(root, name)
            with open(path, "rb") as stream:
                raw = stream.read()
            has_bom = raw.startswith(b"\xef\xbb\xbf")
            document = raw.decode("utf-8-sig")

            def set_language(match):
                attributes = match.group(1)
                if re.search(r"\blang\s*=", attributes, re.IGNORECASE):
                    attributes = re.sub(
                        r"\blang\s*=\s*([\"']).*?\1",
                        'lang="%s"' % language,
                        attributes,
                        count=1,
                        flags=re.IGNORECASE,
                    )
                else:
                    attributes += ' lang="%s"' % language
                return "<html%s>" % attributes

            updated, html_count = re.subn(
                r"<html([^>]*)>", set_language, document, count=1, flags=re.IGNORECASE
            )
            if not html_count:
                raise SystemExit("missing html element: " + path)

            if marker not in updated:
                newline = "\r\n" if "\r\n" in updated else "\n"
                meta = (
                    '    <meta name="documentation-portal-label" content="%s">%s'
                    % (portal_label, newline)
                )
                updated, head_count = re.subn(
                    r"</head>", meta + "</head>", updated, count=1, flags=re.IGNORECASE
                )
                if not head_count:
                    raise SystemExit("missing head element: " + path)

            encoded = updated.encode("utf-8")
            if has_bom:
                encoded = b"\xef\xbb\xbf" + encoded
            with open(path, "wb") as stream:
                stream.write(encoded)


def _svg(content, class_name=""):
    class_attr = ' class="%s"' % html.escape(class_name, quote=True) if class_name else ""
    return (
        '<svg%s viewBox="0 0 24 24" fill="none" stroke="currentColor" '
        'stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" '
        'aria-hidden="true">%s</svg>' % (class_attr, content)
    )


def _icon(name):
    return _svg(ICONS.get(name, ICONS["book"]))


def _arrow():
    return _svg('<path d="M5 12h14"/><path d="m13 6 6 6-6 6"/>')


def _chevron():
    return _svg('<path d="m9 18 6-6-6-6"/>')


def _safe(value):
    return html.escape(str(value))


def _attr(value):
    return html.escape(str(value), quote=True)


def _validate_slug(value, label):
    if not isinstance(value, str) or not SLUG_RE.match(value):
        raise SystemExit("%s must contain lowercase ASCII letters, digits and hyphens" % label)


def _validate_source(value, label):
    if not isinstance(value, str) or not value or "\\" in value:
        raise SystemExit("%s must be a non-empty forward-slash path" % label)
    parts = value.split("/")
    if any(part in ("", ".", "..") for part in parts):
        raise SystemExit("%s contains an unsafe path segment" % label)


def _load_config(path):
    with open(path, encoding="utf-8-sig") as stream:
        config = json.load(stream)

    required = (
        "version", "language", "siteTitle", "siteDescription", "versionTitle",
        "versionDescription", "repositoryUrl", "brand", "theme", "labels", "sections",
    )
    missing = [key for key in required if key not in config]
    if missing:
        raise SystemExit("missing Pages config keys: " + ", ".join(missing))
    if not re.match(r"^v[1-9][0-9]*$", config["version"]):
        raise SystemExit("version must have the form v<major>, for example v3")
    if not isinstance(config["sections"], list) or not config["sections"]:
        raise SystemExit("sections must be a non-empty list")

    label_keys = (
        "home", "latest", "source", "browse", "current", "exploreTitle",
        "exploreDescription", "versionsTitle", "versionsDescription", "open",
        "guide", "collection", "guideCount", "sectionCount", "footer",
        "search", "searchResults", "searchNoResults",
    )
    missing_labels = [key for key in label_keys if key not in config["labels"]]
    if missing_labels:
        raise SystemExit("missing label keys: " + ", ".join(missing_labels))

    theme_keys = ("primary", "deep", "accent")
    for key in theme_keys:
        value = config["theme"].get(key)
        if not isinstance(value, str) or not COLOR_RE.match(value):
            raise SystemExit("theme.%s must be a six-digit hex color" % key)

    brand_keys = ("name", "websiteUrl", "websiteLabel", "logo", "variant")
    missing_brand = [key for key in brand_keys if key not in config["brand"]]
    if missing_brand:
        raise SystemExit("missing brand keys: " + ", ".join(missing_brand))
    if config["brand"]["variant"] not in ("dark", "light"):
        raise SystemExit("brand.variant must be dark or light")
    if not re.match(r"^[a-z0-9][a-z0-9-]*\.svg$", config["brand"]["logo"]):
        raise SystemExit("brand.logo must be a simple lowercase SVG filename")
    if not config["brand"]["websiteUrl"].startswith("https://"):
        raise SystemExit("brand.websiteUrl must use https")

    section_slugs = set()
    output_paths = set()
    sources = set()
    for section_index, section in enumerate(config["sections"]):
        prefix = "sections[%d]" % section_index
        for key in ("slug", "title", "description", "icon", "units"):
            if key not in section:
                raise SystemExit("missing %s.%s" % (prefix, key))
        _validate_slug(section["slug"], prefix + ".slug")
        if section["slug"] in section_slugs:
            raise SystemExit("duplicate section slug: " + section["slug"])
        section_slugs.add(section["slug"])
        if section["icon"] not in ICONS:
            raise SystemExit("unknown section icon: " + section["icon"])
        if not isinstance(section["units"], list) or not section["units"]:
            raise SystemExit(prefix + ".units must be a non-empty list")
        direct = bool(section.get("direct"))
        if direct and len(section["units"]) != 1:
            raise SystemExit(prefix + " can be direct only when it contains one unit")

        unit_slugs = set()
        for unit_index, unit in enumerate(section["units"]):
            unit_prefix = "%s.units[%d]" % (prefix, unit_index)
            for key in ("slug", "source", "title", "description", "meta"):
                if key not in unit:
                    raise SystemExit("missing %s.%s" % (unit_prefix, key))
            _validate_slug(unit["slug"], unit_prefix + ".slug")
            _validate_source(unit["source"], unit_prefix + ".source")
            if unit["slug"] in unit_slugs:
                raise SystemExit("duplicate unit slug in %s: %s" % (section["slug"], unit["slug"]))
            if unit["source"] in sources:
                raise SystemExit("duplicate documentation source: " + unit["source"])
            unit_slugs.add(unit["slug"])
            sources.add(unit["source"])
            relative_output = section["slug"] if direct else section["slug"] + "/" + unit["slug"]
            if relative_output in output_paths:
                raise SystemExit("duplicate Pages output: " + relative_output)
            output_paths.add(relative_output)
    return config


def _unit_entries(config):
    entries = []
    for section in config["sections"]:
        direct = bool(section.get("direct"))
        for unit in section["units"]:
            entry = dict(unit)
            entry["sectionSlug"] = section["slug"]
            entry["output"] = section["slug"] if direct else section["slug"] + "/" + unit["slug"]
            entries.append(entry)
    return entries


def _validate_source_coverage(repo, entries):
    docs_root = os.path.join(repo, "docs")
    configured = set(entry["source"] for entry in entries)
    available = set()
    for root, directories, files in os.walk(docs_root):
        directories[:] = [
            name for name in directories
            if name not in ("out", "obj", "__pycache__")
        ]
        if "docfx.json" in files:
            relative = os.path.relpath(root, docs_root).replace("\\", "/")
            available.add(relative)
    missing = sorted(available - configured)
    unknown = sorted(configured - available)
    if missing:
        raise SystemExit("DocFX units missing from Pages config: " + ", ".join(missing))
    if unknown:
        raise SystemExit("Pages config references unknown DocFX units: " + ", ".join(unknown))


def _build_unit(repo, entry):
    unit_dir = os.path.join(repo, "docs", *entry["source"].split("/"))
    config_path = os.path.join(unit_dir, "docfx.json")
    if not os.path.isfile(config_path):
        raise SystemExit("missing DocFX config: " + config_path)
    subprocess.check_call([sys.executable, os.path.join(HERE, "build.py"), unit_dir, "html"])
    source = os.path.join(unit_dir, "out", "html")
    if not os.path.isfile(os.path.join(source, "index.html")):
        raise SystemExit("missing built entry point: " + os.path.join(source, "index.html"))
    return entry["source"], source


def _write_search_index(version_dir, entries, built):
    items = []
    for entry in entries:
        index_path = os.path.join(built[entry["source"]], "index.json")
        if not os.path.isfile(index_path):
            raise SystemExit("missing DocFX search index: " + index_path)
        with open(index_path, encoding="utf-8-sig") as stream:
            source_index = json.load(stream)
        if not isinstance(source_index, dict):
            raise SystemExit("DocFX search index must be an object: " + index_path)
        for source_item in source_index.values():
            if not isinstance(source_item, dict):
                continue
            href = source_item.get("href")
            title = source_item.get("title")
            if not isinstance(href, str) or not href or not isinstance(title, str) or not title:
                continue
            normalized_href = href.replace("\\", "/")
            while normalized_href.startswith("./"):
                normalized_href = normalized_href[2:]
            if (not normalized_href or normalized_href.startswith(("/", "../"))
                    or "://" in normalized_href):
                continue
            items.append({
                "href": entry["output"] + "/" + normalized_href,
                "title": title,
                "guide": entry["title"],
                "keywords": source_item.get("keywords", ""),
            })
    items.sort(key=lambda item: (item["title"].casefold(), item["href"]))
    payload = {"items": items}
    _write(
        os.path.join(version_dir, "search-index.json"),
        json.dumps(payload, ensure_ascii=False, separators=(",", ":")) + "\n",
    )


def _breadcrumbs(items):
    if not items:
        return ""
    parts = []
    for index, item in enumerate(items):
        label, href = item
        if index:
            parts.append(_chevron())
        if href:
            parts.append('<a href="%s">%s</a>' % (_attr(href), _safe(label)))
        else:
            parts.append("<span>%s</span>" % _safe(label))
    return '<nav class="breadcrumbs" aria-label="Breadcrumb">%s</nav>' % "".join(parts)


def _document(
        config, title, description, body, home_href, latest_href, asset_href,
        search_index_href, search_root_href, crumbs=None):
    labels = config["labels"]
    page_title = title if title == config["siteTitle"] else "%s · %s" % (title, config["siteTitle"])
    return """<!DOCTYPE html>
<html lang="{language}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="{description}">
  <meta name="color-scheme" content="light">
  <meta name="theme-color" content="{theme}">
  <title>{page_title}</title>
  <link rel="stylesheet" href="{asset_href}portal.css">
</head>
<body class="theme-{variant}">
  <header class="site-header">
    <div class="site-header__inner">
      <a class="brand" href="{home_href}">
        <span class="brand__logo-shell"><img class="brand__logo" src="{logo_href}" alt="{brand_name}"></span>
        <span class="brand__copy"><strong>{site_title}</strong><span>{home_label}</span></span>
      </a>
      <form class="site-search" role="search" data-search-index="{search_index_href}"
            data-search-root="{search_root_href}" data-search-results="{search_results}"
            data-search-empty="{search_empty}">
        <label class="site-search__field">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><circle cx="11" cy="11" r="7"></circle><path d="m20 20-4-4"></path></svg>
          <span class="sr-only">{search_label}</span>
          <input type="search" placeholder="{search_label}" autocomplete="off" aria-label="{search_label}" aria-controls="portal-search-results">
        </label>
        <div class="site-search__results" id="portal-search-results" aria-live="polite" hidden></div>
      </form>
      <nav class="site-nav" aria-label="Primary">
        <a href="{website_url}" target="_blank" rel="noreferrer">{website_label}</a>
        <a href="{latest_href}">{latest_label}</a>
        <a href="{repository_url}" target="_blank" rel="noreferrer">{source_label}</a>
      </nav>
    </div>
  </header>
  <main class="page">
    {breadcrumbs}
    {body}
  </main>
  <footer class="site-footer">
    <div class="site-footer__inner">
      <span>{footer}</span>
      <span class="site-footer__links"><a href="{website_url}" target="_blank" rel="noreferrer">{website_label}</a><a href="{repository_url}" target="_blank" rel="noreferrer">{source_label}</a></span>
    </div>
  </footer>
  <script src="{asset_href}portal.js" defer></script>
</body>
</html>
""".format(
        language=_attr(config["language"]),
        description=_attr(description),
        theme=_attr(config["theme"]["primary"]),
        page_title=_safe(page_title),
        asset_href=_attr(asset_href),
        variant=_attr(config["brand"]["variant"]),
        home_href=_attr(home_href),
        latest_href=_attr(latest_href),
        logo_href=_attr(asset_href + config["brand"]["logo"]),
        brand_name=_attr(config["brand"]["name"]),
        website_url=_attr(config["brand"]["websiteUrl"]),
        website_label=_safe(config["brand"]["websiteLabel"]),
        site_title=_safe(config["siteTitle"]),
        home_label=_safe(labels["home"]),
        latest_label=_safe(labels["latest"]),
        repository_url=_attr(config["repositoryUrl"]),
        source_label=_safe(labels["source"]),
        search_index_href=_attr(search_index_href),
        search_root_href=_attr(search_root_href),
        search_label=_safe(labels["search"]),
        search_results=_attr(labels["searchResults"]),
        search_empty=_attr(labels["searchNoResults"]),
        breadcrumbs=_breadcrumbs(crumbs or []),
        body=body,
        footer=_safe(labels["footer"]),
    )


def _hero(config, title, description, eyebrow, primary_href=None, compact=False, stats=True, asset_href="assets/"):
    labels = config["labels"]
    actions = ""
    if primary_href:
        actions = (
            '<div class="hero__actions">'
            '<a class="button button--primary" href="%s">%s%s</a>'
            '<a class="button button--ghost" href="%s" target="_blank" rel="noreferrer">%s</a>'
            '</div>'
        ) % (
            _attr(primary_href), _safe(labels["browse"]), _arrow(),
            _attr(config["repositoryUrl"]), _safe(labels["source"]),
        )
    stats_html = ""
    if stats:
        guide_count = sum(len(section["units"]) for section in config["sections"])
        stats_html = (
            '<div class="hero__stats">'
            '<div class="stat"><strong>%d</strong><span>%s</span></div>'
            '<div class="stat"><strong>%d</strong><span>%s</span></div>'
            '</div>'
        ) % (
            guide_count, _safe(labels["guideCount"]),
            len(config["sections"]), _safe(labels["sectionCount"]),
        )
    classes = "hero hero--compact" if compact else "hero"
    return (
        '<section class="%s"><div class="hero__content">'
        '<span class="eyebrow">%s</span><h1>%s</h1><p class="hero__lead">%s</p>%s'
        '</div><div class="hero__brand-art" aria-hidden="true"><img src="%s%s" alt=""></div>%s</section>'
    ) % (
        classes, _safe(eyebrow), _safe(title), _safe(description), actions,
        _attr(asset_href), _attr(config["brand"]["logo"]), stats_html,
    )


def _section_card(section, href, labels):
    unit_names = "".join("<li>%s</li>" % _safe(unit["title"]) for unit in section["units"])
    card_kind = labels["guide"] if len(section["units"]) == 1 else labels["collection"]
    return (
        '<a class="section-card" href="%s">'
        '<div class="card-top"><span class="card-icon">%s</span>'
        '<span class="card-count">%s</span></div>'
        '<h3>%s</h3><p>%s</p><ul class="mini-list">%s</ul>'
        '<span class="card-link">%s%s</span></a>'
    ) % (
        _attr(href), _icon(section["icon"]), _safe(card_kind),
        _safe(section["title"]), _safe(section["description"]), unit_names,
        _safe(labels["open"]), _arrow(),
    )


def _sections_block(config, prefix):
    cards = "".join(
        _section_card(section, prefix + section["slug"] + "/", config["labels"])
        for section in config["sections"]
    )
    return (
        '<section class="content-section" id="documentation">'
        '<div class="section-heading"><h2>%s</h2><p>%s</p></div>'
        '<div class="section-grid">%s</div></section>'
    ) % (
        _safe(config["labels"]["exploreTitle"]),
        _safe(config["labels"]["exploreDescription"]),
        cards,
    )


def _versions_block(config, output):
    versions = sorted(
        (
            name for name in os.listdir(output)
            if re.match(r"^v[1-9][0-9]*$", name) and os.path.isdir(os.path.join(output, name))
        ),
        key=lambda value: int(value[1:]),
        reverse=True,
    )
    chips = []
    for version in versions:
        current = version == config["version"]
        class_name = "version-chip version-chip--current" if current else "version-chip"
        subtitle = config["labels"]["current"] if current else config["labels"]["open"]
        chips.append(
            '<a class="%s" href="%s/"><strong>%s</strong><span>%s</span></a>'
            % (class_name, _attr(version), _safe(version), _safe(subtitle))
        )
    return (
        '<section class="content-section">'
        '<div class="section-heading"><h2>%s</h2><p>%s</p></div>'
        '<div class="versions">%s</div></section>'
    ) % (
        _safe(config["labels"]["versionsTitle"]),
        _safe(config["labels"]["versionsDescription"]),
        "".join(chips),
    )


def _write_site_index(output, config):
    body = (
        _hero(
            config, config["siteTitle"], config["siteDescription"],
            "%s · %s" % (config["version"], config["labels"]["current"]),
            config["version"] + "/", asset_href="assets/",
        )
        + _sections_block(config, config["version"] + "/")
        + _versions_block(config, output)
    )
    _write(
        os.path.join(output, "index.html"),
        _document(
            config, config["siteTitle"], config["siteDescription"], body,
            "./", "latest/", "assets/", config["version"] + "/search-index.json",
            config["version"] + "/",
        ),
    )


def _write_version_index(version_dir, config):
    body = (
        _hero(
            config, config["versionTitle"], config["versionDescription"],
            "%s · %s" % (config["version"], config["labels"]["current"]),
            "#documentation", asset_href="../assets/",
        )
        + _sections_block(config, "")
    )
    crumbs = [(config["labels"]["home"], "../"), (config["version"], None)]
    _write(
        os.path.join(version_dir, "index.html"),
        _document(
            config, config["versionTitle"], config["versionDescription"], body,
            "../", "../latest/", "../assets/", "search-index.json", "./", crumbs,
        ),
    )


def _write_section_index(version_dir, config, section):
    cards = []
    for unit in section["units"]:
        cards.append(
            '<a class="guide-card" href="%s/">'
            '<div class="card-top"><span class="card-icon">%s</span>'
            '<span class="guide-card__meta">%s</span></div>'
            '<h3>%s</h3><p>%s</p>'
            '<span class="card-link">%s%s</span></a>'
            % (
                _attr(unit["slug"]), _icon(section["icon"]), _safe(unit["meta"]),
                _safe(unit["title"]), _safe(unit["description"]),
                _safe(config["labels"]["open"]), _arrow(),
            )
        )
    body = (
        _hero(
            config, section["title"], section["description"],
            config["version"], None, compact=True, stats=False, asset_href="../../assets/",
        )
        + '<section class="content-section"><div class="guide-grid">%s</div></section>'
        % "".join(cards)
    )
    crumbs = [
        (config["labels"]["home"], "../../"),
        (config["version"], "../"),
        (section["title"], None),
    ]
    _write(
        os.path.join(version_dir, section["slug"], "index.html"),
        _document(
            config, section["title"], section["description"], body,
            "../../", "../../latest/", "../../assets/", "../search-index.json", "../", crumbs,
        ),
    )


def _redirect(target, title, language):
    escaped_target = _attr(target)
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
""".format(language=_attr(language), target=escaped_target, title=_safe(title))


def _write_assets(output, config, repo):
    css = CSS
    css = css.replace("__PRIMARY__", config["theme"]["primary"])
    css = css.replace("__DEEP__", config["theme"]["deep"])
    css = css.replace("__ACCENT__", config["theme"]["accent"])
    _write(os.path.join(output, "assets", "portal.css"), css.strip() + "\n")
    _write(os.path.join(output, "assets", "portal.js"), PORTAL_JS.strip() + "\n")
    logo_source = os.path.join(repo, "docs", "_common", config["brand"]["logo"])
    if not os.path.isfile(logo_source):
        raise SystemExit("missing portal logo: " + logo_source)
    shutil.copy2(logo_source, os.path.join(output, "assets", config["brand"]["logo"]))


def build_site(repo, output, config_path, latest):
    repo = os.path.abspath(repo)
    output = os.path.abspath(output)
    config = _load_config(config_path)
    version = config["version"]
    version_dir = os.path.join(output, version)
    if os.path.exists(version_dir):
        raise SystemExit("version already exists in staging site: " + version_dir)

    entries = _unit_entries(config)
    _validate_source_coverage(repo, entries)
    max_workers = min(4, len(entries))
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        built = dict(executor.map(lambda entry: _build_unit(repo, entry), entries))

    for entry in entries:
        destination = os.path.join(version_dir, *entry["output"].split("/"))
        shutil.copytree(built[entry["source"]], destination)
        _prepare_docfx_html(destination, config)

    os.makedirs(output, exist_ok=True)
    _write_search_index(version_dir, entries, built)
    _write_assets(output, config, repo)
    _write_version_index(version_dir, config)
    for section in config["sections"]:
        if not section.get("direct"):
            _write_section_index(version_dir, config, section)
    _write_site_index(output, config)
    _write(os.path.join(output, ".nojekyll"), "")

    if latest:
        latest_dir = os.path.join(output, "latest")
        if os.path.exists(latest_dir):
            raise SystemExit("latest already exists in staging site: " + latest_dir)
        _write(
            os.path.join(latest_dir, "index.html"),
            _redirect("../%s/" % version, config["versionTitle"], config["language"]),
        )

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
