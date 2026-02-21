import sys
from fontTools.ttLib import TTFont
from pathlib import Path

charset = sys.argv[1] if len(sys.argv) > 1 else "cyrillic"
fonts = Path("fonts").glob("*.ttf")

ranges = {
    "cyrillic": range(0x0400, 0x04FF + 1)
}

required = ranges[charset]

for font_path in fonts:
    font = TTFont(str(font_path))
    cmap = font["cmap"].getBestCmap()
    missing = [cp for cp in required if cp not in cmap]
    if missing:
        print(f"{font_path} missing {len(missing)} {charset} glyphs")
        sys.exit(1)

print("All fonts cover", charset)
