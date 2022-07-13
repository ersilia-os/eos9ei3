import sys
import csv

output_file = sys.argv[1]

sascores = []
with open("tmp_output.csv", "r") as f:
    reader = csv.reader(f, delimiter="\t")
    next(reader) # skip header
    for r in reader:
        sascores += [r[-1]]

with open(output_file, "w") as f:
    writer = csv.writer(f)
    writer.writerow(["sa_score"]) # header
    for sa in sascores:
        writer.writerow([sa])
