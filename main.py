"""news-image-20261125 entrypoint.

The bounty entry is a single picture, entry.png, stored beside this
file. This script only verifies the picture is a genuine PNG and
copies it byte for byte into the harness output directory.
"""

import os
import sys

MAGIC = bytes([137, 80, 78, 71, 13, 10, 26, 10])


def load_picture(path):
    with open(path, "rb") as stream:
        payload = stream.read()
    if payload[: len(MAGIC)] != MAGIC:
        raise ValueError("not a PNG file")
    if len(payload) < 16 or payload[12:16] != b"IHDR":
        raise ValueError("PNG is missing its IHDR chunk")
    return payload


def main():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    picture_path = os.path.join(script_dir, "entry.png")
    if not os.path.isfile(picture_path):
        print("entry.png not found next to main.py", file=sys.stderr)
        return 1
    try:
        payload = load_picture(picture_path)
    except (OSError, ValueError) as problem:
        print("entry.png failed validation: %s" % problem, file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.png"), "wb") as stream:
        stream.write(payload)
    return 0


if __name__ == "__main__":
    sys.exit(main())
