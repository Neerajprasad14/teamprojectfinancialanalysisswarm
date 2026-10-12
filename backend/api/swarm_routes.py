"""
File Name:
swarm_routes.py

Purpose:

Main AgentFin-Swarm API.
"""

from fastapi import APIRouter

from backend.agents.coordinator_agent import (
    CoordinatorAgent
)

router = APIRouter()

coordinator = CoordinatorAgent()


@router.post("/analyze")
def analyze(payload: dict):

    return coordinator.process(

        payload["customer"],

        payload["transaction"]
    )