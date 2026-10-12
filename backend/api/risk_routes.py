"""
Risk Agent API
"""

from fastapi import APIRouter

from backend.agents.risk_agent import (
    RiskAgent
)

router = APIRouter()

risk_agent = RiskAgent()


@router.post("/risk")
def evaluate_risk(payload: dict):

    return risk_agent.evaluate(

        payload["customer"]

    )