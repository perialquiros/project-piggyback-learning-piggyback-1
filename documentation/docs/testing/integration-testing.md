---
sidebar_position: 2
---
# Integration tests

All integration tests are in `tests/test_integration.py` and use FastAPI's `TestClient` to simulate HTTP requests without running a real server.

## check_answer
Tests the `/api/check_answer` endpoint which combines request parsing, text normalization, and fuzzy matching.

| Test Case | Input | Expected Result |
|---|---|---|
| Correct answer | `expected: "dog", user: "dog"` | `status 200`, `status: "correct"` |
| Wrong answer | `expected: "dog", user: "cat"` | `status 200`, `status: "wrong"` |

## get_config
Tests the `/api/config` endpoint which returns app configuration used by the frontend.

| Test Case | Input | Expected Result |
|---|---|---|
| Config loads successfully | `GET /api/config` | `status 200`, contains `"thresholds"` |