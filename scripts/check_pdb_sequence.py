#!/usr/bin/env python
"""Extract a protein sequence from ATOM/HETATM residue records in a PDB file."""

from __future__ import annotations

import argparse
from itertools import groupby
from pathlib import Path


THREE_TO_ONE = {
    "ALA": "A",
    "ARG": "R",
    "ASN": "N",
    "ASP": "D",
    "CYS": "C",
    "GLN": "Q",
    "GLU": "E",
    "GLY": "G",
    "HIS": "H",
    "ILE": "I",
    "LEU": "L",
    "LYS": "K",
    "MET": "M",
    "PHE": "F",
    "PRO": "P",
    "SER": "S",
    "THR": "T",
    "TRP": "W",
    "TYR": "Y",
    "VAL": "V",
}


def extract_sequence(path: Path) -> str:
    rows = []
    for line in path.read_text().splitlines():
        if line.startswith(("ATOM  ", "HETATM")):
            rows.append((line[21].strip(), line[22:26].strip(), line[17:20].strip()))
    residues = [key for key, _ in groupby(rows)]
    unknown = sorted({residue for _, _, residue in residues if residue not in THREE_TO_ONE})
    if unknown:
        raise ValueError(f"Unsupported residue names: {', '.join(unknown)}")
    return "".join(THREE_TO_ONE[residue] for _, _, residue in residues)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("pdb", type=Path)
    parser.add_argument("--expect")
    args = parser.parse_args()

    sequence = extract_sequence(args.pdb)
    print(sequence)
    if args.expect and sequence != args.expect:
        raise SystemExit(f"Expected {args.expect}, observed {sequence}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

