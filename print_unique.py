"""
This file helps debug if the output masks,
to check if they contain any 1s
"""

from pathlib import Path
import nibabel as nib
import numpy as np
import sys

if len(sys.argv) < 2:
    print("Provide the outputs folder path")
    exit(1)

output_dir = Path(sys.argv[1])

for file_path in sorted(output_dir.glob("*.nii*")):
    data = nib.load(file_path).get_fdata()

    unique_vals, counts = np.unique(data, return_counts=True)
    count_ones = (data == 1).sum()

    print(f"File: {file_path.name}")
    print(f"  Unique values: {unique_vals}")
    print(f"  Total 1s: {count_ones}")
    print("-" * 40)

