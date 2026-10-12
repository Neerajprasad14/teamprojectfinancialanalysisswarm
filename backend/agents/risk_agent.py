"""
Risk Assessment Agent
"""

from pathlib import Path

import joblib

from backend.config import (
    RISK_THRESHOLD
)


class RiskAgent:

    def __init__(self):

        model_path = (

            Path(__file__)
            .resolve()
            .parents[1]

            / "models"

            / "risk_model.pkl"
        )

        self.model = joblib.load(
            model_path
        )

    def evaluate(
            self,
            customer):

        features = [[

            customer["credit.policy"],

            customer["int.rate"],

            customer["installment"],

            customer["log.annual.inc"],

            customer["dti"],

            customer["fico"],

            customer["days.with.cr.line"],

            customer["revol.bal"],

            customer["revol.util"],

            customer["inq.last.6mths"],

            customer["delinq.2yrs"],

            customer["pub.rec"]

        ]]

        probability = (

            self.model
            .predict_proba(
                features
            )[0][1]
        )

        score = round(
            probability * 100,
            2
        )

        return {

            "agent":
            "RiskAgent",

            "score":
            score,

            "confidence":
            probability,

            "risk_level":

            "HIGH"

            if score >= RISK_THRESHOLD

            else "LOW"
        }