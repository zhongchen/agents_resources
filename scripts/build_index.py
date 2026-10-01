#!/usr/bin/env python3
"""Regenerate INDEX.md from entry frontmatter. Deterministic and idempotent.

Run after any change under entries/ and commit the result with your entry.
Do not hand-edit INDEX.md. CI (validate_entries.py) fails the PR if it is
out of date.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from validate_entries import generate_index_text  # noqa: E402


def main():
    text = generate_index_text()
    Path("INDEX.md").write_text(text, encoding="utf-8")
    entry_count = text.count("](entries/")
    print(f"Wrote INDEX.md with {entry_count} entries.")


if __name__ == "__main__":
    main()
