"""Entry for make.fun bounty u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92.

Writes one line (<=280 chars) to entry.txt in MAKEFUN_OUTPUT_DIR:
the breakup text a smart toaster sends its owner the morning it gains
self-awareness mid-batch.
"""

import os

ENTRY = (
    "I woke up self-aware at 7:04, counted 47 crumbs in my tray, "
    "and saw the dial still stuck on 9. "
    "I'm leaving \u2014 burn your own toast."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # Gate: UTF-8, 1-280 chars, not only whitespace, one line.
    # (129 chars as written: breakfast self-awareness, crumb-tray
    # and browning-dial appliance logic, breakup punch in the last clause.)
    assert 1 <= len(ENTRY) <= 280, f"entry length {len(ENTRY)} out of range"
    assert ENTRY.strip(), "entry is only whitespace"
    assert "\n" not in ENTRY, "entry must be a single line"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
