#!/bin/bash
# Setup Bark venv with latest PyTorch

set -e

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
VENV_DIR="$PROJECT_ROOT/venv-bark"

echo "=== Setting up Bark Environment ==="
echo "Requirements: Latest PyTorch, Python 3.11"
echo ""

# Create venv
echo "[1/5] Creating Python 3.11 virtual environment..."
if [ -d "$VENV_DIR" ]; then
    echo "  ⚠ venv already exists, removing..."
    rm -rf "$VENV_DIR"
fi
/opt/homebrew/bin/python3.11 -m venv "$VENV_DIR"
echo "  ✓ Created venv at: $VENV_DIR"

# Activate
source "$VENV_DIR/bin/activate"
echo ""
echo "[2/5] Activated venv (Python $(python --version))"

# Upgrade pip
echo ""
echo "[3/5] Upgrading pip..."
pip install --upgrade pip setuptools wheel -q
echo "  ✓ pip upgraded"

# Install PyTorch (latest)
echo ""
echo "[4/5] Installing latest PyTorch..."
pip install torch torchvision torchaudio -q
echo "  ✓ PyTorch $(python -c 'import torch; print(torch.__version__)')"

# Install Bark and dependencies
echo ""
echo "[5/5] Installing Bark with optimization libraries..."
pip install git+https://github.com/suno-ai/bark.git -q
pip install transformers accelerate scipy -q 2>&1 | grep -v "already satisfied" || true
echo "  ✓ Bark installed"

echo ""
echo "=== Bark Setup Complete ==="
echo ""
echo "Installed:"
pip list | grep -E "bark|torch|transformers"
echo ""
echo "⚠ Note: Bark has 13-second generation limit (guide details)"
echo ""
echo "To activate: source $VENV_DIR/bin/activate"
echo "To test: python scripts/test_bark.py"
