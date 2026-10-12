"""
File Name:
confidence_calculator.py

Purpose:

Standardize confidence scores
across all agents.

Research Contribution:

Improves consistency of consensus
calculations.
"""


class ConfidenceCalculator:

    def normalize(
            self,
            value):

        if value > 1:

            return 1

        if value < 0:

            return 0

        return value