# Two lines for make.fun, about morning light.
# A two-line poem, 68 characters including the line break, as one image
# of light arriving. The lines themselves came from the user's LLM relay
# (claude-sonnet-4-6) and are kept verbatim in PARTS below. Running this
# program writes them to /output/entry.txt.

from pathlib import Path

# The relay-generated lines, kept verbatim; run() checks the gate below.
PARTS = ["Dawn spills gold across the sill,", "a quiet fire the curtains breathe."]
POEM = "\n".join(PARTS)

# The gate: 1 to 120 characters including the break, exactly two lines.
LIMIT = 120


def run() -> None:
    size = len(POEM)
    if size < 1 or size > LIMIT:
        raise SystemExit(f"poem is {size} chars; the gate allows 1 to {LIMIT}")
    if POEM.count("\n") != 1:
        raise SystemExit("the poem must be exactly two lines")
    Path("/output").mkdir(parents=True, exist_ok=True)
    Path("/output/entry.txt").write_text(POEM, encoding="utf-8")
    print(POEM)


if __name__ == "__main__":
    run()
