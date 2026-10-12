"""
File: bank_simulator.py

Purpose:
Create synthetic banking transactions.

Used for:

1. System testing
2. Experimental evaluation
3. Stress testing
4. Scalability testing

Research Contribution:
Provides Digital Twin Simulation
for AgentFin-Swarm.
"""

import random


class BankSimulator:
    """
    Generates synthetic banking events.
    """

    def generate_transaction(self):
        """
        Create a synthetic transaction.

        Returns:
            dict
        """

        return {

            "amount":

            random.randint(
                1000,
                5000000
            ),

            "country":

            random.choice([
                "India",
                "UAE",
                "Singapore",
                "USA"
            ]),

            "kyc_verified":

            random.choice([
                True,
                False
            ])
        }


if __name__ == "__main__":

    simulator = BankSimulator()

    print(
        simulator.generate_transaction()
    )