#!/usr/bin/env bash
set -euo pipefail

echo "===================================="
echo " Oracle AI DP - Local Pipeline Start "
echo "===================================="

# Root do projeto
PROJECT_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$PROJECT_ROOT"

# -------------------------
# Virtual environment
# -------------------------
if [ ! -d ".venv" ]; then
  echo "Creating virtual environment..."
  python -m venv .venv
fi

source .venv/bin/activate

echo "Using python: $(which python)"

# -------------------------
# Upgrade pip
# -------------------------
pip install --upgrade pip

# -------------------------
# Install dependencies
# -------------------------
pip install -r data-generator/requirements.txt
pip install -r ml/requirements.txt

# -------------------------
# Generate mock data
# -------------------------
python data-generator/generate_mock_data.py \
  --rows 5000 \
  --out data-generator/output/clientes.csv

# -------------------------
# Train model
# -------------------------
python ml/train.py \
  --input data-generator/output/clientes.csv \
  --model ml/model.pkl

# -------------------------
# Predict
# -------------------------
python ml/predict.py \
  --model ml/model.pkl \
  --input data-generator/output/clientes.csv

echo "===================================="
echo " Pipeline finished successfully ✅ "
echo "===================================="
