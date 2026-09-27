#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/../.." && pwd)"
SRC_DIR="${REPO_ROOT}/src/MAWS"
OUT_DIR="${SCRIPT_DIR}/outputs/LEAK_DNA_26nt"

mkdir -p "${OUT_DIR}"

for required in "${SRC_DIR}/MAWS.py" "${SRC_DIR}/DNA.xml" "${SCRIPT_DIR}/LEAK.pdb"; do
    if [[ ! -f "${required}" ]]; then
        echo "Required file not found: ${required}" >&2
        exit 1
    fi
done

echo "Repository root: ${REPO_ROOT}"
echo "Output directory: ${OUT_DIR}"
echo "Python: $(command -v python || true)"
echo "tleap: $(command -v tleap || true)"
python - <<'PY'
try:
    import openmm
    print("OpenMM:", openmm.__version__)
    for i in range(openmm.Platform.getNumPlatforms()):
        print("OpenMM platform:", openmm.Platform.getPlatform(i).getName())
except Exception as exc:
    print("OpenMM check failed:", exc)
PY

cp "${SCRIPT_DIR}/LEAK.pdb" "${OUT_DIR}/LEAK.pdb"
cp "${SRC_DIR}/DNA.xml" "${OUT_DIR}/DNA.xml"
cp "${SRC_DIR}/RNA.xml" "${OUT_DIR}/RNA.xml"
cp "${SRC_DIR}/PROT.xml" "${OUT_DIR}/PROT.xml"

# The supplied successful run included this minimal Amber parameter sidecar.
# It avoids a missing-file warning when the PDB library unit is loaded.
printf 'remark  minimal frcmod placeholder (no overrides)\n' > "${OUT_DIR}/PDB.frcmod"

(
    cd "${OUT_DIR}"
    python "${SRC_DIR}/MAWS.py" \
        --name LEAK_test_DNA \
        --path "${OUT_DIR}/LEAK.pdb" \
        --ntides 25 \
        --aptamer_type DNA \
        --firstchunksize 5000 \
        --secondchunksize 5000 \
        --beta 0.01
)

echo "MAWS run finished. Outputs are in ${OUT_DIR}"

