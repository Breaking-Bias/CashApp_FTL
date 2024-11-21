import pytest
from backend.data_reader import DataReader


@pytest.fixture
def women_bias_data():
    real_data = DataReader("women_bias_data.csv").read_dataset()
    return real_data