# Validation

## Validation target

LEA-K peptide

`MDAKDKLKEKAKE`

The supplied `examples/LEAK/LEAK.pdb` was checked by residue records and contains this exact 13-residue sequence.

## Parameters

- Aptamer type: DNA
- Final designed aptamer length: 26 nt
- MAWS `--ntides` value: `25` further extension steps after initial nucleotide selection
- First step samples: 5000
- Later step samples: 5000 per nucleotide-extension step
- beta: `0.01`

## Reported reference result

`CTTCTGGTTCTTGCTTGTCTGCCTCC`

The raw reported run log is preserved in `validation/validation_log.txt`. The reported entropy/energy candidate log is preserved in `validation/reported_entropy_log.txt`.

## Validation interpretation

The reported successful run demonstrates technical completion of an end-to-end protein/peptide-to-DNA aptamer generation workflow for LEA-K in the supplied restored code lineage.

It does not by itself demonstrate:

- experimental affinity;
- biochemical specificity;
- superiority to SELEX;
- universal convergence;
- identical sequence generation across stochastic runs.

## Not independently re-run during repository preparation

The full 26-nt MAWS workflow was not independently re-run during repository preparation because the local machine used for packaging did not have OpenMM or tleap available through its default Python environment.

