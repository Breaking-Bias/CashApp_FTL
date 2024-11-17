import datetime
from graphing_data import GraphingData
from model_interactor import ModelInteractor
import pandas as pd
import pytest


@pytest.fixture
def sample_onecol():
    df = pd.DataFrame({
        'date': [datetime.date(2021, 1, 1),
                 datetime.date(2021, 1, 2),
                 datetime.date(2021, 1, 3),
                 datetime.date(2021, 1, 4),
                 datetime.date(2021, 1, 5)],
        'frequency': [100, 200, 300, 400, 500]
    })
    df.set_index('date', inplace=True)
    return df

@pytest.fixture
def sample_graphingdata():
    df = pd.DataFrame({
        'date': [datetime.date(2021, 1, 1),
                 datetime.date(2021, 1, 2),
                 datetime.date(2021, 1, 3),
                 datetime.date(2021, 1, 4),
                 datetime.date(2021, 1, 5)],
        'frequency': [100, 200, 300, 400, 500]
    })
    return GraphingData(df)

@pytest.fixture
def sample_training_data():
    frequency_data = pd.DataFrame({
        'date': [datetime.date(2021, 1, 1),
                 datetime.date(2021, 1, 2),
                 datetime.date(2021, 1, 3),
                 datetime.date(2021, 1, 4),
                 datetime.date(2021, 1, 5)],
        'frequency': [100, 200, 300, 400, 500]
    })
    revenue_data = pd.DataFrame({
        'date': [datetime.date(2021, 1, 1),
                 datetime.date(2021, 1, 2),
                 datetime.date(2021, 1, 3),
                 datetime.date(2021, 1, 4),
                 datetime.date(2021, 1, 5)],
        'revenue': [10000, 20000, 30000, 40000, 50000]
    })
    return GraphingData(frequency_data), GraphingData(revenue_data)



@pytest.fixture
def sample_graphingdata_with_missing_dates():
    df = pd.DataFrame({
        'date': [datetime.date(2021, 1, 1),
                 datetime.date(2021, 1, 3),
                 datetime.date(2021, 1, 5)],
        'frequency': [100, 300, 500]
    })
    return GraphingData(df)


def test_add_back_missing(sample_graphingdata_with_missing_dates):
    expected_df = pd.DataFrame({
        'date': [datetime.date(2021, 1, 1),
                 datetime.date(2021, 1, 2),
                 datetime.date(2021, 1, 3),
                 datetime.date(2021, 1, 4),
                 datetime.date(2021, 1, 5)],
        'frequency': [100, 0, 300, 0, 500]
    })
    assert (ModelInteractor._add_back_missing_dates(
        sample_graphingdata_with_missing_dates) == expected_df)


def test_add_back_missing_unchanged(sample_training_data):
    """With data with no missing dates, the dataframe should not change."""
    expected_df =

def test_get_for_predicting(sample_training_data):
    ...
