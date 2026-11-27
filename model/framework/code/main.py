# imports
import os
import csv
import sys
from rdkit import Chem
import time
import shutil
import tempfile
from sascorer import readFragmentScores, processMols

# parse arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# current file directory
root = os.path.dirname(os.path.abspath(__file__))


# read SMILES from .csv file, assuming one column with header
smiles_list=[]
with open(input_file, "r") as f:
    reader = csv.reader(f)
    next(reader) # skip header
    for r in reader:
        smiles_list += [r[0]]

# temporary files go to a fresh temp dir: the working directory may be read-only (e.g. Apptainer)
tmp_dir = tempfile.mkdtemp()
tmp_input = os.path.join(tmp_dir, "tmp_input.smi")

with open(tmp_input, "w") as f:
    writer = csv.writer(f, delimiter=" ")
    writer.writerow(["smiles", "identifier"]) # header
    for i, smi in enumerate(smiles_list):
        writer.writerow([smi, "mol{0}".format(i)])

# run model
readFragmentScores("fpscores")
suppl = Chem.SmilesMolSupplier(tmp_input)
R = processMols(suppl)

outputs = []
for r in R:
    outputs += [r[-1].strip()]

#check input and output have the same lenght
input_len = len(smiles_list)
output_len = len(outputs)
assert input_len == output_len

# write output in a .csv file
with open(output_file, "w") as f:
    writer = csv.writer(f)
    writer.writerow(["sa_score"])  # header
    for o in outputs:
        writer.writerow([o])

shutil.rmtree(tmp_dir, ignore_errors=True)
