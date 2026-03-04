from fastapi.testclient import TestClient
from api.app import app

client = TestClient(app)


def test_api_health():

    response = client.get("/")

    assert response.status_code == 200