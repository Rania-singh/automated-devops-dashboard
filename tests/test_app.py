from app import app


def test_home_returns_project_details():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    data = response.get_json()
    assert data["project"] == "CloudDevOps CI/CD Demo"
    assert data["status"] == "running"


def test_health_endpoint():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}
