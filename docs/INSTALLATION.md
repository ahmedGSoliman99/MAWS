# Installation

## Clone

```bash
git clone https://github.com/ahmedGSoliman99/MAWS.git
cd MAWS
```

## Create environment

```bash
conda env create -f environment/environment.yml
conda activate maws
```

If conda cannot solve OpenMM and AmberTools together, use the staged procedure in `environment/README.md`.

## Verify AmberTools

```bash
which tleap
tleap -h
```

## Verify OpenMM

```bash
python -c "import openmm; print(openmm.__version__)"
```

## Verify available OpenMM platforms

```bash
python scripts/check_environment.py
```

The restored source currently requests the `CUDA` platform in `src/MAWS/Complex.py`. CPU execution has not been independently verified for this restoration.

## Verify LEA-K input

```bash
python scripts/check_pdb_sequence.py examples/LEAK/LEAK.pdb --expect MDAKDKLKEKAKE
```

## Run LEA-K example

```bash
bash examples/LEAK/run_LEAK.sh
```

The full 26-nt run is computationally expensive and was not independently re-run during repository preparation.

