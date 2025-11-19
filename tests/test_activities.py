import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

# Ensure the Soccer activity exists before running tests
def setup_module(module):
    # Ensure the Soccer activity exists before running tests
    client.post("/activities", json={
        "name": "Soccer",
        "description": "Join the school soccer team and compete in matches",
        "schedule": "Wednesdays, 4:00 PM - 5:30 PM",
        "max_participants": 22,
        "participants": []
    })


def test_get_activities():
    response = client.get("/activities")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)


def test_signup_activity():
    payload = {"email": "test@example.com"}
    response = client.post("/activities/Soccer/signup", json=payload)
    assert response.status_code == 200 or response.status_code == 400
    assert "message" in response.json()


def test_unregister_activity():
    # Ensure the participant is registered first
    client.post("/activities/Soccer/signup", json={"email": "test@example.com"})

    payload = {"participant": "test@example.com"}
    response = client.post("/activities/Soccer/unregister", json=payload)
    assert response.status_code == 200 or response.status_code == 400
    assert "message" in response.json()