import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_getinfo(client):
    response = client.get('/getinfo')
    assert response.status_code == 200
    assert response.get_json() == {"name": "breaking bias", "score": "awesome"}

if __name__ == '__main__':
    pytest.main(['test_get_info.py'])
