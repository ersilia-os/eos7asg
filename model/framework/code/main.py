import csv
import sys
import os
import tempfile
from padelpy import from_smiles

infile = sys.argv[1]
outfile = sys.argv[2]

with open(infile, "r") as f:
    reader = csv.reader(f)
    next(reader)
    smiles = []
    for r in reader:
        smiles += [r[0]]

# padelpy creates temporary .smi and .csv files in os.getcwd(),
# which fails in read-only Singularity environments.
_orig_dir = os.getcwd()
os.chdir(tempfile.mkdtemp())
descs = from_smiles(smiles)
os.chdir(_orig_dir)

keys = None
with open(outfile, "w", newline="") as f:
    writer = csv.writer(f)
    for desc in descs:
        if keys is None:
            keys = sorted([k for k, _ in desc.items()])
            header=[k.lower().replace('-', '_') for k in keys]
            writer.writerow(header)
        v = [desc[k] if desc[k] != "" else float("nan") for k in keys]
        writer.writerow(v)
