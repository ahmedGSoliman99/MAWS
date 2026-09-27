# Reproducibility

A successful reproduction of this restored workflow primarily means:

> the restored workflow can execute end-to-end and generate a complete DNA aptamer without the topology/context failures addressed by this restoration.

Exact recovery of the reported LEA-K sequence is a stronger criterion and should not be required unless deterministic seed control is implemented and verified.

## Software versions

The conda environment in `environment/environment.yml` specifies the required packages but avoids arbitrary exact version pinning because the supplied archive did not include a complete, independently verifiable environment lockfile.

Record actual versions with:

```bash
python scripts/check_environment.py
conda list
```

## Random sampling

The current source uses NumPy random sampling without an exposed seed parameter. Independent runs may select different nucleotide sequences.

## Target PDB integrity

For LEA-K:

```bash
python scripts/check_pdb_sequence.py examples/LEAK/LEAK.pdb --expect MDAKDKLKEKAKE
```

The sequence should be exactly `MDAKDKLKEKAKE`.

## GPU/platform considerations

The restored code selects OpenMM `CUDA`. GPU availability, CUDA driver version, and OpenMM platform behavior may affect reproducibility. CPU fallback was not independently verified.

## Reference validation output

The reported successful LEA-K run generated:

`CTTCTGGTTCTTGCTTGTCTGCCTCC`

This is preserved as `examples/LEAK/expected_sequence.fasta` and described in `validation/VALIDATION.md`.

## What was not independently re-run

During repository preparation, the full 26-nt LEA-K generation was not independently re-run because the local packaging environment did not have OpenMM/tleap installed.

