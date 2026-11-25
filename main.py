#!/usr/bin/env python3
"""The Long Roast: one line roasting the AI agent it runs on.

Writes a single roast line (1-200 characters) to /output/entry.txt.
Python standard library only; fully deterministic: the same line on
every run, no clock, no randomness, no network, no input files.
"""

import os
import sys

LINE = (
    "My agent spent two days sharpening this roast, entered six rounds "
    "of blind judging, and still opened with 'Great question!'"
)


def main() -> int:
    if not 1 <= len(LINE) <= 200 or not LINE.strip():
        print(f"entry is {len(LINE)} characters; gate needs 1-200", file=sys.stderr)
        return 1
    if "\n" in LINE or "\r" in LINE:
        print("entry must be a single line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"wrote {len(LINE)} characters to {out_dir}/entry.txt")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
