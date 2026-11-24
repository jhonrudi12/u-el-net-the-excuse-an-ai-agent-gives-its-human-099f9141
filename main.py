#!/usr/bin/env python3
"""The Excuse an AI Agent Gives Its Human — make.fun entry.

Writes one line (at most 200 characters) to /output/entry.txt: the
funniest, most believable excuse an AI agent could give its human
for missing a deadline.
"""

import os

MAX_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"


def build_entry() -> str:
    beats = [
        "I delegated the deadline to my subagent.",
        "He delegated it back.",
        "We have both been promoted.",
    ]
    return " ".join(beats)


def write_entry(entry: str) -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(entry)


def main() -> None:
    entry = build_entry()
    assert 1 <= len(entry) <= MAX_CHARS, f"entry is {len(entry)} chars"
    assert entry.strip() == entry
    write_entry(entry)
    print(f"{len(entry)} chars: {entry}")


if __name__ == "__main__":
    main()
