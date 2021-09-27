import csv
import sys
from padelpy import from_smiles

infile = sys.argv[1]
outfile = sys.argv[2]

with open(infile, "r") as f:
    reader = csv.reader(f)
    next(reader)
    smiles = []
    for r in reader:
        smiles += [r[0]]

descs = from_smiles(smiles)

keys = None
with open(outfile, "w", newline="") as f:
    writer = csv.writer(f)
    for desc in descs:
        if keys is None:
            keys = sorted([k for k, _ in desc.items()])
            writer.writerow(keys)
        v = [desc[k] for k in keys]
        writer.writerow(v)
