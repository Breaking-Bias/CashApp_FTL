import pytest
import pandas as pd
from data_formatter import DataFormatter
from data_reader import DataReader
from model import Model

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

    pred_trans_amount = Model(training_data[0]).predict().get_result(forecast_steps)
    pred_trans_count = Model(training_data[1]).predict().get_result(forecast_steps)

    pred_trans_amount = DataFormatter.helper_datetime_to_string(pred_trans_amount)
    pred_trans_count = DataFormatter.helper_datetime_to_string(pred_trans_count)

    # should figure out some way of asserting something true.