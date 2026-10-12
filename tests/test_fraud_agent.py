"""
Test Fraud Agent
"""

from agents.fraud_agent import FraudAgent


def test_fraud_agent():

    agent = FraudAgent()

    sample = [

        100000,

        0,
        
        1
    ]

    result = agent.evaluate(
        sample
    )

    assert "score" in result