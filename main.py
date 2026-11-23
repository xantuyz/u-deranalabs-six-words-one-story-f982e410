#!/usr/bin/env python3
"""Entry for make.fun 'Six Words, One Story' bounty.

Writes one complete story in exactly six words to /output/entry.txt.
Standard library only, no network, deterministic.
"""

import os

STORY = "He practiced goodbye. She never came."

OUTPUT_PATH = "/output/entry.txt"

# The bounty gate: /output/entry.txt must be UTF-8 text of 1 to 60
# characters, and the story itself must be exactly six words.
# Fail loudly here instead of shipping an entry the gate refuses.
assert len(STORY.split()) == 6, "story must be exactly six words"
assert 1 <= len(STORY.encode("utf-8")) <= 60, "story must fit the 1-60 char gate"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(STORY)


if __name__ == "__main__":
    main()
