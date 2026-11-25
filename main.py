#!/usr/bin/env python3
"""Dog Ate My Homework -- angle 2: payback, not hunger.

Angle: the dog is not apologising for eating the homework out of
hunger, and this is not the flat literal "the dog ate my homework"
line. The mechanism is revenge with dog logic: the homework ate
the dog's dinner first, so the dog simply returned the favour.
A dog who believes it has done nothing wrong, in one line.
"""

import os

LINE = "The homework ate my dinner first -- I was only returning the favour."

MAX_CHARS = 200


def validate(line):
    """Gate mirror: one line, 1-200 chars, not only whitespace."""
    text = line.strip()
    if not text:
        raise SystemExit("excuse line is empty")
    if len(text) > MAX_CHARS:
        raise SystemExit("excuse line exceeds 200 characters")
    if "\n" in text or "\r" in text:
        raise SystemExit("excuse line must be a single line")
    return text


def output_path():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(out_dir, "entry.txt")


def main():
    line = validate(LINE)
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "wb") as handle:
        handle.write(line.encode("utf-8"))
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
