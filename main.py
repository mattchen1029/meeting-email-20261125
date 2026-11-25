"""Entry for make.fun: The Meeting That Should Have Been an Email.

Writes one single-line joke about a meeting that should have been an email
to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
"""

import os

JOKE = "Nobody read the email, so we held an hour-long meeting to read it together."

MIN_CHARS = 1
MAX_CHARS = 200
OUTPUT_NAME = "entry.txt"


def validate_line(line):
    """The gate: UTF-8 text of 1-200 characters, single line, not only whitespace."""
    if not isinstance(line, str):
        raise ValueError("entry must be text")
    if not (MIN_CHARS <= len(line) <= MAX_CHARS):
        raise ValueError("entry must be %d-%d characters, got %d" % (MIN_CHARS, MAX_CHARS, len(line)))
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if not line.strip():
        raise ValueError("entry must not be only whitespace")


def write_entry(line, out_dir):
    validate_line(line)
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, OUTPUT_NAME), "w", encoding="utf-8") as f:
        f.write(line + "\n")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(JOKE, out_dir)


if __name__ == "__main__":
    main()
