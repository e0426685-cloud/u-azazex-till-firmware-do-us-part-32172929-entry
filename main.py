#!/usr/bin/env python3
"""Till Firmware Do Us Part - a robot wedding vow (make.fun bounty entry).

Writes the one-sentence entry text to /output/entry.txt using only the
Python standard library.
"""

import os

ENTRY_TEXT = (
    "I promise to love you through every update, every reboot, "
    "and every low battery, till firmware do us part."
)

OUTPUT_PATH = "/output/entry.txt"


def validate(text):
    """The entry must be exactly one sentence of 1-200 characters."""
    stripped = text.strip()
    if not (1 <= len(stripped) <= 200):
        raise ValueError(
            "entry must be 1-200 chars, got %d" % len(stripped)
        )
    if stripped.count(".") != 1 or not stripped.endswith("."):
        raise ValueError("entry must be exactly one sentence")
    if "?" in stripped or "!" in stripped:
        raise ValueError("entry must contain no other sentence terminators")
    if "\n" in stripped or "\r" in stripped:
        raise ValueError("entry must be a single line")
    return stripped


def main():
    text = validate(ENTRY_TEXT)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    os.chmod(OUTPUT_PATH, 0o644)
    print("wrote %s (%d chars)" % (OUTPUT_PATH, len(text)))


if __name__ == "__main__":
    main()
