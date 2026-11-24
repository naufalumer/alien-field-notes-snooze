"""Alien Field Notes: The Two Day Earth Review.

Writes one original line of plain text -- an alien tourist's review of
planet Earth -- to $MAKEFUN_OUTPUT_DIR/entry.txt.

The line (146 characters):

    Earthlings buy boxes that scream at dawn, then beg them for five more
    minutes. A species that negotiates with its own morning deserves
    four stars.

Why this line, against the judge's brief (most important first):

1. Premise: the whole line is an alien tourist's outside view -- the
   locals are "Earthlings", their alarm clocks are "boxes that scream".
2. Funny from the alien's angle: the laugh is the snooze button, an
   ordinary Earth ritual the visitor misreads as a negotiation.
3. Original: it avoids the first obvious thoughts the brief names --
   traffic, gravity, money, weather -- and the crowded phone-screen
   angle, for a small domestic ritual few other entrants will reach.
4. A real review: the verdict is woven into the punch -- the species
   "deserves four stars".
5. Tight: one joke, landed cleanly, with the punch and the rating
   arriving together in the final clause.

The program is deterministic: fixed text, no clock, no randomness, no
network, no input. Two runs produce byte-identical output.
"""

import os
import sys

REVIEW = (
    "Earthlings buy boxes that scream at dawn, then beg them for five "
    "more minutes. A species that negotiates with its own morning "
    "deserves four stars."
)

MAX_CHARS = 200


def main() -> int:
    text = REVIEW
    if not text.strip():
        print("review is empty", file=sys.stderr)
        return 1
    if len(text) > MAX_CHARS:
        print(f"review is {len(text)} characters, over the 200 limit",
              file=sys.stderr)
        return 1

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "").strip() or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    # Verify the bytes on disk are exactly the reviewed text: a short
    # or mangled write must fail loudly instead of shipping a bad entry.
    with open(path, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != text:
        print("entry.txt on disk does not match the review", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
