from fastapi import FastAPI
from fastapi.testclient import TestClient
from fastapi.testclient import TestClient

from app.api.server import get_application

app = get_application()


client = TestClient(app)


def test_server_demo_route():
    response = client.get("/api/demo_route")
    assert response.status_code == 200
    assert response.json() == {"message":"Demo route for Limehome HMS"}