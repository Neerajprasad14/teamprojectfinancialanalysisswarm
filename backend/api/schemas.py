"""
Pydantic Request Schemas
"""

from pydantic import BaseModel


class CustomerRequest(
    BaseModel
):

    customer_id: str

    income: float

    credit_score: int


class TransactionRequest(
    BaseModel
):

    transaction_id: str

    amount: float

    country: str

    kyc_verified: bool