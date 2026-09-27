# Restoration Patch

`maws_restoration.patch` is a real `git diff` from the inherited MAWS baseline source to the supplied restored implementation in `src/MAWS`.

## Baseline

The baseline source was the nested `MAWS-Heidelberg-x-NU_Kazakhstan-main` directory from the supplied archive. It corresponds to the public NU Kazakhstan/Heidelberg MAWS code lineage.

## Modified files

- `src/MAWS/Complex.py`
- `src/MAWS/MAWS.py`
- `src/MAWS/DNA.py`
- `src/MAWS/Core.py`
- `src/MAWS/Prepare.py`

Only `Complex.py`, `MAWS.py`, and `Prepare.py` directly affect the documented restored DNA execution path. `DNA.py` adds RNA definitions and a module-level demonstration block inherited from the supplied modified tree. `Core.py` changes one comment.

## Apply

From a clean checkout containing the inherited baseline:

```bash
git apply patches/maws_restoration.patch
```

During repository preparation, `git apply --check patches/maws_restoration.patch` was tested in a clean temporary copy of the baseline.

