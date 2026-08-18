# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fastapi.testclient import TestClient

from app.main import app, jobs, id_counter
import pytest

test_app = TestClient(app)

@pytest.fixture(autouse=True)
def clear_jobs() -> None:
    jobs.clear()

def test_health_check_returns_ok() -> None:
    response = test_app.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_create_valid_job_returns_201_and_body() -> None:
    body = {
        "title": "Backend Engineer",
        "company": "Example Company",
        "url": "https://example.com/jobs/backend-engineer",
        "location": "Remote",
        "source": "company_site",
    }

    response = test_app.post("/jobs", json=body)
    response_data = response.json()
    assert response.status_code == 201
    assert response_data['id']==next(id_counter)-1
    assert response_data['title'] == body['title']
    assert response_data['company'] == body['company']
    assert response_data['url'] == body['url']
    assert response_data['location'] == body['location']
    assert response_data['source'] == body['source']


def test_create_invalid_job_returns_422() -> None:
    body = {
        "title": "1",
        "company": "Example Company",
        "url": "https://example.com/jobs/backend-engineer",
        "location": "Remote",
        "source": "company_site",
    }
    response = test_app.post("/jobs", json=body)
    assert response.status_code == 422
    assert response.json()['detail']

def test_check_jobs_list() -> None:
    response=test_app.get('/jobs')
    response_data = response.json()
    assert response_data == []
    
