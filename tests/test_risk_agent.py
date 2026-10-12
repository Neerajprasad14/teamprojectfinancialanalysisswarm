"""
Test Risk Agent
"""

from agents.risk_agent import RiskAgent


def test_risk_agent():

    agent = RiskAgent()

    sample = [

        50000,

        750,

        200000
    ]

    result = agent.evaluate(
        sample
    )

    assert "score" in result