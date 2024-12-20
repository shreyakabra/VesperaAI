import pytest
from app import app

@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

def test_generate_story(client):
    response = client.post('/generate_story', json={
        "prompt": "Once upon a time...",
        "max_length": 100,
        "temperature": 0.7,
        "mode": "fantasy"
    })
    assert response.status_code == 200
    assert "story" in response.json

def test_save_story(client):
    response = client.post('/save_story', json={
        "title": "Sample Title",
        "prompt": "Sample Prompt",
        "story": "This is a test story."
    })
    assert response.status_code == 200
    assert response.json["message"] == "Story saved successfully!"
