import argparse
import joblib
import pandas as pd


def main():
    parser = argparse.ArgumentParser(description="Run churn prediction")
    parser.add_argument("--model", required=True, help="Trained model path")
    parser.add_argument("--input", required=True, help="CSV input dataset")
    args = parser.parse_args()

    model = joblib.load(args.model)
    df = pd.read_csv(args.input)

    X = pd.get_dummies(df.drop(columns=["churn"]), columns=["plano"], drop_first=False)

    # Align columns with training
    model_features = getattr(model, "feature_names_in_", None)

    if model_features is not None:
        for col in model_features:
            if col not in X.columns:
                X[col] = 0
        X = X[model_features]

    scores = model.predict_proba(X)[:, 1]

    result = df[["customer_id"]].copy()
    result["churn_score"] = scores

    print(result.head(10).to_string(index=False))


if __name__ == "__main__":
    main()
