"""
Fraud Detection Agent
"""

import joblib

from pathlib import Path

from backend.config import (
    FRAUD_THRESHOLD
)


class FraudAgent:

    def __init__(self):

        model_path = (

            Path(__file__)
            .resolve()
            .parents[1]

            / "models"

            / "fraud_model.pkl"
        )

        self.model = joblib.load(
            model_path
        )

    def evaluate(
            self,
            transaction):

        probability = 0.75

        score = round(
            probability * 100,
            2
        )

        return {

            "agent":
            "FraudAgent",

            "score":
            score,

            "confidence":
            probability,

            "fraud_level":

            "HIGH"

            if score >= FRAUD_THRESHOLD

            else "LOW"
        }