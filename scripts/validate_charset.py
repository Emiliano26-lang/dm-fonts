import argparse
from fontTools.ttLib import TTFont
from pathlib import Path
import sys

parser = argparse.ArgumentParser()
parser.add_argument("--charset", default="cyrillic", choices=["cyrillic"])
parser.add_argument("fonts", nargs="+", help="Font files to validate")
args = parser.parse_args()

ranges = {
    "cyrillic": range(0x0400, 0x04FF + 1)
}

required = ranges[args.charset]

for font_path in args.fonts:
    font = TTFont(font_path)
    cmap = font["cmap"].getBestCmap()
    missing = [cp for cp in required if cp not in cmap]
    if missing:
        print(f"{font_path} missing {len(missing)} {args.charset} glyphs")
        sys.exit(1)

print("All fonts cover", args.charset)
