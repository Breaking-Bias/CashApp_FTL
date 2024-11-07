import pytest
import re
from datetime import datetime
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def is_valid_format(data) -> bool:
    # Check that data is a list
    if not isinstance(data, list):
        return False  # "Expected data to be a list of dictionaries"

    # Regex pattern for YYYY-MM-DD date format
    date_pattern = re.compile(r'^\d{4}-\d{2}-\d{2}$')

    # Check each item in the list
    for item in data:
        if not (isinstance(item, dict)  # "Each item in the list should be a dictionary"
        and 'date' in item # "Each dictionary should have a 'date' key"
        and 'value' in item # "Each dictionary should have a 'value' key"

        # Check date format
        and isinstance(item['date'], str) # "The 'date' key should have a string value"
        and date_pattern.match(item['date'])): # "The 'date' value should match the format YYYY-MM-DD"
            return False
        # Check if the date string is valid
        try:
            datetime.strptime(item['date'], "%Y-%m-%d")
        except ValueError:
            return False # f"The 'date' value '{item['date']}' is not a valid date"

        # Check value type
        if not isinstance(item['value'], int): # "The 'value' key should have an integer value"
            return False

    return True

def test_getinfo(client):
    response = client.get('/getinfo')
    assert response.status_code == 200
    assert response.json == {"name": 'breaking bias', "score": "awesome"}

def test_getPastData(client):
    response = client.post('/getPastData', json={'filtering_factor': 'Female'})
    assert response.status_code == 200
    # Ensure the response data is JSON
    try:
        data = response.json
    except ValueError:
        assert False, "Response is not valid JSON"

    assert is_valid_format(data), "Past data is not in the expected format"

def test_predictValues(client):
    response = client.post('/predictData', json={'num_points': 10, 'filtering_factor': 'Female'})
    assert response.status_code == 200
    # Ensure the response data is JSON
    try:
        data = response.json
    except ValueError:
        assert False, "Response is not valid JSON"

    assert is_valid_format(data), "Predicted data is not in the expected format"

def test_getPastDataUnbiased(client):
    response = client.post('/getPastDataUnbiased', json={'filtering_factor': 'Female'}) # This should be unbiased data by default)
    assert response.status_code == 200
    # Ensure the response data is JSON
    try:
        data = response.json
    except ValueError:
        assert False, "Response is not valid JSON"

    assert is_valid_format(data), "Past data is not in the expected format"

def test_predictValuesUnbiased(client):
    response = client.post('/predictDataUnbiased', json={'num_points': 10, 'filtering_factor': 'Female'})
    assert response.status_code == 200
    # Ensure the response data is JSON
    try:
        data = response.json
    except ValueError:
        assert False, "Response is not valid JSON"

    assert is_valid_format(data), "Predicted data is not in the expected format"

def test_cicd_test(client):
    response = client.get('/cicd_test')
    assert response.status_code == 200
    assert response.json == "Hello World"
