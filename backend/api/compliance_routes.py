"""
Compliance Agent API
"""

from fastapi import APIRouter

from backend.agents.compliance_agent import (
    ComplianceAgent
)

router = APIRouter()

compliance_agent = ComplianceAgent()


@router.post("/compliance")
def evaluate_compliance(
        payload: dict):

    return compliance_agent.evaluate(

        payload["transaction"]

    )