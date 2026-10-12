"""
Regulation API
"""

from fastapi import APIRouter

from backend.agents.regulation_agent import (
    RegulationAgent
)

router = APIRouter()

regulation_agent = RegulationAgent()


@router.get("/regulations")
def get_regulations():

    return regulation_agent.get_rules()