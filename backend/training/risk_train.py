"""
Risk Model Training
"""

from pathlib import Path

import joblib
import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

BASE_DIR = Path(__file__).resolve().parents[2]

DATASET_PATH = (
    BASE_DIR
    / "datasets"
    / "risk"
    / "loan_data.csv"
)

MODEL_PATH = (
    BASE_DIR
    / "backend"
    / "models"
    / "risk_model.pkl"
)

df = pd.read_csv(DATASET_PATH)

target = "not.fully.paid"

# Drop target and purpose to keep
# feature count consistent with RiskAgent

X = df.drop(
    columns=[
        target,
        "purpose"
    ]
)

y = df[target]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(
    X_train,
    y_train
)

predictions = model.predict(
    X_test
)

accuracy = accuracy_score(
    y_test,
    predictions
)

print(
    "Accuracy:",
    accuracy
)

MODEL_PATH.parent.mkdir(
    parents=True,
    exist_ok=True
)

joblib.dump(
    model,
    MODEL_PATH
)

print(
    "Risk model saved successfully."
)