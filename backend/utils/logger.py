"""
Central Logging Module
"""

import logging

logging.basicConfig(

    filename="agentfin.log",

    level=logging.INFO,

    format=
    "%(asctime)s - %(message)s"
)


def write_log(message):

    logging.info(
        message
    )