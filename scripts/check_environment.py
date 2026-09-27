#!/usr/bin/env python
"""Print basic MAWS runtime diagnostics."""

from __future__ import annotations

import importlib
import shutil
import sys


def version(module_name: str) -> str:
    try:
        module = importlib.import_module(module_name)
    except Exception as exc:
        return f"not available ({exc})"
    return getattr(module, "__version__", "available")


def main() -> int:
    print(f"Python: {sys.version.split()[0]}")
    print(f"Executable: {sys.executable}")
    print(f"NumPy: {version('numpy')}")
    print(f"OpenMM: {version('openmm')}")
    print(f"mpmath: {version('mpmath')}")
    print(f"numba: {version('numba')}")
    print(f"tleap: {shutil.which('tleap') or 'not found'}")

    try:
        import openmm

        for index in range(openmm.Platform.getNumPlatforms()):
            platform = openmm.Platform.getPlatform(index)
            print(f"OpenMM platform[{index}]: {platform.getName()}")
    except Exception as exc:
        print(f"OpenMM platform check failed: {exc}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

