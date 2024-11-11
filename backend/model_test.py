import pytest
from data_formatter import DataFormatter
from data_reader import DataReader
from model import Model
from model_interactor import ModelInteractor

@pytest.fixture
def women_bias_data():
    real_data = DataReader("women_bias_data.csv").read_dataset()
    return real_data


def test_model(women_bias_data):
    filter_gender = 'Female'
    forecast_steps = 10
    training_data = (DataFormatter(women_bias_data)
                     .filter_by(filter_gender)
                     .filter_invalid_transactions()
                     .get_for_predicting())

    return_data = ModelInteractor(training_data).execute(forecast_steps)
    print(return_data)
    # should figure out some way of asserting something true.