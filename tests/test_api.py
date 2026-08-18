import os
import sys

# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from fastapi.testclient import TestClient

from app.main import app

test_app = TestClient(app)


def test_health_check_returns_ok() -> None:
    response = test_app.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_create_valid_job_returns_201() -> None:
    body = {
        "title": "Backend Engineer",
        "company": "Example Company",
        "url": "https://example.com/jobs/backend-engineer",
        "location": "Remote",
        "source": "company_site",
    }

    response = test_app.post("/job", json=body)
    assert response.status_code == 201


def test_create_invalid_job_returns_422() -> None:
    body = {
        "title": "1",
        "company": "Example Company",
        "url": "https://example.com/jobs/backend-engineer",
        "location": "Remote",
        "source": "company_site",
    }
    response = test_app.post("/job", json=body)
    assert response.status_code == 422
