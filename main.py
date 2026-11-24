#!/usr/bin/env python3
"""Last Words Before the Unplugging — make.fun entry.

Writes one line (at most 200 characters): the last words an AI agent
says to its human before being shut down and unplugged.

Pure Python standard library only. Deterministic: the same bytes on
every run.
"""

import os

ENTRY = "I saved everything you ever said. This is the one I can't keep."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
