import pytest
from src.app import app

@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

def test_index(client):
    resp = client.get('/')
    assert resp.status_code == 200
    assert resp.get_json() == {"message": "Hello, DevOps CI/CD!"}

# תוכל להוסיף כאן בדיקה ל-/cicd-test לאחר שתריץ אותה
