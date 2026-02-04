import argparse
import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split


def main():
    parser = argparse.ArgumentParser(description="Train churn prediction model")
    parser.add_argument("--input", required=True, help="CSV input dataset")
    parser.add_argument("--model", required=True, help="Path to save trained model")
    args = parser.parse_args()

    # Load dataset
    df = pd.read_csv(args.input)

    # Target
    y = df["churn"].astype(int)
    X = df.drop(columns=["churn"])

    # One-hot encode categorical
    X = pd.get_dummies(X, columns=["plano"], drop_first=False)

    # Split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42
    )

    # Train
    model = RandomForestClassifier(
        n_estimators=200,
        max_depth=None,
        random_state=42
    )
    model.fit(X_train, y_train)

    accuracy = model.score(X_test, y_test)

    # Persist
    joblib.dump(model, args.model)

    print("Model training completed")
    print(f"Accuracy: {accuracy:.4f}")
    print(f"Model saved at: {args.model}")


if __name__ == "__main__":
    main()
