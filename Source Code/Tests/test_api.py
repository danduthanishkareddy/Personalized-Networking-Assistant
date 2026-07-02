from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)


def test_health_api():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "API is running successfully"


def test_analyze_event_api():
    response = client.post(
        "/analyze-event",
        json={"event_description": "AI for healthcare"}
    )
    assert response.status_code == 200
    assert "extracted_themes" in response.json()


def test_generate_conversation_api():
    response = client.post(
        "/generate-conversation",
        json={
            "event_description": "AI for sustainable cities",
            "interests": ["climate change"]
        }
    )
    assert response.status_code == 200
    assert "conversation_starters" in response.json()


def test_fact_check_api():
    response = client.post(
        "/fact-check",
        json={"topic": "Artificial intelligence"}
    )
    assert response.status_code == 200
    assert "summary" in response.json()


def test_history_api():
    response = client.get("/history")
    assert response.status_code == 200
    assert "history" in response.json()