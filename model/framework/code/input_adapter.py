import sys
import csv

input_file = sys.argv[1]
smiles_list = []
with open(input_file, "r") as f:
    reader = csv.reader(f)
    next(reader) # skip header
    for r in reader:
        smiles_list += [r[0]]

with open("tmp_input.smi", "w") as f:
    writer = csv.writer(f, delimiter=" ")
    writer.writerow(["smiles", "identifier"]) # header
    for i, smi in enumerate(smiles_list):
        writer.writerow([smi, "mol{0}".format(i)])
