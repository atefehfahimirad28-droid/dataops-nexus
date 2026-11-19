import os

import pytest
from sqlalchemy import inspect, text
from sqlalchemy.exc import SQLAlchemyError

from dataops_nexus.db.session import engine


@pytest.mark.skipif(
    os.getenv("RUN_DB_INTEGRATION_TESTS") != "1",
    reason="Set RUN_DB_INTEGRATION_TESTS=1 to enable database integration tests",
)
def test_postgres_connection_and_metadata_tables() -> None:
    expected_tables = {
        "pipelines",
        "datasets",
        "pipeline_runs",
        "data_quality_results",
    }

    try:
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 1"))
            assert result.scalar_one() == 1

        inspector = inspect(engine)
        actual_tables = set(inspector.get_table_names())

    except SQLAlchemyError as exc:
        pytest.fail(f"PostgreSQL integration test failed: {exc}")

    assert expected_tables.issubset(actual_tables)
