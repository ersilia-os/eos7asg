import csv
import sys
import os
import tempfile
from padelpy import from_smiles
from tqdm import tqdm

root = os.path.dirname(os.path.abspath(__file__))

infile = sys.argv[1]
outfile = sys.argv[2]

# Load expected descriptor columns
columns_file = os.path.join(root, "..", "columns", "run_columns.csv")
with open(columns_file, "r") as f:
    reader = csv.reader(f)
    next(reader)
    expected_keys = [r[0] for r in reader]

with open(infile, "r") as f:
    reader = csv.reader(f)
    next(reader)
    smiles = []
    for r in reader:
        smiles += [r[0]]

BATCH_SIZE = 10

# padelpy creates temporary .smi and .csv files in os.getcwd(),
# which fails in read-only Singularity environments.
_orig_dir = os.getcwd()

descs = []
with tempfile.TemporaryDirectory() as tmpdir:
    os.chdir(tmpdir)
    for i in tqdm(range(0, len(smiles), BATCH_SIZE)):
        batch = smiles[i:i+BATCH_SIZE]
        try:
            descs += from_smiles(batch, timeout=60)
        except Exception:
            for smi in batch:
                try:
                    descs += from_smiles([smi], timeout=60)
                except Exception:
                    descs.append(None)
    os.chdir(_orig_dir)

with open(outfile, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(expected_keys)
    nan_row = [""] * len(expected_keys)
    for desc in descs:
        if desc is None:
            writer.writerow(nan_row)
        else:
            desc_lower = {k.lower().replace('-', '_'): v for k, v in desc.items()}
            row = []
            for k in expected_keys:
                v = desc_lower.get(k, "")
                row.append("" if v.lower() == "nan" else v)
            writer.writerow(row)
