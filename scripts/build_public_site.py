#!/usr/bin/env python3
"""Build the explicit public artifact for suite.goreecloud.com."""

from __future__ import annotations

from pathlib import Path
import shutil
import sys

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
PUBLIC_FILES = (
    "index.html",
    "styles.css",
    "_headers",
    "robots.txt",
    "sitemap.xml",
    "site.webmanifest",
    "assets/goreecloud-logo.svg",
)


def main() -> int:
    try:
        if len(PUBLIC_FILES) != len(set(PUBLIC_FILES)):
            raise ValueError("public allowlist contains duplicate paths")
        if DIST.exists():
            if DIST.is_symlink():
                raise ValueError("dist must not be a symlink")
            shutil.rmtree(DIST)
        DIST.mkdir()
        for relative in PUBLIC_FILES:
            source = ROOT / relative
            if not source.is_file() or source.is_symlink():
                raise ValueError(f"invalid public source: {relative}")
            target = DIST / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, target)
    except (OSError, ValueError) as exc:
        print(f"Suite website build failed: {exc}")
        return 1

    files = [path for path in DIST.rglob("*") if path.is_file()]
    print(f"Built Suite website artifact: {len(files)} files, {sum(path.stat().st_size for path in files)} bytes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
