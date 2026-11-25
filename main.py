"""Copy the 25 November 2026 news image into the harness output folder.

The repository holds the finished front page as entry.png. This program
only checks that the file really is a PNG and places an identical copy at
$MAKEFUN_OUTPUT_DIR/entry.png (or /output/entry.png when that variable is
not set). It never touches the network and never changes the bytes.
"""

import os
import sys


MAGIC_BYTES = (0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A)


def publish() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    with open(source, "rb") as handle:
        data = handle.read()
    if len(data) < 8 or tuple(data[:8]) != MAGIC_BYTES:
        print("entry.png: not a PNG file", file=sys.stderr)
        return 1
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(outdir, exist_ok=True)
    target = os.path.join(outdir, "entry.png")
    with open(target, "wb") as handle:
        handle.write(data)
    return 0


if __name__ == "__main__":
    raise SystemExit(publish())
