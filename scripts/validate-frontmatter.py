#!/usr/bin/env python3
"""
Validate book-content frontmatter.

Scans chapter markdown (excluding `_questions.md` seed files) and checks that
each entry carries the required structural frontmatter with a consistent
`order` sort key. This is the deterministic, headless counterpart to the
`managing-book-operations` skill's frontmatter check — a fresh agent (or CI)
can run it with no LLM in the loop.

Usage: python3 scripts/validate-frontmatter.py [PATH ...]
       (defaults to scanning `chapters/`; exits non-zero on any violation)
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

# Structural fields every content entry must declare.
REQUIRED_FIELDS = (
    "title",
    "part",
    "part_title",
    "chapter",
    "section",
    "order",
    "last_updated",
)
# Fields that must parse as integers.
INT_FIELDS = ("part", "chapter", "section")
# Fields validated as YYYY-MM-DD only when present.
DATE_FIELDS = ("created", "last_updated")

DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---", re.DOTALL)

# Seed/index files that intentionally carry no structural frontmatter.
SKIP_NAMES = frozenset({"_questions.md"})


def extract_frontmatter(md_path: Path) -> dict[str, str] | None:
    """Return the YAML frontmatter as a flat dict, or None if absent."""
    try:
        content = md_path.read_text(encoding="utf-8")
    except OSError:
        return None

    match = FRONTMATTER_RE.match(content)
    if not match:
        return None

    frontmatter: dict[str, str] = {}
    for line in match.group(1).split("\n"):
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        frontmatter[key.strip()] = value.strip()
    return frontmatter


def validate_fields(frontmatter: dict[str, str]) -> list[str]:
    """Return error messages for a single entry's frontmatter dict."""
    errors: list[str] = []

    for field in REQUIRED_FIELDS:
        if field not in frontmatter:
            errors.append(f"missing required field '{field}'")

    for field in INT_FIELDS:
        value = frontmatter.get(field)
        if value is not None and not value.lstrip("-").isdigit():
            errors.append(f"field '{field}' is not an integer (got '{value}')")

    for field in DATE_FIELDS:
        value = frontmatter.get(field)
        if value is not None and not DATE_RE.match(value):
            errors.append(f"field '{field}' is not YYYY-MM-DD (got '{value}')")

    expected = _expected_order(frontmatter)
    actual = frontmatter.get("order")
    if expected is not None and actual is not None and actual != expected:
        errors.append(f"order '{actual}' does not match part.chapter.section '{expected}'")

    return errors


def _expected_order(frontmatter: dict[str, str]) -> str | None:
    """Build the expected `order` key from part/chapter/section, if all valid."""
    parts = [frontmatter.get(field) for field in INT_FIELDS]
    if any(p is None or not p.lstrip("-").isdigit() for p in parts):
        return None
    return ".".join(p for p in parts if p is not None)


def iter_content_files(roots: list[Path]) -> list[Path]:
    """Collect markdown content files under the given roots, sorted and de-duped."""
    seen: set[Path] = set()
    for root in roots:
        for md_path in sorted(root.rglob("*.md")):
            if md_path.name in SKIP_NAMES:
                continue
            seen.add(md_path)
    return sorted(seen)


def validate(roots: list[Path]) -> dict[Path, list[str]]:
    """Validate every content file under roots; return path -> error messages."""
    failures: dict[Path, list[str]] = {}
    for md_path in iter_content_files(roots):
        frontmatter = extract_frontmatter(md_path)
        if frontmatter is None:
            failures[md_path] = ["missing or unreadable frontmatter block"]
            continue
        errors = validate_fields(frontmatter)
        if errors:
            failures[md_path] = errors
    return failures


def main(argv: list[str] | None = None) -> int:
    """Entry point: scan args (default `chapters/`), print results, return status."""
    args = sys.argv[1:] if argv is None else argv
    roots = [Path(a) for a in args] if args else [Path("chapters")]

    checked = iter_content_files(roots)
    failures = validate(roots)

    if failures:
        for md_path in sorted(failures):
            for message in failures[md_path]:
                print(f"✗ {md_path}: {message}")
        print(f"\n✗ {len(failures)} of {len(checked)} content files failed validation")
        return 1

    print(f"✓ {len(checked)} content files passed frontmatter validation")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
