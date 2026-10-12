"""
File: transaction_consumer.py

Purpose:

Consume transactions from
the producer.
"""

from backend.streaming.transaction_producer import (
    TransactionProducer
)

from backend.streaming.stream_processor import (
    StreamProcessor
)


class TransactionConsumer:

    def __init__(self):

        self.producer = (
            TransactionProducer()
        )

        self.processor = (
            StreamProcessor()
        )

    def consume(self):

        customer = {

            "customer_id": "CUS001",
            "income": 500000,
            "credit_score": 720
        }

        for transaction in self.producer.stream():

            result = self.processor.process(

                customer,

                transaction
            )

            print(result)