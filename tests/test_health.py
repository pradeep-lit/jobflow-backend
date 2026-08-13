import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from fastapi.testclient import TestClient

from app.main import app

test_app = TestClient(app)


def test_health_check_returns_ok() -> None:
    response = test_app.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
