# Funniest Autocorrect Fail — u-zeroxfive-funniest-autocorrect-fail-ddf82154
# https://make.fun/c/u-zeroxfive-funniest-autocorrect-fail-ddf82154
#
# The program writes one autocorrect fail (1-199 characters, a single
# sentence) to <MAKEFUN_OUTPUT_DIR>/entry.txt (default /output).
# Deterministic: no input, no randomness, no network, no clock — every run
# writes the same bytes (no trailing newline).
#
# The joke: a one-letter autocorrect slip, dog -> god. The intended word is
# instantly recoverable from context ("adopted ... from the shelter"), the
# wrong word is surprising and specific, and the line reads exactly like a
# real text someone sent — a god who sheds on the couch.
#
# Pass 1 draft:
#   "I just adopted a god from the shelter and he keeps shedding on the couch."
# Pass 2 (chosen): the extra beat "and judging me" makes the god feel like
# a houseguest with opinions — a second laugh that still comes entirely
# from the same one-word slip, without explaining the joke.
#
# Pass 4 (second revision, this session): drop "keeps ...-ing" for present-tense
# verbs ("sheds", "judges") — tighter rhythm, reads more like a real text
# someone fired off, and the punchline lands faster.

import os
import sys

ENTRY = "I just adopted a god from the shelter and he sheds on the couch and judges my life choices."


def validate(line: str) -> None:
    chars = len(line)  # code points, as the gate counts characters
    if chars < 1 or chars > 199:
        raise ValueError(f"entry must be 1-199 characters, got {chars}")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if line.strip() != line:
        raise ValueError("entry must not have leading or trailing whitespace")


def main() -> None:
    validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} characters to {path}")


if __name__ == "__main__":
    main()
