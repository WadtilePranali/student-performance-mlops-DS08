import pytest
from app import app, estimate_performance

@pytest.fixture()
def client():
    app.config.update(TESTING=True)
    with app.test_client() as client:
        yield client

def test_home_page_loads(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Student Performance Demo" in response.data

def test_health_endpoint(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json()["status"] == "ok"

def test_estimation_categories():
    assert estimate_performance(16, 100) == "High"
    assert estimate_performance(8, 50) == "Moderate"
    assert estimate_performance(0, 0) == "Needs Support"

def test_form_submission(client):
    response = client.post("/", data={"study_hours": "8", "attendance": "80"})
    assert response.status_code == 200
    assert b"Demo result" in response.data
