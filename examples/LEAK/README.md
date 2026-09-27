# LEA-K DNA Aptamer Example

## Target

LEA-K peptide

Sequence: `MDAKDKLKEKAKE`

Length: 13 aa

## Output

Output type: DNA aptamer

Requested final aptamer length: 26 nt

MAWS command detail: the current `MAWS.py` treats `--ntides` as the number of further extension steps after the first nucleotide. Therefore the reported 26-nt validation run used `--ntides 25`.

Sampling: 5000 configurations in the first step and 5000 configurations per later nucleotide-extension step

Beta: `0.01`

Reference reported output:

`CTTCTGGTTCTTGCTTGTCTGCCTCC`

This is a reference sequence obtained in the reported successful validation run, not a guaranteed deterministic output for every independent run.

## Run

From the repository root:

```bash
bash examples/LEAK/run_LEAK.sh
```

The script copies the LEA-K PDB and XML residue definitions into `examples/LEAK/outputs/LEAK_DNA_26nt`, prints basic environment diagnostics, and runs:

```bash
python src/MAWS/MAWS.py --name LEAK_test_DNA --path examples/LEAK/outputs/LEAK_DNA_26nt/LEAK.pdb --ntides 25 --aptamer_type DNA --firstchunksize 5000 --secondchunksize 5000 --beta 0.01
```

The command above is shown conceptually; the script resolves absolute paths at runtime.

## Input verification

Verify the PDB sequence before running:

```bash
python scripts/check_pdb_sequence.py examples/LEAK/LEAK.pdb --expect MDAKDKLKEKAKE
```

## Expected files from a completed run

- `LEAK_test_DNA_output.log`: run metadata and final selected sequence.
- `LEAK_test_DNA_entropy.log`: candidate sequence, entropy score, and lowest sampled potential energy for each evaluated candidate.
- `LEAK_test_DNA_RESULT.pdb`: final rendered complex structure.
- `LEAK_test_DNA.in`, `.prmtop`, `.inpcrd`: tleap input and generated Amber/OpenMM topology-coordinate files.
- `PDB.lib`, `PDB_tmp.pdb`, `PDB.frcmod`: local files used for the PDB-derived protein library unit.

