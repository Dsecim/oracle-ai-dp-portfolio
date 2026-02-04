import argparse
import os
import numpy as np
import pandas as pd


def generate_dataset(rows: int, seed: int = 42) -> pd.DataFrame:
    rng = np.random.default_rng(seed)

    df = pd.DataFrame({
        "customer_id": np.arange(1, rows + 1),
        "idade": rng.integers(18, 70, rows),
        "renda": rng.integers(2000, 15000, rows),
        "plano": rng.choice(
            ["basic", "premium", "enterprise"],
            size=rows,
            p=[0.6, 0.3, 0.1]
        ),
        "tempo_cliente": rng.integers(1, 60, rows),
        "qtd_chamados": rng.integers(0, 10, rows),
        "atraso_pagamento": rng.choice([0, 1], rows, p=[0.85, 0.15])
    })

    # Regra simples para gerar churn
    df["churn"] = (
        (df["qtd_chamados"] > 5) |
        (df["atraso_pagamento"] == 1)
    ).astype(int)

    return df


def main():
    parser = argparse.ArgumentParser(description="Generate mock customer churn dataset")
    parser.add_argument("--rows", type=int, default=5000)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument(
        "--out",
        type=str,
        default="data-generator/sample_output/clientes_sample.csv"
    )

    args = parser.parse_args()

    df = generate_dataset(args.rows, args.seed)

    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    df.to_csv(args.out, index=False)

    print(f"Arquivo gerado com sucesso: {args.out}")
    print(f"Total de linhas: {len(df)}")
    print(df.head())


if __name__ == "__main__":
    main()
