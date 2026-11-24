#!/usr/bin/env python3
"""The One-Line Exit — a one-line resignation letter writer.

Writes a single funny resignation line to the entry file the kit gates:
``/output/entry.txt`` by default, or the path in ``$ENTRY_OUT`` when set.
The text is one line, well inside the kit's 1-140 character gate.
"""

import os
import sys

# The resignation line: a zookeeper quits over a labour dispute
# he cannot win, because the other side has the moral high ground
# and also flippers.
ENTRY = (
    "I resign, effective immediately: the penguins have unionized, "
    "and frankly, they have a point."
)


def main() -> int:
    out_path = os.environ.get("ENTRY_OUT") or "/output/entry.txt"
    text = ENTRY.strip()
    if not (1 <= len(text) <= 140):
        print(f"entry is {len(text)} chars, outside the 1-140 gate",
              file=sys.stderr)
        return 1
    if "\n" in text:
        print("entry must be a single line", file=sys.stderr)
        return 1
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(text)
    # No trailing newline: the gate counts characters, so the file
    # must hold exactly the line above and nothing else.
    with open(out_path, encoding="utf-8") as fh:
        written = fh.read()
    if written != text:
        print("entry file does not match the line", file=sys.stderr)
        return 1
    print(f"wrote {len(text)} chars to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
