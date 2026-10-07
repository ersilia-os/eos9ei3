# Synthetic accessibility score

Calculates the synthetic accessibility score of Ertl and Schuffenhauer, combining a fragment contribution term, derived from how commonly each substructure occurs among one million representative PubChem molecules, with a penalty for size, stereocomplexity, macrocycles and unusual ring systems. Scores run from 1 to 10 and are inverted relative to intuition, low marking compounds that should be straightforward to make. The authors checked the score against estimates by experienced medicinal chemists for 40 molecules, agreeing with r2 of 0.89. This is the implementation contributed to RDKit.

This model was incorporated on 2022-07-12.Last packaged on 2025-09-15.

## Information
### Identifiers
- **Ersilia Identifier:** `eos9ei3`
- **Slug:** `sa-score`

### Domain
- **Task:** `Annotation`
- **Subtask:** `Property calculation or prediction`
- **Biomedical Area:** `Any`
- **Target Organism:** `Any`
- **Tags:** `Synthetic accessibility`, `Chemical synthesis`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `1`
- **Output Consistency:** `Fixed`
- **Interpretation:** Synthetic accessibility score from 1 to 10, where lower values indicate easier synthesis.

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| sa_score | float | low | Synthetic accessibility score |


### Source and Deployment
- **Source:** `Local`
- **Source Type:** `External`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos9ei3](https://hub.docker.com/r/ersiliaos/eos9ei3)
- **Docker Architecture:** `AMD64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos9ei3.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos9ei3.zip)

### Resource Consumption
- **Model Size (Mb):** `8`
- **Environment Size (Mb):** `516`
- **Image Size (Mb):** `450.34`

**Computational Performance (seconds):**
- 10 inputs: `27`
- 100 inputs: `16.77`
- 10000 inputs: `45.03`

### References
- **Source Code**: [https://github.com/rdkit/rdkit/tree/master/Contrib/SA_Score](https://github.com/rdkit/rdkit/tree/master/Contrib/SA_Score)
- **Publication**: [https://doi.org/10.1186/1758-2946-1-8](https://doi.org/10.1186/1758-2946-1-8)
- **Publication Type:** `Peer reviewed`
- **Publication Year:** `2009`
- **Ersilia Contributor:** [miquelduranfrigola](https://github.com/miquelduranfrigola)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [BSD-3-Clause](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos9ei3
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos9ei3
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!
