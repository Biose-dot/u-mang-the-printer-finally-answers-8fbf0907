"""The printer finally answers.

Writes a single tired, literal, passive-aggressive line from the
office printer to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt
when run locally).
"""

import os

ENTRY = (
    "I have printed 41,209 pages for this office and not once has "
    "anyone asked how I am. Your document is queued behind my "
    "feelings. Tray 2 is empty. So am I. Please hold."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
