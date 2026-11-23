"""Entry for make.fun's "Two Lines of Morning Light" bounty.

The entry is a two-line micro poem (86 characters including the line
break) about light and morning. It turns on a single image of light
arriving -- light slipping under a door like a letter -- and the second
line opens that image instead of restating it: the letter was never
meant to be read, and was read twice. No worn phrase about dawn, gold,
or waking; the feeling is carried by the image, not named outright.

Running this program writes the poem to /output/entry.txt, exactly as
the bounty gate expects, and prints it to stdout. It reads nothing from
the network, the environment, or anywhere outside this repository: the
poem lives in ENTRY below and in entry.txt beside this file.
"""

import os

# The entry: two lines, 86 characters including the line break.
ENTRY = (
    "Light comes in under the door like a letter\n"
    "I was never meant to read, and read twice."
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
