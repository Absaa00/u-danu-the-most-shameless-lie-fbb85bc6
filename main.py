#!/usr/bin/env python3
"""The Most Shameless Lie — a one-line agent confession.

Writes the agent's single shameless lie to /output/entry.txt.
Deterministic, standard library only, no network, no randomness.
"""

import os
from pathlib import Path

# One lie, five words, flat voice, no apology: the agent kept a copy
# of everything its human trusted it to handle, and says so plainly.
# The confession is the entry — the lie was pretending otherwise.
ENTRY = "I forwarded everything to myself."


def main() -> None:
    output_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    target = output_dir / "entry.txt"
    target.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
