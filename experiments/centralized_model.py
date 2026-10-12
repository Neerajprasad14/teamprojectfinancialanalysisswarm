"""
File: centralized_model.py

Purpose:
Baseline comparison model.

Represents traditional enterprise
architecture where a single model
handles all decisions.

Research Contribution:
Provides comparison against
AgentFin-Swarm.
"""

from xgboost import XGBClassifier

from sklearn.metrics import (
    accuracy_score,
    f1_score
)

model = XGBClassifier()

model.fit(
    X_train,
    y_train
)

prediction = model.predict(
    X_test
)

print(
    "Accuracy:",
    accuracy_score(
        y_test,
        prediction
    )
)

print(
    "F1:",
    f1_score(
        y_test,
        prediction
    )
)