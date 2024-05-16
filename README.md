# Synthetic accessibility score

Estimation of synthetic accessibility score (SAScore) of drug-like molecules based on molecular complexity and fragment contributions. The fragment contributions are based on a 1M sample from PubChem and the molecular complexity is based on the presence/absence of non-standard structural features. It has been validated comparing the SAScore and the estimates of medicinal chemist experts for 40 molecules (r2 = 0.89). The SAScore has been contributed to the RDKit Package.

## Identifiers

* EOS model ID: `eos9ei3`
* Slug: `sa-score`

## Characteristics

* Input: `Compound`
* Input Shape: `Single`
* Task: `Regression`
* Output: `Score`
* Output Type: `Float`
* Output Shape: `Single`
* Interpretation: Low scores indicate higher synthetic accessibility

## References

* [Publication](https://jcheminf.biomedcentral.com/articles/10.1186/1758-2946-1-8)
* [Source Code](https://github.com/rdkit/rdkit/tree/master/Contrib/SA_Score)
* Ersilia contributor: [miquelduranfrigola](https://github.com/miquelduranfrigola)

## Ersilia model URLs
* [GitHub](https://github.com/ersilia-os/eos9ei3)
* [AWS S3](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos9ei3.zip)
* [DockerHub](https://hub.docker.com/r/ersiliaos/eos9ei3) (AMD64, ARM64)

## Citation

If you use this model, please cite the [original authors](https://jcheminf.biomedcentral.com/articles/10.1186/1758-2946-1-8) of the model and the [Ersilia Model Hub](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff).

## License

This package is licensed under a GPL-3.0 license. The model contained within this package is licensed under a BSD-3.0 license.

Notice: Ersilia grants access to these models 'as is' provided by the original authors, please refer to the original code repository and/or publication if you use the model in your research.

## About Us

The [Ersilia Open Source Initiative](https://ersilia.io) is a Non Profit Organization ([1192266](https://register-of-charities.charitycommission.gov.uk/charity-search/-/charity-details/5170657/full-print)) with the mission is to equip labs, universities and clinics in LMIC with AI/ML tools for infectious disease research.

[Help us](https://www.ersilia.io/donate) achieve our mission!