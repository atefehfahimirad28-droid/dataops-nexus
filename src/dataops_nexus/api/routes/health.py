from fastapi import APIRouter, HTTPException, status
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from dataops_nexus.db.session import engine

router = APIRouter(tags=["health"])


@router.get("/health")
def health() -> dict[str, str]:
    """Check whether the API process is running."""
    return {"status": "ok"}


@router.get("/ready")
def readiness() -> dict[str, str]:
    """Check whether the API and database are ready to serve requests."""
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
    except SQLAlchemyError as exc:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Database is unavailable",
        ) from exc

    return {
        "status": "ready",
        "database": "connected",
    }
