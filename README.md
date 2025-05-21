# PADEL small molecule descriptors

PaDEL is a commonly used molecular descriptor. It calculates 1875 molecular descriptors (1444 1D and 2D descriptors, 431 3D descriptors) and 12 types of fingerprints for small molecule representation. Originally developed in Java, here we provide PaDDELPy, its python implementation.

This model was incorporated on 2021-09-27.

## Information
### Identifiers
- **Ersilia Identifier:** `eos7asg`
- **Slug:** `padel`

### Domain
- **Task:** `Representation`
- **Subtask:** `Featurization`
- **Biomedical Area:** `Any`
- **Target Organism:** `Not Applicable`
- **Tags:** `Descriptor`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `1875`
- **Output Consistency:** `Fixed`
- **Interpretation:** Vector representation of a molecule

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| aats0e | float |  | PADEL Descriptor property |
| aats0i | float |  | PADEL Descriptor property |
| aats0m | float |  | PADEL Descriptor property |
| aats0p | float |  | PADEL Descriptor property |
| aats0s | float |  | PADEL Descriptor property |
| aats0v | float |  | PADEL Descriptor property |
| aats1e | float |  | PADEL Descriptor property |
| aats1i | float |  | PADEL Descriptor property |
| aats1m | float |  | PADEL Descriptor property |
| aats1p | float |  | PADEL Descriptor property |

_10 of 1875 columns are shown_
### Source and Deployment
- **Source:** `Local`
- **Source Type:** `External`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos7asg](https://hub.docker.com/r/ersiliaos/eos7asg)
- **Docker Architecture:** `AMD64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos7asg.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos7asg.zip)

### Resource Consumption
- **Model Size (Mb):** `1`
- **Environment Size (Mb):** `421`


### References
- **Source Code**: [https://github.com/ecrl/padelpy](https://github.com/ecrl/padelpy)
- **Publication**: [https://onlinelibrary.wiley.com/doi/10.1002/jcc.21707](https://onlinelibrary.wiley.com/doi/10.1002/jcc.21707)
- **Publication Type:** `Peer reviewed`
- **Publication Year:** `2010`
- **Ersilia Contributor:** [miquelduranfrigola](https://github.com/miquelduranfrigola)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [MIT](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos7asg
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos7asg
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
