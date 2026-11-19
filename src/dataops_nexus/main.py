from fastapi import FastAPI

from dataops_nexus.api.routes.health import router as health_router

app = FastAPI(
    title="DataOps Nexus API",
    version="0.1.0",
    description="Backend API for the DataOps Nexus platform.",
)

app.include_router(health_router)
