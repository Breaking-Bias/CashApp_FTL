import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_getinfo(client):
    response = client.get('/getinfo')
    assert response.status_code == 200
    assert response.json == {"name": 'breaking bias', "score": "awesome"}

def test_getOriginalData(client):
    response = client.get('/getOriginalData')
    assert response.status_code == 200
    # Add more assertions based on the expected data format

def test_predictValues(client):
    response = client.post('/predictValues', json={'numPoints': 10})
    assert response.status_code == 200
    # Add more assertions based on the expected prediction results

def test_cicd_test(client):
    response = client.get('/cicd_test')
    assert response.status_code == 200
    assert response.json == "Hello World"
