"""
File: swarm_model.py

Purpose:
Execute AgentFin-Swarm.

This experiment evaluates:

- Multi-agent architecture
- Consensus mechanism
- Reputation-aware intelligence

Research Contribution:
Validates the proposed swarm system.
"""

from agents.coordinator_agent import (
    CoordinatorAgent
)

swarm = CoordinatorAgent()

result = swarm.process(

    customer_data,

    transaction_data

)

print(result)