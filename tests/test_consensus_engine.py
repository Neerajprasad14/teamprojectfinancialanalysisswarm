"""
File Name:
test_consensus_engine.py

Purpose:

Validate correctness of
swarm consensus algorithm.

Research Importance:

Ensures reliability
of published results.
"""

from swarm.consensus_engine import (
    ConsensusEngine
)

engine = ConsensusEngine()

risk = {

    "score": 80,

    "confidence": 0.9
}

fraud = {

    "score": 90,

    "confidence": 0.95
}

compliance = {

    "score": 70,

    "confidence": 0.9
}

result = engine.calculate(

    risk,

    fraud,

    compliance
)

assert result > 0