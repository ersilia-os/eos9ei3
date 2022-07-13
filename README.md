# Synthetic accessibility score
## Model identifiers
- Slug: sa-score
- Ersilia ID: eos9ei3
- Tags: Synthetic accessibility

# Model description
Estimation of synthetic accessibility score of drug-like molecules based on molecular complexity and fragment contributions.
- Input: Compound
- Output: SA score. Large SA scores (e.g. >6) indicate difficult synthesis. Small scores (e.g. <3) indicate feasible synthesis.
- Model type: Regression
- Training set: N/A
- Mode of training: Pretrained

# Source code
Cite the source publication.
- Code: https://github.com/rdkit/rdkit/tree/master/Contrib/SA_Score
- Checkpoints: https://github.com/rdkit/rdkit/tree/master/Contrib/SA_Score/fpscores.pkl.gz

# License
The main script is licensed by Novartis. The License is kept in this script. The current repository is licensed under GPLv3.

# History 
- Model incorporated on the 13th of July, 2022
