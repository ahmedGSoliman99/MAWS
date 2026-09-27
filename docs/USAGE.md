# Usage

## Entry point

The restored workflow keeps the inherited MAWS entry point:

```bash
python /path/to/MAWS/src/MAWS/MAWS.py -p TARGET.pdb -n JOB_NAME -t N_FURTHER_STEPS -a DNA -c1 5000 -c2 5000 -b 0.01
```

The inherited script loads `DNA.xml`, `RNA.xml`, and `PROT.xml` relative to the current working directory. Run it from a working directory containing those XML files, or use `examples/LEAK/run_LEAK.sh`, which copies the required XML files into a clean output directory before execution.

Available arguments in the current source:

- `-n`, `--name`: job name and output prefix.
- `-b`, `--beta`: inverse-temperature parameter used in entropy scoring.
- `-c1`, `--firstchunksize`: samples in the first nucleotide-selection step.
- `-c2`, `--secondchunksize`: samples in later extension steps.
- `-t`, `--ntides`: number of further extension steps after the first nucleotide selection.
- `-p`, `--path`: input PDB path.
- `-a`, `--aptamer_type`: `DNA` or `RNA`.

No random seed argument or platform argument exists in the restored source.

## Input PDB expectations

The target PDB should contain a protein or peptide structure that AmberTools/tleap can load using the selected protein force field. Unsupported residues, malformed atoms, missing atoms, or unusual protonation states may require preprocessing outside MAWS.

For the LEA-K case:

```bash
python scripts/check_pdb_sequence.py examples/LEAK/LEAK.pdb --expect MDAKDKLKEKAKE
```

## Chain treatment

The restored `Complex.build()` emits nucleic-acid chains as tleap `sequence {...}` objects and emits single PDB-derived protein library units directly. Empty chains are skipped.

## DNA generation

For DNA, `MAWS.py` loads `DNA.xml`, marks it with `is_dna`, and candidate nucleotides are `DGN`, `DAN`, `DTN`, and `DCN`. `Complex.build()` then loads `leaprc.DNA.OL15`.

## Output files

For a job named `JOB_NAME`, MAWS writes:

- `JOB_NAME_output.log`: run metadata and final sequence.
- `JOB_NAME_entropy.log`: candidate sequences with entropy scores and lowest sampled potential energies.
- `JOB_NAME_RESULT.pdb`: final rendered complex.
- `JOB_NAME.in`: tleap input from the most recent topology build.
- `JOB_NAME.prmtop` and `JOB_NAME.inpcrd`: generated Amber topology and coordinates.
- `JOB_NAME_step_cache.pdb`: opened by the inherited code; often empty because intermediate PDB writes are commented out.
- `PDB.lib`, `PDB_tmp.pdb`, `PDB.frcmod`: PDB-derived library side files used by tleap.

Potential energies in the entropy log are OpenMM molecular-mechanics potential-energy samples. They are not experimental binding energies.

## LEA-K example

```bash
bash examples/LEAK/run_LEAK.sh
```

The reported successful validation run used `--ntides 25`, giving 26 nt total, with 5000 samples per step and `beta = 0.01`.

