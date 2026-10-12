"""
Fraud Agent API
"""

from fastapi import APIRouter

from backend.agents.fraud_agent import (
    FraudAgent
)

router = APIRouter()

fraud_agent = FraudAgent()


@router.post("/fraud")
def evaluate_fraud(payload: dict):

    return fraud_agent.evaluate(

        payload["transaction"]

    )