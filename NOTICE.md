# Notice and Attribution

This repository contains a restored and documented implementation derived from MAWS, Making Aptamers Without SELEX.

## Original MAWS authorship

The supplied MAWS source headers state:

- MAWS is part of the sharksome software suite.
- Copyright 2017 Michael Jendrusch.
- Authors: Michael Jendrusch and Stefan Holderbach.
- The software is published under the MIT license.

The inherited `LICENSE` file in this repository also identifies the NU_Kazakhstan iGEM team as the 2022 copyright holder for the modified distribution.

The inherited README and the public NU Kazakhstan repository identify MAWS as software first created by the Heidelberg iGEM team and slightly updated by the NU Kazakhstan iGEM team:

- https://github.com/iGEM-NU-Kazakhstan/MAWS-Heidelberg-x-NU_Kazakhstan
- https://static.igem.wiki/teams/4389/wiki/contribution/guidebook-how-to-use-making-aptamers-without-selex-maws.pdf

## Restored implementation

The present repository focuses on restoration, documentation, and reproducibility of a tested public MAWS code lineage. It does not claim original invention of MAWS.

Restoration work in this repository is attributed to Ahmed Gamal Soliman Ahmed. The restoration addresses technical execution issues involving DNA force-field loading, tleap input construction, empty chain handling, tleap failure detection, and OpenMM context/topology synchronization.

## License status

The inherited source distribution contains an MIT license. This repository retains that license file and preserves upstream attribution. No new DOI has been assigned; a DOI should be added only after formal archival, for example through Zenodo.

## Scientific interpretation

The tested public MAWS code lineage did not provide reproducible end-to-end protein-to-DNA aptamer generation in the tested environment prior to the restoration described here. The restored workflow demonstrates technical execution of the pipeline for the documented LEA-K case study. It does not establish experimental binding affinity, biochemical specificity, or equivalence to downstream molecular-dynamics studies unless those claims are independently supported.

