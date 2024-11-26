import pytest
from data_access.data_access_object import DataAccessObject


@pytest.fixture
def women_bias_data():
    real_data = DataAccessObject("women_bias_data.csv").read_dataset()
    return real_data
    