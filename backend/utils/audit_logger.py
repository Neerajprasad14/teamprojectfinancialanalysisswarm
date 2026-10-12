"""
File Name:
audit_logger.py

Purpose:

Maintain an audit trail of every decision.

Why Needed?

Financial systems require:

1. Traceability
2. Accountability
3. Compliance auditing

Every decision produced by the swarm
must be logged.

Research Contribution:

Supports Explainable AI
and regulatory compliance.
"""

import logging

logging.basicConfig(

    filename="agentfin_audit.log",

    level=logging.INFO
)


def log_event(message):

    """
    Save activity.

    Input:
        Event message

    Output:
        Log record
    """

    logging.info(message)