from fastapi import APIRouter

from backend.database.db import (
    engine
)

router = APIRouter()


@router.get("/health")
def health():

    try:

        with engine.connect():
            database_status = (
                "Connected"
            )

    except Exception:

        database_status = (
            "Disconnected"
        )

    return {

        "service":
        "AgentFin-Swarm",

        "status":
        "Healthy",

        "database":
        database_status
    }