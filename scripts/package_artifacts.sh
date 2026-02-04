#!/usr/bin/env bash
set -euo pipefail

echo "Packaging project artifacts..."

PROJECT_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$PROJECT_ROOT"

ARTIFACT_NAME="artifacts.zip"

# Remove zip anterior se existir
rm -f "$ARTIFACT_NAME"

zip -r "$ARTIFACT_NAME" \
  data-generator \
  spark-jobs \
  ml \
  sql \
  configs \
  docs \
  diagrams \
  scripts \
  README.md \
  pyproject.toml \
  LICENSE \
  .gitignore \
  -x "*.env" \
  -x ".venv/*" \
  -x "data-generator/output/*" \
  -x "ml/model.pkl" \
  -x "__pycache__/*"

echo "Generated: $ARTIFACT_NAME"
