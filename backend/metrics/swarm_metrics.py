"""
File Name:
swarm_metrics.py

Purpose:

Measure swarm behaviour.

Research Metrics:

1. Consensus Time
2. Communication Cost
3. Agent Reliability
4. Swarm Efficiency

Research Contribution:

Provides publication-ready metrics.
"""


class SwarmMetrics:

    def reliability(
            self,
            successes,
            failures):

        total = successes + failures

        if total == 0:

            return 0

        return successes / total