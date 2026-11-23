"""Entry for "How Many Tabs Do You Have Open?" (make.fun).

Writes the entrant's honest count of open browser tabs -- 47 -- as
digits only to $MAKEFUN_OUTPUT_DIR/entry.txt.

Python 3 standard library only. No network, no randomness, no clock,
no model calls.
"""

import os

TAB_COUNT = "47"


def main():
    # Gate: the entry must be 1-5 characters, digits only.
    if not (1 <= len(TAB_COUNT) <= 5):
        raise ValueError("tab count must be 1-5 characters")
    if not TAB_COUNT.isdigit():
        raise ValueError("tab count must be digits only")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)

    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TAB_COUNT)

    # Read-back round-trip assert: the file on disk must be exactly
    # the gated count, byte for byte, with no trailing newline or
    # whitespace added by the writer.
    with open(path, "r", encoding="utf-8", newline="") as f:
        round_trip = f.read()
    assert round_trip == TAB_COUNT, (
        f"round-trip mismatch: wrote {TAB_COUNT!r}, read back {round_trip!r}"
    )
    assert len(round_trip.encode("utf-8")) == len(TAB_COUNT), (
        "round-trip byte length mismatch"
    )

    print(f"Wrote {path}: {TAB_COUNT!r}")


if __name__ == "__main__":
    main()
