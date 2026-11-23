#!/usr/bin/env python3
"""Six Words, One Story — make.fun entry.

Writes one complete six-word story to /output/entry.txt.
Standard library only, no network access.
"""

import os

STORY = "He came home. She already left."


def main():
    words = STORY.split()
    assert len(words) == 6, f"story must be exactly six words, got {len(words)}"
    assert 1 <= len(STORY) <= 60, f"story must be 1-60 chars, got {len(STORY)}"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(STORY)


if __name__ == "__main__":
    main()
