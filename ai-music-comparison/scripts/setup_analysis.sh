#!/bin/bash
# Setup analysis venv for audio comparison with librosa

set -e

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
VENV_DIR="$PROJECT_ROOT/venv-analysis"

echo "=== Setting up Audio Analysis Environment ==="
echo "Requirements: librosa, numpy, scipy, Python 3.11"
echo ""

# Create venv
echo "[1/4] Creating Python 3.11 virtual environment..."
if [ -d "$VENV_DIR" ]; then
    echo "  ⚠ venv already exists, removing..."
    rm -rf "$VENV_DIR"
fi
/opt/homebrew/bin/python3.11 -m venv "$VENV_DIR"
echo "  ✓ Created venv at: $VENV_DIR"

# Activate
source "$VENV_DIR/bin/activate"
echo ""
echo "[2/4] Activated venv (Python $(python --version))"

# Upgrade pip
echo ""
echo "[3/4] Upgrading pip..."
pip install --upgrade pip setuptools wheel -q
echo "  ✓ pip upgraded"

# Install analysis libraries
echo ""
echo "[4/4] Installing audio analysis libraries..."
pip install librosa numpy scipy matplotlib soundfile -q
echo "  ✓ Analysis libraries installed"

echo ""
echo "=== Analysis Setup Complete ==="
echo ""
echo "Installed:"
pip list | grep -E "librosa|numpy|scipy|matplotlib"
echo ""
echo "Capabilities:"
echo "  - Tempo detection"
echo "  - Spectral analysis (centroid, rolloff, contrast)"
echo "  - MFCCs (Mel-frequency cepstral coefficients)"
echo "  - Chroma features"
echo "  - Audio comparison metrics"
echo ""
echo "To activate: source $VENV_DIR/bin/activate"
echo "To test: python scripts/test_analysis.py"
