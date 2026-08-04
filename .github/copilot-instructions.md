# DataOps Nexus Repository Instructions

When reviewing this repository:

- Prioritize correctness, maintainability, security, and testability.
- Reject hard-coded credentials, secrets, tokens, and connection strings.
- Require type hints for public Python functions.
- Require clear docstrings for public modules, classes, and functions.
- Verify that error handling is explicit and meaningful.
- Check that logs are structured and do not expose sensitive data.
- Require tests for business-critical logic.
- Flag duplicated code and unnecessary complexity.
- Verify that documentation matches the implemented behavior.
- Do not mark planned features as implemented.
- Check database queries for parameterization.
- Check Kafka consumers for idempotency and duplicate handling.
- Check PySpark transformations for schema validation and data-quality rules.
- Verify that Bronze data remains immutable.
- Verify that Silver data is cleaned, validated, and quarantines invalid records.
- Verify that Gold data is business-ready and aggregated.
- Check Airflow tasks for retries, timeouts, and idempotency.
- Check Databricks and Delta code for schema evolution and MERGE correctness.
