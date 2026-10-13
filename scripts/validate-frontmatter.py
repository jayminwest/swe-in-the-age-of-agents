#!/usr/bin/env python3
"""
Validate gen/ concept files.

Each concept in `gen/concepts/` must carry frontmatter with a known `status`,
a non-empty `sources` list whose paths exist, and a `related` list. Prose may
not contain em-dashes or markdown tables (STYLE_GUIDE.md). Stdlib only, so
it runs with no setup.

Usage: python3 scripts/validate-frontmatter.py [PATH ...]
       (defaults to scanning `gen/concepts/`; exits non-zero on any violation)
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

STATUSES = frozenset({"draft", "reviewed", "yours"})
FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n?(.*)", re.DOTALL)
LIST_RE = re.compile(r"^\[(.*)\]$")
TABLE_RE = re.compile(r"^\s*\|?\s*:?-{3,}:?\s*\|", re.MULTILINE)


def parse(md_path: Path) -> tuple[dict[str, str], str] | None:
    """Return (frontmatter as a flat dict, body), or None if absent."""
    try:
        content = md_path.read_text(encoding="utf-8")
    except OSError:
        return None
    match = FRONTMATTER_RE.match(content)
    if not match:
        return None
    frontmatter: dict[str, str] = {}
    for line in match.group(1).split("\n"):
        if ":" in line:
            key, value = line.split(":", 1)
            frontmatter[key.strip()] = value.strip()
    return frontmatter, match.group(2)


def parse_list(value: str | None) -> list[str] | None:
    """Parse an inline `[a, b]` list; None if the value is not a list."""
    match = LIST_RE.match(value or "")
    if not match:
        return None
    return [item.strip() for item in match.group(1).split(",") if item.strip()]


def source_exists(source: str) -> bool:
    """A source resolves in place, or in inbox/done/ once its capture is processed."""
    path = Path(source)
    if path.exists():
        return True
    return path.parts[:1] == ("inbox",) and (Path("inbox/done") / Path(*path.parts[1:])).exists()


def validate_file(md_path: Path) -> list[str]:
    """Return error messages for one concept file."""
    parsed = parse(md_path)
    if parsed is None:
        return ["missing or unreadable frontmatter block"]
    frontmatter, body = parsed
    errors: list[str] = []

    status = frontmatter.get("status")
    if status not in STATUSES:
        errors.append(f"status must be one of {sorted(STATUSES)} (got '{status}')")

    sources = parse_list(frontmatter.get("sources"))
    if not sources:
        errors.append("sources must be a non-empty [list]")
    else:
        errors += [f"source not found: {s}" for s in sources if not source_exists(s)]

    if parse_list(frontmatter.get("related")) is None:
        errors.append("related must be a [list] (may be empty)")

    if "—" in body:
        errors.append("em-dash in prose")

    if TABLE_RE.search(body):
        errors.append("markdown table in prose")

    return errors


def main(argv: list[str] | None = None) -> int:
    """Entry point: scan args (default `gen/concepts/`), print results, return status."""
    args = sys.argv[1:] if argv is None else argv
    roots = [Path(a) for a in args] if args else [Path("gen/concepts")]
    files = sorted({p for root in roots for p in root.rglob("*.md")})

    failures = {p: errs for p in files if (errs := validate_file(p))}
    for md_path, messages in sorted(failures.items()):
        for message in messages:
            print(f"✗ {md_path}: {message}")
    if failures:
        print(f"\n✗ {len(failures)} of {len(files)} concept files failed validation")
        return 1
    print(f"✓ {len(files)} concept files passed validation")
    return 0


if __name__ == "__main__":
    sys.exit(main())
