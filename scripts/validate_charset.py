import sys
from pathlib import Path

charset = sys.argv[1] if len(sys.argv) > 1 else "cyrillic"
sources = Path("sources").glob("*.glyphs")

print(f"Validating {charset} coverage in {len(list(sources))} source files...")
# TODO: implement actual checks
