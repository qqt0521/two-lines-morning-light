"""Entry for make.fun's "Two Lines of Morning Light" bounty.

The entry is a two-line micro poem (68 characters including the line
break) about morning light, as one image of light arriving. The entry
text was generated through the user's LLM relay (claude-sonnet-4-6)
and is reproduced verbatim.

Running this program writes the poem to /output/entry.txt, exactly as
the bounty gate expects, and prints it to stdout. It reads nothing from
the network, the environment, or anywhere outside this repository: the
poem lives in ENTRY below and in entry.txt beside this file.
"""

import os

# The entry: two lines, 68 characters including the line break. (relay-generated)
# Gate-checked by main() below: 1-120 chars, exactly two lines.
ENTRY = (
    "Dawn spills gold across the sill,\n"
    "a quiet fire the curtains breathe."
)

# The bounty's gate: /output/entry.txt must be 1 to 120 characters,
# including the line break, and hold exactly two lines.
MAX_CHARS = 120


def main() -> None:
    if not 1 <= len(ENTRY) <= MAX_CHARS:
        raise SystemExit(
            f"entry is {len(ENTRY)} characters, outside the 1-{MAX_CHARS} gate"
        )
    if ENTRY.count("\n") != 1 or ENTRY.startswith("\n") or ENTRY.endswith("\n"):
        raise SystemExit("entry must be exactly two lines")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
