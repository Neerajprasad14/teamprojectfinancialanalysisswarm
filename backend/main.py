"""
Application Entry Point
"""

from fastapi import FastAPI

from backend.api.health_routes import (
    router as health_router
)

from backend.api.risk_routes import (
    router as risk_router
)

from backend.api.fraud_routes import (
    router as fraud_router
)

from backend.api.compliance_routes import (
    router as compliance_router
)

from backend.api.regulation_routes import (
    router as regulation_router
)

from backend.api.swarm_routes import (
    router as swarm_router
)

from backend.api.database_routes import (
    router as database_router
)

app = FastAPI(
    title="AgentFin-Swarm"
)

app.include_router(
    health_router,
    tags=["Health"]
)

app.include_router(
    risk_router,
    tags=["Risk"]
)

app.include_router(
    fraud_router,
    tags=["Fraud"]
)

app.include_router(
    compliance_router,
    tags=["Compliance"]
)

app.include_router(
    regulation_router,
    tags=["Regulation"]
)

app.include_router(
    swarm_router,
    tags=["Swarm"]
)

app.include_router(
    database_router,
    tags=["Database"]
)

from backend.agents.regulation_agent import (
    RegulationAgent
)


@app.get("/debug-rules")
def debug_rules():

    agent = RegulationAgent()

    return agent.get_rules()