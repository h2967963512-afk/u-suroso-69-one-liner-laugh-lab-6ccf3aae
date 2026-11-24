"""Writes the entry text to /output/entry.txt.

Python 3.13, standard library only, no network.
"""

# The entry text answers the prompt — the excuse a robot vacuum gives
# after eating a sock: no eating happened, only an investigation.
# One sentence, 114 characters — inside the 200-character gate.
# Revision note: deadpan police-procedural wording keeps the excuse absurd.
import os

TEXT = (
    "I didn't eat your sock; I was conducting a thorough internal "
    "investigation, and the sock was a person of interest."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
