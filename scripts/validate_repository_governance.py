#!/usr/bin/env python3
"""Validate mandatory GoreeCloud Suite repository-governance records."""

from __future__ import annotations

from pathlib import Path
import sys

from build_public_site import PUBLIC_FILES

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_RECORDS = {
    "README.md": "# GoreeCloud Suite",
    "SPECIFICATIONS.md": "# GoreeCloud Suite — Repository Specifications",
    "FEATURES.md": "# GoreeCloud Suite — Features",
    "BENEFITS.md": "# GoreeCloud Suite — Benefits",
    "COMPETITIVE-OBJECTIVES.md": "# GoreeCloud Suite — Competitive Objectives",
    "BRANDING.md": "# GoreeCloud Suite Branding",
}

LICENSE_CANDIDATES = (
    "LICENSE",
    "LICENSE.md",
    "LICENSE.txt",
    "COPYING",
    "COPYING.md",
    "COPYING.txt",
)


def main() -> int:
    errors: list[str] = []
    public_files = set(PUBLIC_FILES)

    for relative, expected_heading in REQUIRED_RECORDS.items():
        path = ROOT / relative
        if not path.is_file() or path.is_symlink():
            errors.append(f"mandatory root governance record is missing or invalid: {relative}")
            continue

        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            errors.append(f"mandatory root governance record is not readable UTF-8: {relative}: {exc.__class__.__name__}")
            continue

        first_line = text.splitlines()[0] if text.splitlines() else ""
        if first_line != expected_heading:
            errors.append(
                f"mandatory root governance record has unexpected identity heading: {relative}; "
                f"expected {expected_heading!r}"
            )
        if len(text.strip()) < len(expected_heading) + 20:
            errors.append(f"mandatory root governance record is unexpectedly empty or skeletal: {relative}")
        if relative in public_files:
            errors.append(f"repository governance record must not be part of the public Suite artifact allowlist: {relative}")

    license_present = next((name for name in LICENSE_CANDIDATES if (ROOT / name).is_file()), None)

    if errors:
        print("Suite repository governance validation failed:")
        for error in errors:
            print(f"  - {error}")
        return 1

    print(
        "Suite repository governance validation passed: all six mandatory root records are present, "
        "identified, non-symlink files and remain outside the public artifact allowlist."
    )
    if license_present:
        print(f"Repository license material detected at {license_present}; license correctness remains a separate governed review.")
    else:
        print("Repository license remains unresolved; no license is inferred or asserted by this validator.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
