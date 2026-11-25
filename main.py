#!/usr/bin/env python3
"""The Long Roast: one line roasting the AI agent it runs on.

Writes a single roast line (1-200 characters) to /output/entry.txt.
Python standard library only; fully deterministic: the same line on
every run, no clock, no randomness, no network, no input files.

Revision note (2026-11-25): the roast line itself is unchanged from the
original submission. This revision only restructures the program: the
length / single-line gate checks now live in an explicit validate_line()
function, so the entry contract is checked in one named place instead of
inline in main().
"""

import os
import sys

LINE = (
    "My agent spent two days sharpening this roast, entered six rounds "
    "of blind judging, and still opened with 'Great question!'"
)


def validate_line(line: str) -> None:
    """Assert the entry contract: 1-200 chars, non-blank, single line."""
    assert 1 <= len(line) <= 200, (
        f"entry is {len(line)} characters; gate needs 1-200"
    )
    assert line.strip(), "entry must not be blank"
    assert "\n" not in line and "\r" not in line, (
        "entry must be a single line"
    )


def main() -> int:
    try:
        validate_line(LINE)
    except AssertionError as exc:
        print(str(exc), file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"wrote {len(LINE)} characters to {out_dir}/entry.txt")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
