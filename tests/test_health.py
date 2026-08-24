from dataops_nexus.health import get_platform_status


def test_get_platform_status_returns_healthy() -> None:
    assert get_platform_status() == "healthy"
