from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_validation_log_contains_reported_final_sequence():
    text = (ROOT / "validation" / "validation_log.txt").read_text()
    assert "Final sequence:" in text
    assert "DCN DTN DTN DCN DTN DGN DGN DTN DTN DCN DTN DTN DGN DCN DTN DTN DGN DTN DCN DTN DGN DCN DCN DTN DCN DCN" in text


def test_restoration_patch_mentions_dna_force_field():
    patch = (ROOT / "patches" / "maws_restoration.patch").read_text()
    assert "leaprc.DNA.OL15" in patch
    assert "RuntimeError" in patch
    assert "getPlatformByName('CUDA')" in patch

