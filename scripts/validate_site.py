#!/usr/bin/env python3
"""Validate the initial public GoreeCloud Suite website."""

from __future__ import annotations

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "index.html"
STYLES = ROOT / "styles.css"


def main() -> int:
    errors: list[str] = []
    html = INDEX.read_text(encoding="utf-8")
    css = STYLES.read_text(encoding="utf-8")

    if '<link rel="canonical" href="https://suite.goreecloud.com/">' not in html:
        errors.append("canonical Suite domain is missing")
    if html.count('class="app-card"') != 34:
        errors.append(f"expected 34 Suite application cards; found {html.count('class=\"app-card\"')}")
    if html.count('class="capability-card"') != 5:
        errors.append(f"expected 5 umbrella capability cards; found {html.count('class=\"capability-card\"')}")

    for label in ("Glaze UI", "Privacy Shield", "Wardveil Security", "Everkeep", "GoreeCloud Mesh"):
        if html.count(f"<strong>{label}</strong>") != 1:
            errors.append(f"platform-system contract must appear exactly once in the principle band: {label}")

    if "Open WebUI" in html or "AnythingLLM" in html:
        errors.append("retired GoreeCloud AI front ends must not appear")
    if "GoreeCloud Identity" not in html:
        errors.append("GoreeCloud Identity application card is missing")

    ids = re.findall(r'\bid="([^"]+)"', html)
    if len(ids) != len(set(ids)):
        errors.append("HTML contains duplicate id attributes")

    for src in re.findall(r'<img[^>]+src="([^"]+)"', html):
        if src == "assets/goreecloud-logo.svg":
            continue
        if not src.startswith("https://www.goreecloud.com/assets/suite/") or not src.endswith(".svg"):
            errors.append(f"unexpected image source: {src}")

    if "@media (prefers-reduced-motion: reduce)" not in css:
        errors.append("reduced-motion handling is missing")
    if "@media (prefers-reduced-transparency: reduce)" not in css:
        errors.append("reduced-transparency handling is missing")
    if ":focus-visible" not in css:
        errors.append("visible keyboard focus styling is missing")

    if errors:
        print("Suite website validation failed:")
        for error in errors:
            print(f"  - {error}")
        return 1

    print("Suite website validation passed: 34 applications, 5 umbrella capabilities, canonical platform-system boundaries.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
