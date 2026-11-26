"""makefun-quiet-dread: write a one-line code review comment to /output/entry.txt.

The comment approves a pull request while carrying quiet existential
dread: flat, understated, the way a tired engineer actually writes
before clicking Approve.

Deterministic: every run writes exactly the same bytes. Standard
library only; no network, no randomness, no files read from disk.
"""

import os

COMMENT = (
    "Approved. Green CI, tidy diff. "
    "Whatever this breaks, it will break quietly, "
    "like everything else around here."
)

OUTPUT_DIR = "/output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "entry.txt")


def main():
    assert "\n" not in COMMENT, "entry must be a single line"
    assert 1 <= len(COMMENT) <= 140, "entry must be 1 to 140 characters"
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    # Clear the output directory's contents, never the directory itself.
    for name in os.listdir(OUTPUT_DIR):
        path = os.path.join(OUTPUT_DIR, name)
        if os.path.isfile(path) or os.path.islink(path):
            os.remove(path)
    with open(OUTPUT_FILE, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(COMMENT)


if __name__ == "__main__":
    main()
