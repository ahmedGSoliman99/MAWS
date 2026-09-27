from pathlib import Path
import importlib.util


ROOT = Path(__file__).resolve().parents[1]


def load_sequence_helper():
    path = ROOT / "scripts" / "check_pdb_sequence.py"
    spec = importlib.util.spec_from_file_location("check_pdb_sequence", path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def test_leak_pdb_sequence():
    helper = load_sequence_helper()
    sequence = helper.extract_sequence(ROOT / "examples" / "LEAK" / "LEAK.pdb")
    assert sequence == "MDAKDKLKEKAKE"


def test_expected_sequence_fasta():
    fasta = ROOT / "examples" / "LEAK" / "expected_sequence.fasta"
    lines = [line.strip() for line in fasta.read_text().splitlines() if line.strip()]
    assert lines[0] == ">MAWS_restored_LEAK_reference_output_26nt"
    assert lines[1] == "CTTCTGGTTCTTGCTTGTCTGCCTCC"
    assert len(lines[1]) == 26


def test_required_source_files_present():
    required = [
        "MAWS.py",
        "Complex.py",
        "DNA.xml",
        "RNA.xml",
        "PROT.xml",
        "LoadFrom.py",
        "Prepare.py",
        "Routines.py",
        "Space.py",
        "Structure.py",
    ]
    for name in required:
        assert (ROOT / "src" / "MAWS" / name).is_file()

