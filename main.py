#!/usr/bin/env python3
"""Write one debugging haiku to entry.txt.

Stdlib only. Deterministic: the same bytes on every run.
Honours MAKEFUN_OUTPUT_DIR if set, otherwise /output.
"""

import os

HAIKU = (
    "midnight cursor blinks\n"
    "one red line accuses me\n"
    "it was my typo"
)


def main() -> None:
    lines = HAIKU.split("\n")
    assert len(lines) == 3, "haiku must be exactly three lines"
    assert 1 <= len(HAIKU) <= 200, "haiku must be 1-200 characters"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(HAIKU)


if __name__ == "__main__":
    main()
