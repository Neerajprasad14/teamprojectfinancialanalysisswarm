from fastapi import APIRouter

from backend.database.repository import (
    TransactionRepository
)

router = APIRouter()

repo = TransactionRepository()


@router.get("/transactions")
def get_transactions():

    data = repo.get_all()

    return [

        {
            "id": row.id,
            "transaction_id": row.transaction_id,
            "customer_id": row.customer_id,
            "final_score": row.final_score
        }

        for row in data
    ]