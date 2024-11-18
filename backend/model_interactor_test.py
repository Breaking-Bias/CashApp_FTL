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
def sample_training_tuple_df():
    frequency_data = pd.DataFrame({
        'date': [datetime.date(2021, 1, 1),
                 datetime.date(2021, 1, 2),
                 datetime.date(2021, 1, 3),
                 datetime.date(2021, 1, 4),
                 datetime.date(2021, 1, 5)],
        'frequency': [100, 200, 300, 400, 500]
    })
    frequency_data.set_index('date', inplace=True)
    revenue_data = pd.DataFrame({
        'date': [datetime.date(2021, 1, 1),
                 datetime.date(2021, 1, 2),
                 datetime.date(2021, 1, 3),
                 datetime.date(2021, 1, 4),
                 datetime.date(2021, 1, 5)],
        'revenue': [10000, 20000, 30000, 40000, 50000]
    })
    revenue_data.set_index('date', inplace=True)
    return frequency_data, revenue_data


@pytest.fixture
def sample_graphingdata_with_missing_dates():
    df = pd.DataFrame({
        'date': [datetime.date(2021, 1, 1),
                 datetime.date(2021, 1, 3),
                 datetime.date(2021, 1, 5)],
        'frequency': [100, 300, 500]
    })
    return GraphingData(df)


def test_graphingdata_to_onecol(sample_graphingdata, sample_onecol):
    assert (ModelInteractor._graphingdata_to_onecol(sample_graphingdata)
            .equals(sample_onecol))


def test_onecol_to_graphingdata(sample_onecol, sample_graphingdata):
    assert (ModelInteractor._onecol_to_graphingdata(sample_onecol)
            .equals(sample_graphingdata))


def test_add_back_missing(sample_graphingdata_with_missing_dates):
    expected_df = pd.DataFrame({
        'date': [datetime.date(2021, 1, 1),
                 datetime.date(2021, 1, 2),
                 datetime.date(2021, 1, 3),
                 datetime.date(2021, 1, 4),
                 datetime.date(2021, 1, 5)],
        'frequency': [100, 0, 300, 0, 500]
    })
    expected_df.set_index('date', inplace=True)
    assert (ModelInteractor._add_back_missing_dates(
        sample_graphingdata_with_missing_dates).equals(expected_df))


def test_add_back_missing_unchanged(sample_graphingdata):
    """With data with no missing dates, the dataframe should not change."""
    expected_df = ModelInteractor._graphingdata_to_onecol(sample_graphingdata)
    assert (ModelInteractor._add_back_missing_dates(sample_graphingdata)
            .equals(expected_df))


def test_get_for_predicting(sample_training_data, sample_training_tuple_df):
    model_interactor = ModelInteractor(sample_training_data)
    assert (model_interactor.get_for_predicting()[0]
            .equals(sample_training_tuple_df[0]))
    assert (model_interactor.get_for_predicting()[1]
            .equals(sample_training_tuple_df[1]))


def test_execute(sample_training_data):
    model_interactor = ModelInteractor(sample_training_data)
    pred_frequency, pred_revenue = model_interactor.execute(forecast_steps=3)
    assert isinstance(pred_frequency, GraphingData)
    assert isinstance(pred_revenue, GraphingData)

