from pathlib import Path

# scripts/ and root directory
SCRIPTS_DIR = Path(__file__).resolve().parent.parent
ROOT_DIR = SCRIPTS_DIR.parent

# assets/
ASSETS_DIR = ROOT_DIR / "assets"

# data/
DATA_DIR = ROOT_DIR / "data"

# maps/
MAP_DIR = ROOT_DIR / "maps"

# tests/
# TESTS_DIR = ROOT_DIR / "tests"