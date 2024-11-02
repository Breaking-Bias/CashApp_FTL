import pytest
import re
from datetime import datetime
from backend.app import app

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
    # Ensure the response data is JSON
    try:
        data = response.json
    except ValueError:
        assert False, "Response is not valid JSON"

    # Check that data is a list
    assert isinstance(data, list), "Expected data to be a list of dictionaries"

    # Regex pattern for YYYY-MM-DD date format
    date_pattern = re.compile(r'^\d{4}-\d{2}-\d{2}$')

    # Check each item in the list
    for item in data:
        assert isinstance(item, dict), "Each item in the list should be a dictionary"
        assert 'date' in item, "Each dictionary should have a 'date' key"
        assert 'value' in item, "Each dictionary should have a 'value' key"

        # Check date format
        assert isinstance(item['date'], str), "The 'date' key should have a string value"
        assert date_pattern.match(item['date']), "The 'date' value should match the format YYYY-MM-DD"

        # Check if the date string is valid
        try:
            datetime.strptime(item['date'], "%Y-%m-%d")
        except ValueError:
            assert False, f"The 'date' value '{item['date']}' is not a valid date"

        # Check value type
        assert isinstance(item['value'], int), "The 'value' key should have an integer value"

def test_predictValues(client):
    response = client.post('/predictValues', json={'numPoints': 10})
    assert response.status_code == 200
    # Ensure the response data is JSON
    try:
        data = response.json
    except ValueError:
        assert False, "Response is not valid JSON"

    # Check that data is a list
    assert isinstance(data, list), "Expected data to be a list of dictionaries"

    # Regex pattern for YYYY-MM-DD date format
    date_pattern = re.compile(r'^\d{4}-\d{2}-\d{2}$')

    # Check each item in the list
    for item in data:
        assert isinstance(item, dict), "Each item in the list should be a dictionary"
        assert 'date' in item, "Each dictionary should have a 'date' key"
        assert 'value' in item, "Each dictionary should have a 'value' key"

        # Check date format
        assert isinstance(item['date'], str), "The 'date' key should have a string value"
        assert date_pattern.match(item['date']), "The 'date' value should match the format YYYY-MM-DD"

        # Check if the date string is valid
        try:
            datetime.strptime(item['date'], "%Y-%m-%d")
        except ValueError:
            assert False, f"The 'date' value '{item['date']}' is not a valid date"

        # Check value type
        assert isinstance(item['value'], int), "The 'value' key should have an integer value"

def test_cicd_test(client):
    response = client.get('/cicd_test')
    assert response.status_code == 200
    assert response.json == "Hello World"
