from unittest.mock import patch

from fastapi.testclient import TestClient
from sqlalchemy.exc import OperationalError

from dataops_nexus.main import app

client = TestClient(app)


def test_health_returns_ok() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_ready_when_database_available() -> None:
    with patch("dataops_nexus.api.routes.health.engine") as mock_engine:
        response = client.get("/ready")

    assert response.status_code == 200
    assert response.json() == {
        "status": "ready",
        "database": "connected",
    }
    mock_engine.connect.assert_called_once()


def test_ready_when_database_unavailable() -> None:
    with patch("dataops_nexus.api.routes.health.engine") as mock_engine:
        mock_engine.connect.side_effect = OperationalError(
            "SELECT 1", {}, Exception("Database unavailable")
        )

        response = client.get("/ready")

    assert response.status_code == 503
    assert response.json() == {"detail": "Database is unavailable"}
