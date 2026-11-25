#!/usr/bin/env python3
"""Emit the 25 November 2026 front page for the make.fun harness.

The entry image lives beside this script as entry.png. This program makes
sure the file really is a PNG (magic bytes plus an IHDR chunk), then hands
an exact copy to the harness output directory so the judge sees the same
pixels on every run. It touches no network and writes nothing else.
"""

import hashlib
import os
import shutil
import sys

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
HERE = os.path.dirname(os.path.abspath(__file__))


def fail(message):
    sys.stderr.write("main.py: " + message + "\n")
    return 1


def main():
    picture = os.path.join(HERE, "entry.png")
    try:
        handle = open(picture, "rb")
    except OSError as exc:
        return fail("cannot open entry.png (%s)" % exc)
    with handle:
        head = handle.read(33)
    if head[:8] != PNG_MAGIC:
        return fail("entry.png does not start with the PNG magic bytes")
    if head[12:16] != b"IHDR":
        return fail("entry.png has no IHDR chunk where one belongs")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    destination = os.path.join(out_dir, "entry.png")
    shutil.copyfile(picture, destination)
    digest = hashlib.sha256(open(destination, "rb").read()).hexdigest()
    sys.stdout.write("wrote %s sha256=%s\n" % (destination, digest))
    return 0


if __name__ == "__main__":
    sys.exit(main())
