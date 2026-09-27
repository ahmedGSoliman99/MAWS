# MAWS

## Restored and reproducible workflow for de novo DNA aptamer design

This repository provides a restored and documented implementation of Making Aptamers Without SELEX (MAWS) for structure-guided de novo nucleic-acid aptamer generation.

The restored implementation addresses technical issues encountered in the tested public code lineage involving DNA force-field handling, tleap-based topology construction, protein/nucleotide structure handling, and OpenMM topology/context consistency.

An end-to-end validation case is provided for the 13-residue LEA-K peptide:

`MDAKDKLKEKAKE`

The reported validation run generated a complete 26-nt DNA aptamer:

`CTTCTGGTTCTTGCTTGTCTGCCTCC`

This sequence is a reference sequence obtained in the reported successful validation run. MAWS uses stochastic conformational sampling, and this repository does not claim that independent executions will necessarily generate the identical sequence unless deterministic seed control is added and verified.

## Why this repository exists

This repository is a reproducibility-oriented restoration of an inherited MAWS code lineage. The goal is to preserve the scientific logic of the supplied implementation while making the technical restoration, provenance, execution requirements, and validation evidence clear enough for peer review.

Appropriate wording for the restoration is:

> The tested public MAWS code lineage did not provide reproducible end-to-end protein-to-DNA aptamer generation in the tested environment prior to the restoration described here.

## Key restoration changes

- DNA structures marked with `is_dna` trigger loading of `leaprc.DNA.OL15`.
- RNA structures marked with `is_rna` trigger loading of `leaprc.RNA.OL3`.
- Empty chains are skipped when generating tleap chain definitions.
- Protein PDB library units are loaded directly as `CHAINn = PDB` rather than incorrectly wrapped in `sequence {PDB}`.
- tleap return codes are checked and failures raise an explicit `RuntimeError`.
- OpenMM simulations are rebuilt after topology/position changes during sequence extension.
- The restored code uses the CUDA OpenMM platform in `Complex.py`; CPU execution has not been independently verified in this repository preparation.

The complete source diff is in [`patches/maws_restoration.patch`](patches/maws_restoration.patch).

## Repository structure

```text
MAWS/
  src/MAWS/                 restored MAWS source and XML residue definitions
  examples/LEAK/            LEA-K input, run script, and expected reference sequence
  validation/               reported validation log and interpretation
  environment/              conda environment and setup notes
  patches/                  restoration patch against the inherited baseline
  docs/                     installation, usage, methods, troubleshooting, reproducibility
  scripts/                  environment and PDB sequence helpers
  tests/                    lightweight tests; full MAWS generation is manual/integration
```

## Requirements

The MAWS workflow requires Python, OpenMM, AmberTools/tleap, NumPy, mpmath, numba, lxml, scikit-learn, and matplotlib. The supplied restored code requests the OpenMM `CUDA` platform, so a working CUDA-capable OpenMM installation is expected for the documented restored workflow.

See [`environment/README.md`](environment/README.md) and [`docs/INSTALLATION.md`](docs/INSTALLATION.md).

## Quick start

```bash
conda env create -f environment/environment.yml
conda activate maws
python scripts/check_environment.py
python scripts/check_pdb_sequence.py examples/LEAK/LEAK.pdb --expect MDAKDKLKEKAKE
bash examples/LEAK/run_LEAK.sh
```

The LEA-K run is computationally expensive. During repository preparation, the full 26-nt workflow was not independently re-run on this machine because OpenMM and tleap were not available in the local environment.

## LEA-K validation example

- Target: LEA-K peptide
- Sequence: `MDAKDKLKEKAKE`
- Target length: 13 aa
- Aptamer type: DNA
- Requested final aptamer length: 26 nt
- MAWS `-t` argument used for this length: `25` further extension steps after the initial nucleotide
- Sampling: 5000 configurations per nucleotide-extension step
- Beta: `0.01`
- Reported reference output: `CTTCTGGTTCTTGCTTGTCTGCCTCC`

See [`examples/LEAK/README.md`](examples/LEAK/README.md) and [`validation/VALIDATION.md`](validation/VALIDATION.md).

## Output interpretation

MAWS evaluates molecular-mechanics potential energies during stochastic conformational sampling and uses an entropy-based selection criterion implemented in `Routines.py`. These energies are not experimental binding energies and should not be described as binding free energies.

Successful completion means the restored workflow can execute end to end and generate a complete DNA aptamer without the topology/context failures addressed by the restoration.

## Known limitations

- MAWS uses molecular-mechanics/conformational sampling rather than experimental selection.
- Successful sequence generation does not prove target affinity or specificity.
- Predictions require downstream structural, computational, and experimental validation.
- Stochastic sampling may produce different sequences.
- Short, highly charged targets such as LEA-K can have electrostatically dominated interaction landscapes.
- Force-field, platform, and GPU/driver details can affect numerical behavior.
- CPU execution was not independently verified during repository preparation.

## Citation and attribution

Please cite this repository through [`CITATION.cff`](CITATION.cff) when using this restored workflow. Original MAWS attribution and licensing details are provided in [`NOTICE.md`](NOTICE.md).

No DOI is assigned yet. Add a DOI after formal release and archival.

