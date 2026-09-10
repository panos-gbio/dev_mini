import sys
from pathlib import Path

print(sys.path)  # python path array of directories, site packages, etc..

# check existence of a file I am importing from a higher hierarchy
file_path = Path(__file__)
if not file_path.exists():
    raise FileNotFoundError("File not found")
else:
    print(f"File found: {file_path}")
    print(f"Absolute path: {file_path.resolve()}")

# sys.path.insert(
#     0, "C:/Users/gpano/Desktop/projects_py/packaging_examples"
# )  # add a path to the python path array of directories, finds executables, site packages, etc..

from my_package_gpanos.my_other_file import CONSTANT as CONSTANT_HIGHER

CONSTANT2 = "hi2"

print(f"script running from: {Path(__file__).resolve()}")
print(f"CONSTANT2: {CONSTANT2}")
print(f"CONSTANT_HIGHER: {CONSTANT_HIGHER}")
