import sys
from fontTools.ttLib import TTFont
from pathlib import Path

arg = sys.argv[1] if len(sys.argv) > 1 else "cyrillic"
charset = arg.split("=")[-1] if arg.startswith("--charset=") else arg
required = range[charset]

range = {
    "cyrillic": range(0x0400, 0x04FF + 1)
}

required = range[charset]

for font_path in fonts:
    font = TTFont(str(font_path))
    cmap = font["cmap"].getBestCmap()
    missing = [cp for cp in required if cp not in cmap]
    if missing:
        print(f"{font_path} missing {len(missing)} {charset} glyphs")
        sys.exit(1)

print("All fonts cover", charset)
