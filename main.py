# SPDX-License-Identifier: MIT
"""Make the AI judge feel curious.

Writes one short text to /output/entry.txt: a quiet, concrete image in the
second person, with a question that keeps working after the last line.
Deterministic: the same text on every run, no network, no randomness.
"""

import os

TEXT = (
    "You have lived in this house for years, and only tonight noticed the "
    "door at the end of the hall \u2014 painted the same colour as the "
    "wall, with no handle and no keyhole. Your hand is raised. When did "
    "you stop asking what is behind it, and why did it wait until tonight "
    "to be seen."
)


def main() -> None:
    output_dir = "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(TEXT)


if __name__ == "__main__":
    main()
