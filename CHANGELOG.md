# Changelog

## Restoration release 1.0.0 - 2026-09-24

This release packages the supplied restored MAWS implementation, LEA-K validation case, provenance patch, and reproducibility documentation.

### DNA topology / force-field handling

Previous observed problem: DNA residues such as `DG5`, `DT`, and `DC3` were not defined by the protein force field alone, causing tleap `Illegal UNIT` failures during DNA aptamer construction.

Technical correction: `Complex.build()` now checks for structures marked with `is_dna` and adds `source leaprc.DNA.OL15` to the generated tleap input. `MAWS.py` marks the DNA XML structure with `DNA.is_dna = True`.

Expected effect: DNA residue templates are available to tleap during aptamer construction.

### tleap structure construction

Previous observed problem: every chain was wrapped in `sequence {}`, including protein/PDB library units. This could generate invalid commands such as `CHAIN1 = sequence {PDB}`.

Technical correction: `Complex.build()` distinguishes single library units from residue sequences. Protein/PDB units are emitted as `CHAINn = PDB`, while nucleic-acid chains remain `CHAINn = sequence {...}`.

Expected effect: protein structures loaded through `PDB.lib` are combined with the aptamer without invalid tleap sequence construction.

### Protein/nucleotide separation

Previous observed problem: protein structures and nucleotide sequence construction were treated identically in the tleap input.

Technical correction: nucleic acid chains are sequence-built; PDB-derived protein chains are loaded as library units. The final supplied DNA tleap input shows `CHAIN0 = sequence {...}` and `CHAIN1 = PDB`.

Expected effect: aptamer extension can proceed while preserving protein structure handling.

### Empty-chain safeguards

Previous observed problem: an uninitialized aptamer chain could produce invalid empty chain definitions.

Technical correction: `Complex.build()` skips chains without a sequence or `sequence_array`.

Expected effect: the initial empty aptamer placeholder does not generate invalid tleap input before the first nucleotide is selected.

### tleap failure detection

Previous observed problem: the workflow could continue after tleap failed, leading to stale or invalid topology/coordinate files and later OpenMM errors.

Technical correction: `subprocess.call("tleap ...")` return codes are checked. Nonzero exits raise `RuntimeError`.

Expected effect: topology generation failures stop close to the root cause.

### OpenMM context rebuilding / synchronization

Previous observed problem: iterative nucleotide extension changes topology and coordinates. A stale OpenMM `Context` could then receive a mismatched number of positions.

Technical correction: `Complex.rebuild()` recreates the Langevin integrator and OpenMM `Simulation` after topology/position edits. `Complex.get_energy()` also checks topology atom count against the current positions and recreates the simulation if they differ.

Expected effect: OpenMM context particle counts remain synchronized with the modified topology.

### CUDA platform handling

Previous observed state: the inherited baseline used `CPU` in `Complex.py`.

Technical correction: the supplied restored code selects `mm.Platform.getPlatformByName('CUDA')`.

Expected effect: the documented restored implementation targets CUDA/OpenMM GPU execution. CPU execution remains a possible future compatibility improvement, but was not verified here.

### Reproducibility improvements

Added the LEA-K example, expected reference sequence, validation interpretation, environment specification, helper scripts, lightweight tests, and documentation. No deterministic random-seed control was found or added in this release.

