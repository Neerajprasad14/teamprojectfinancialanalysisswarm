"""
File Name:
digital_twin_test.py

Purpose:

Evaluate AgentFin using a
synthetic banking environment.

Generated Entities:

1. Customers
2. Accounts
3. Transactions
4. Fraudsters

Research Contribution:

Digital Twin Banking Simulation.
"""

from simulator.bank_simulator import (
    BankSimulator
)

simulator = BankSimulator()

for i in range(10):

    print(

        simulator.generate_transaction()

    )