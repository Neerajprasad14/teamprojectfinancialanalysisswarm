from sqlalchemy.orm import declarative_base

from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    Text,
    TIMESTAMP
)

from sqlalchemy.sql import func

Base = declarative_base()


class Transaction(Base):

    __tablename__ = "transactions"

    id = Column(
        Integer,
        primary_key=True
    )

    transaction_id = Column(
        String(50)
    )

    customer_id = Column(
        String(50)
    )

    risk_score = Column(
        Float
    )

    fraud_score = Column(
        Float
    )

    compliance_score = Column(
        Float
    )

    final_score = Column(
        Float
    )

    threat_level = Column(
        String(20)
    )

    evidence = Column(
        Text
    )

    created_at = Column(
        TIMESTAMP,
        server_default=func.now()
    )