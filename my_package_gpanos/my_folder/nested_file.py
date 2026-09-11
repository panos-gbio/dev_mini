import sys
from pathlib import Path

from my_package_gpanos.my_other_file import CONSTANT as CONSTANT_HIGHER

print(sys.path)  # python path array of directories, site packages, etc..

# check existence of a file I am importing from a higher hierarchy
file_path = Path(__file__)

if not file_path.exists():
    raise FileNotFoundError("File not found")
print(f"File found: {file_path}")
print(f"Absolute path: {file_path.resolve()}")

CONSTANT2 = "hi2"

print(f"script running from: {Path(__file__).resolve()}")
print(f"CONSTANT2: {CONSTANT2}")
print(f"CONSTANT_HIGHER: {CONSTANT_HIGHER}")
