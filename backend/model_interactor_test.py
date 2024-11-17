from model_interactor import ModelInteractor
import pandas as pd
import pytest


@pytest.fixture
def sample_training_data():
    frequency_data = pd.DataFrame({
        'date': ['2021-01-01', '2021-01-02', '2021-01-03', '2021-01-04',
                 '2021-01-05'],
        'frequency': [100, 200, 300, 400, 500]
    })
    revenue_data = pd.DataFrame({
        'date': ['2021-01-01', '2021-01-02', '2021-01-03', '2021-01-04',
                 '2021-01-05'],
        'revenue': [10000, 20000, 30000, 40000, 50000]
    })
    return frequency_data, revenue_data


@pytest.fixture
def sample_df_with_missing_dates():
    df = pd.DataFrame({
        'date': ['2021-01-01', '2021-01-03', '2021-01-05'],
        'frequency': [100, 300, 500]
    })
    return df


def test_add_back_missing(sample_df_with_missing_dates):
    expected_df = pd.DataFrame({
        'date': ['2021-01-01', '2021-01-02', '2021-01-03', '2021-01-04',
                 '2021-01-05'],
        'frequency': [100, 0, 300, 0, 500]
    })
    assert (ModelInteractor._add_back_missing_dates(sample_df_with_missing_dates) ==
            expected_df)

def test_get_for_predicting(sample_training_data):
    ...
