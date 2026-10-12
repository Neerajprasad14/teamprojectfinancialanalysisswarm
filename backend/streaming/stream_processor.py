"""
File: stream_processor.py

Purpose:

Process incoming transactions
in real time.

Research Contribution:

Provides streaming capability
for AgentFin-Swarm.
"""

from backend.agents.coordinator_agent import (
    CoordinatorAgent
)


class StreamProcessor:

    def __init__(self):

        self.coordinator = (
            CoordinatorAgent()
        )

    def process(
            self,
            customer,
            transaction):

        return self.coordinator.process(

            customer,

            transaction
        )