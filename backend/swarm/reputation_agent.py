"""
Reputation Engine

Maintains trust scores
for swarm agents.
"""


class ReputationEngine:

    def update(

            self,

            previous_reputation,

            current_accuracy,

            alpha=0.8):

        reputation = (

            alpha
            * previous_reputation

            +

            (1 - alpha)
            * current_accuracy

        )

        return reputation