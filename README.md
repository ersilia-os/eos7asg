# PADEL small molecule descriptors

## Model Identifiers
- Slug: padel
- Ersilia ID: eos7asg
- Tags: fingerprint,	ML,	descriptor

## Model Description 
PADEL physicochemical descriptors for QSAR 
- Input: SMILES 
- Output: Vector (16092 bit-vector for molecular representation)
- Model type: Regression
- Mode of training: Pretrained 
- Experimentally validated: No 

## Source code
This model is published by Yap Chun Wei (2011). PaDEL-Descriptor: An open source software to calculate molecular descriptors and fingerprints. *Journal of Computational Chemistry*. 32 (7): 1466-1474. DOI: https://onlinelibrary.wiley.com/doi/full/10.1002/jcc.21707
- Code: https://github.com/ecrl/padelpy
- Checkpoints: https://github.com/ecrl/padelpy/tree/master/padelpy/PaDEL-Descriptor

## License
The GPL-v3 license applies to all parts of the repository that are not externally maintained libraries. This repository uses the externally maintained library "PaDEL-Descriptor", located at `/src` and licensed under a MIT License

## History
- Model was downloaded Septenber 28, 2021
