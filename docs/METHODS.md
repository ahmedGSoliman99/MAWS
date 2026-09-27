# Methods

MAWS is a structure-guided de novo aptamer-generation workflow. The implementation in this repository follows the supplied MAWS source rather than introducing a new aptamer-design algorithm.

## Workflow

```text
protein/peptide structure
initial molecular complex construction
candidate nucleotide addition
conformational sampling
OpenMM potential-energy evaluation
Boltzmann-weighted entropy calculation
selection of nucleotide extension
iterative aptamer growth
final nucleic-acid sequence and structure
```

## Implementation summary

`MAWS.py` reads a target PDB and constructs an initial `Complex`. For each candidate nucleotide, the aptamer chain is built with tleap, sampled in translational/rotational space, and evaluated with OpenMM. Later growth steps test appending and prepending each candidate nucleotide to the current best sequence.

`Routines.py` computes Boltzmann weights from sampled potential energies using `exp(-beta * E)`, normalizes them into probabilities, and computes an entropy term. The current source selects the candidate with the lowest entropy value at each step.

## Energy terminology

The values reported in `*_entropy.log` are MAWS/OpenMM potential-energy samples used for relative selection in this workflow. They should not be called experimental binding energies or binding free energies. No alchemical, umbrella-sampling, MM/PBSA, MM/GBSA, or other binding-free-energy method is implemented in the supplied source.

## Force fields and topology

The restored DNA path loads:

- `leaprc.ff14SB` from the MAWS entry point for protein handling;
- `leaprc.gaff` from `Complex`;
- `leaprc.DNA.OL15` when a DNA structure is present.

PDB-derived protein units are loaded through a tleap-generated `PDB.lib` and are combined with the nucleic acid chain.

## Stochastic sampling

Sampling uses NumPy random draws in `Space.py` and `Complex.py`. No explicit seed control was found in the restored source. The reference LEA-K sequence should therefore be interpreted as the output of the reported successful validation run, not as a guaranteed deterministic result.

