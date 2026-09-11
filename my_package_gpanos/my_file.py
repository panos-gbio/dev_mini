from pathlib import Path

from my_package_gpanos.my_other_file import CONSTANT

print(f"script running from: {Path(__file__).resolve()}")
print(f"CONSTANT: {CONSTANT}")
