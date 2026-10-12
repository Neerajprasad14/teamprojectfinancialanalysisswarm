"""
Test Compliance Agent
"""

from agents.compliance_agent import (
    ComplianceAgent
)


def test_compliance_agent():

    agent = ComplianceAgent()

    transaction = {

        "amount": 2000000,

        "kyc_verified": False
    }

    result = agent.evaluate(
        transaction
    )

    assert len(
        result["violations"]
    ) > 0