"""
Consensus Engine

Combines decisions from
multiple swarm agents.
"""


class ConsensusEngine:

    def calculate(

            self,

            risk,

            fraud,

            compliance):

        score = (

            risk["score"]
            * risk["confidence"]

            +

            fraud["score"]
            * fraud["confidence"]

            +

            compliance["score"]
            * compliance["confidence"]

        ) / 3

        return round(
            score,
            2
        )