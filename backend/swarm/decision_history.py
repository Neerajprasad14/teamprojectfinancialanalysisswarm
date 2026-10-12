"""
File Name:
decision_history.py

Purpose:

Store historical agent decisions.

Benefits:

1. Future analysis.
2. Reputation updates.
3. Auditing.
4. Model improvement.

Research Contribution:

Supports long-term swarm learning.
"""


class DecisionHistory:

    def __init__(self):

        self.history = []

    def add_decision(
            self,
            decision):

        self.history.append(
            decision
        )

    def get_all(self):

        return self.history