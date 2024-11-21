import pytest
from data_formatter import DataFormatter
from data_reader import DataReader
from model import Model
from model_interactor import ModelInteractor


@pytest.fixture
def women_bias_data():
    real_data = DataReader("women_bias_data.csv").read_dataset()
    return real_data
    