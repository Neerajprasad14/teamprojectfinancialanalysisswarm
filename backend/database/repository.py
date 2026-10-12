"""
File Name:
repository.py

Purpose:

Repository layer for database operations.
"""

from backend.database.db import SessionLocal
from backend.database.models import Transaction


class TransactionRepository:

    def save(self, data):

        session = SessionLocal()

        try:

            transaction = Transaction(

                transaction_id=data["transaction_id"],

                customer_id=data["customer_id"],

                risk_score=data["risk_score"],

                fraud_score=data["fraud_score"],

                compliance_score=data["compliance_score"],

                final_score=data["final_score"],

                threat_level=data["threat_level"],

                evidence=data["evidence"]
            )

            session.add(transaction)

            session.commit()

        except Exception as error:

            session.rollback()

            print(
                f"Database Error: {error}"
            )

        finally:

            session.close()

    def get_all(self):

        session = SessionLocal()

        try:

            records = session.query(
                Transaction
            ).all()

            return records

        finally:

            session.close()