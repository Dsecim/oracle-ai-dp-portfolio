import subprocess
import sys
from pathlib import Path


def test_train_pipeline_smoke(tmp_path: Path):
    data_path = tmp_path / "clientes.csv"
    model_path = tmp_path / "model.pkl"

    # Generate mock data
    subprocess.check_call(
        [
            sys.executable,
            "data-generator/generate_mock_data.py",
            "--rows",
            "200",
            "--out",
            str(data_path),
        ]
    )

    # Train model
    subprocess.check_call(
        [
            sys.executable,
            "ml/train.py",
            "--input",
            str(data_path),
            "--model",
            str(model_path),
        ]
    )

    assert model_path.exists()
