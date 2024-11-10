import pytest
import pandas as pd
from data_formatter import DataFormatter
from data_reader import DataReader
from model import Model

@pytest.fixture
def women_bias_data():
    real_data = DataReader("women_bias_data.csv").read_dataset()
    return real_data

trans_amount = pd.DataFrame({
    'date': [
        '2024-08-01', '2024-08-02', '2024-08-03', '2024-08-04', '2024-08-05',
        '2024-08-06', '2024-08-07', '2024-08-08', '2024-08-09', '2024-08-10'
    ],
    'value': [
        16.995673, 16.222627, 16.034839, 16.945018, 14.109536,
        14.770461, 14.904923, 13.969297, 18.254376, 15.256364
    ]
})

trans_count = pd.DataFrame({
    'date': [
        '2024-08-01', '2024-08-02', '2024-08-03', '2024-08-04', '2024-08-05',
        '2024-08-06', '2024-08-07', '2024-08-08', '2024-08-09', '2024-08-10'
    ],
    'value': [
        380355.198397, 309959.603093, 344232.402834, 310156.871630, 322884.728054,
        318517.260802, 313631.131515, 255724.795039, 352815.135615, 301532.155613
    ]
})

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

    pd.testing.assert_frame_equal(pred_trans_amount, trans_amount)
    pd.testing.assert_frame_equal(pred_trans_count, trans_count)