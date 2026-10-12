"""
File: coordinator_agent.py

Purpose:

Coordinate all agents,
aggregate results,
and persist assessments.
"""

from backend.agents.risk_agent import (
    RiskAgent
)

from backend.agents.fraud_agent import (
    FraudAgent
)

from backend.agents.compliance_agent import (
    ComplianceAgent
)

from backend.swarm.consensus_engine import (
    ConsensusEngine
)

from backend.database.repository import (
    TransactionRepository
)

class CoordinatorAgent:

    def __init__(self):

        self.risk = RiskAgent()

        self.fraud = FraudAgent()

        self.compliance = (
            ComplianceAgent()
        )

        self.consensus = (
            ConsensusEngine()
        )

        self.repository = (
            TransactionRepository()
        )

    def process(
            self,
            customer,
            transaction):

        risk = self.risk.evaluate(
            customer
        )

        fraud = self.fraud.evaluate(
            transaction
        )

        compliance = (
            self.compliance.evaluate(
                transaction
            )
        )

        final_score = (
            self.consensus.calculate(
                risk,
                fraud,
                compliance
            )
        )

        self.repository.save({

            "transaction_id":

            transaction.get(
                "transaction_id",
                "TXN_UNKNOWN"
            ),

            "customer_id":

            customer.get(
                "customer_id",
                "CUS_UNKNOWN"
            ),

            "risk_score":
            risk["score"],

            "fraud_score":
            fraud["score"],

            "compliance_score":
            compliance["score"],

            "final_score":
            final_score,

            "threat_level":

            "HIGH"

            if final_score >= 80

            else "LOW",

            "evidence":
            "Consensus Engine Assessment"
        })

        return {

            "risk":
            risk,

            "fraud":
            fraud,

            "compliance":
            compliance,

            "final_score":
            final_score
        }