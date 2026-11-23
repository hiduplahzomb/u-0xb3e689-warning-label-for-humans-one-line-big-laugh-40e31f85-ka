"""One-line entry for make.fun's "Warning Label for Humans" bounty.

The safety warning label that should come printed on every human being,
framed as a biological machine overheating: a human run too long without
sleep does not drain like a battery, it overheats and shuts itself down
mid-task. Funny first, plausible second, in the terse register of a real
product label.
"""

import os
import sys

# The entry: one line, at most 160 characters.
# Angle: overheating/shutdown — the human overheats after 16 hours of
# continuous use, and without sleep the unit shuts down without warning.
# The three shutdown locations escalate from embarrassing (mid-sentence)
# to professional (mid-meeting) to a genuine hazard (mid-staircase):
# the last one is what makes it a safety warning, not an instruction.
TEXT = (
    "WARNING: This human overheats after 16 hours of continuous use. "
    "Do not operate without sleep — unit may shut down mid-sentence, "
    "mid-meeting, or mid-staircase."
)


def main() -> int:
    """Write the entry to /output/entry.txt and verify it byte-for-byte."""
    if not (1 <= len(TEXT) <= 160):
        print(f"gate failed: entry is {len(TEXT)} characters, must be 1-160",
              file=sys.stderr)
        return 1
    if not TEXT.strip():
        print("gate failed: entry is only whitespace", file=sys.stderr)
        return 1
    if "\n" in TEXT:
        print("gate failed: entry must be a single line", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)

    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != TEXT:
        print("gate failed: entry.txt does not match TEXT byte-for-byte",
              file=sys.stderr)
        return 1

    print(f"entry written: {len(TEXT)} characters -> {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
