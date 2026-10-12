"""
File: transaction_producer.py

Purpose:

Generate transaction events
for streaming simulation.
"""

import time


class TransactionProducer:

    def stream(self):

        sample_transactions = [

            {
                "transaction_id": "TXN001",
                "amount": 50000,
                "country": "India",
                "kyc_verified": True
            },

            {
                "transaction_id": "TXN002",
                "amount": 2500000,
                "country": "UAE",
                "kyc_verified": False
            }
        ]

        for transaction in sample_transactions:

            yield transaction

            time.sleep(1)