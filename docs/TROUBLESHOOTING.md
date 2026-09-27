# Troubleshooting

## Verified restoration issues

### Problem / symptom: `sequence: Illegal UNIT at position #1`

Probable cause: a PDB library unit was wrapped in `sequence {PDB}`, or DNA residue templates were not loaded.

How to diagnose: inspect `JOB_NAME.in` and `leap.log`.

Solution: verify that protein units are written as `CHAINn = PDB` and DNA runs include `source leaprc.DNA.OL15`.

### Problem / symptom: OpenMM reports the wrong number of positions

Probable cause: topology and positions changed during nucleotide extension while the OpenMM context still reflected an older system.

How to diagnose: compare the number of topology atoms with the number of positions before `setPositions()`.

Solution: the restored `Complex.rebuild()` and `Complex.get_energy()` recreate the simulation context after topology changes.

### Problem / symptom: workflow continues after tleap failed

Probable cause: inherited code did not check the tleap return code.

How to diagnose: inspect console output and `leap.log` for `Errors = 1`.

Solution: the restored code raises `RuntimeError` on nonzero tleap return.

## General issues

### Problem / symptom: `tleap` not found

Probable cause: AmberTools is not installed or the conda environment is not active.

How to diagnose: run `which tleap`.

Solution: activate the `maws` environment or install AmberTools from conda-forge.

### Problem / symptom: malformed PDB or unsupported residues

Probable cause: target PDB residue names or atoms are not compatible with AmberTools.

How to diagnose: run tleap manually on the PDB and inspect warnings.

Solution: clean or parameterize the structure before running MAWS.

### Problem / symptom: empty PDB chains

Probable cause: input structure contains chain records without usable atoms.

How to diagnose: inspect residues and chain IDs with a PDB parser.

Solution: remove empty chains before MAWS.

### Problem / symptom: O3'-P connectivity problems

Probable cause: nucleotide templates or residue aliases are not compatible with the expected append/prepend connectivity.

How to diagnose: inspect `DNA.xml`, `RNA.xml`, and tleap bond warnings.

Solution: use the supplied XML definitions and documented force fields; avoid silently substituting residue names.

### Problem / symptom: CUDA platform unavailable

Probable cause: no CUDA-capable OpenMM platform is installed or the driver is incompatible.

How to diagnose: run `python scripts/check_environment.py`.

Solution: install a CUDA-compatible OpenMM build and driver, or modify and verify CPU platform support in `Complex.py`.

### Problem / symptom: NaN or unstable energy

Probable cause: bad contacts, poor starting geometry, missing parameters, or unstable minimization.

How to diagnose: inspect the lowest-energy structures and OpenMM/tleap warnings.

Solution: clean the PDB, verify parameters, reduce perturbation size, or test shorter smoke runs.

### Problem / symptom: output sequence differs from the reference

Probable cause: stochastic sampling and platform/force-field differences.

How to diagnose: compare run parameters, software versions, and OpenMM platform.

Solution: treat exact sequence identity as stronger than basic technical reproduction unless seed control is added and verified.

