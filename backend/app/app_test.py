import json
import pytest
import re
from datetime import datetime
from app.app import App


@pytest.fixture
def client():

    app_instance = App()
    app = app_instance.get_app()

    with app.test_client() as client:
        yield client


def is_valid_format(response_data) -> bool:
    # Check that data is a list
    if not isinstance(response_data[0], list):
        return False  # "Expected data to be a list of dictionaries"
    if not isinstance(response_data[1], list):
        return False  # "Expected data to be a list of dictionaries"

    # Regex pattern for YYYY-MM-DD date format
    date_pattern = re.compile(r'^\d{4}-\d{2}-\d{2}$')

    # Check each item in the list
    for dictionary in response_data:
        for item in dictionary:
            # "Each item in the list should be a dictionary"
            if (not (isinstance(item, dict)
                     # "Each dictionary should have a 'date' key"
                     and 'date' in item
                     # "Each dictionary should have a 'value' key"
                     and ('value' in item)
                     # "The 'date' key should have a string value"
                     and isinstance(item['date'], str)
                     # "The 'date' value should match the format YYYY-MM-DD"
                     and date_pattern.match(item['date']))):
                print('The date value should match the format YYYY-MM-DD')
                return False
            # Check if the date string is valid
            try:
                datetime.strptime(item['date'], "%Y-%m-%d")
            except ValueError:
                print("The 'date' value '{item['date']}' is not a valid date")
                # f"The 'date' value '{item['date']}' is not a valid date"
                return False

    for item in response_data[0]:
        # Check value type
        # "The 'frequency' or 'revenue' key should have an float value"
        if not isinstance(item['value'], (int, float)):
            print("The 'frequency' or 'revenue' key should have a float value")
            return False
    for item in response_data[1]:
        # Check value type
        # "The 'value' key should have an integer value"
        if not isinstance(item['value'], float):
            print("The 'value' key should have an integer value")
            return False

    return True


def test_getinfo(client):
    response = client.get('/getinfo')
    assert response.status_code == 200
    assert response.json == {"name": 'breaking bias', "score": "stupendous"}


def test_get_past_data(client):
    response = client.post('/getPastData',
                           json={'filtering_factor': [None, None]})

    assert response.status_code == 200
    # Ensure the response data is JSON
    try:
        frequency_graph = response.json['frequency_graph']
        revenue_graph = response.json['revenue_graph']
    except ValueError:
        assert False, "Response is not valid JSON"

    assert is_valid_format((frequency_graph['past_biased_line'],
                            revenue_graph['past_biased_line'])), \
        "Past data is not in the expected format"


def test_get_graph_data(client):
    response = client.post('/getGraphData',
                           json=({'num_points': 30,
                                  'filtering_factor': [None, None]}))
    assert response.status_code == 200
    with open('../response_log.json', 'w') as f:
        json.dump(response.json, f, indent=4)
