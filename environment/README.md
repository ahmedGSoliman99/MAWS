# Environment

The preferred setup is:

```bash
conda env create -f environment/environment.yml
conda activate maws
```

Then verify the required tools:

```bash
which tleap
python -c "import openmm; print(openmm.__version__)"
python scripts/check_environment.py
```

The environment file is inferred from source imports and the supplied MAWS guide. During repository preparation, this conda environment was not independently created on the local machine, and `tleap` was not available there.

If conda cannot solve OpenMM and AmberTools together on a specific platform, create the environment in stages:

```bash
conda create -n maws -c conda-forge python=3.10 openmm ambertools
conda activate maws
conda install -c conda-forge numpy mpmath numba matplotlib lxml scikit-learn pytest pyyaml
```

The restored source currently selects the OpenMM `CUDA` platform. A working CUDA driver and compatible OpenMM build are required for the documented restored configuration.

