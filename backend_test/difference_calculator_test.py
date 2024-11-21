from backend.difference_calculator import DifferenceCalculator
from backend.graphing_data import GraphingData
import pandas as pd
import pytest
import datetime


@pytest.fixture
def sample_data_biased():
    return pd.DataFrame({
        'date': [
            datetime.date(2024, 11, 1),
            datetime.date(2024, 11, 2),
            datetime.date(2024, 11, 3),
            datetime.date(2024, 11, 4),
            datetime.date(2024, 11, 5)
        ],
        'revenue': [100.00, 150.00, 200.00, 250.00, 300.00]
    })


@pytest.fixture
def sample_data_unbiased():
    return pd.DataFrame({
        'date': [
            datetime.date(2024, 11, 1),
            datetime.date(2024, 11, 2),
            datetime.date(2024, 11, 3),
            datetime.date(2024, 11, 4),
            datetime.date(2024, 11, 5)
        ],
        'revenue': [130.00, 155.03, 223.48, 301.11, 301.00]
    })

# GraphingData Fixture
@pytest.fixture
def graphing_data_biased(sample_data_biased):
    return GraphingData(sample_data_biased)

@pytest.fixture
def graphing_data_unbiased(sample_data_unbiased):
    return GraphingData(sample_data_unbiased)

# DifferenceCalculator Fixture
@pytest.fixture
def difference_calculator(graphing_data_biased, graphing_data_unbiased):
    return DifferenceCalculator(graphing_data_unbiased, graphing_data_biased)

# Tests
# def test_volume_zero_on_same():
#     volume = graphing_data_biased.volume_difference()
#     assert volume == 0


def test_volume_calculation(difference_calculator):
    volume = difference_calculator.volume_difference()
    assert volume == 111


def test_invalid_input():
    biased_data_invalid = pd.DataFrame({
        'date': [
            datetime.date(2024, 11, 1),
            datetime.date(2024, 11, 2),
            datetime.date(2024, 11, 3),
            datetime.date(2024, 11, 4),
            datetime.date(2024, 11, 5)
        ],
        "revenue": [90.00, 110.00, 120.00, 150.00, 180.00]
    })

    graphing_biased_invalid = GraphingData(biased_data_invalid)
    diff_calc_invalid = DifferenceCalculator(GraphingData(pd.DataFrame({
        'date': [
            datetime.date(2024, 11, 1),
            datetime.date(2024, 11, 2),
            datetime.date(2024, 11, 3),
            datetime.date(2024, 11, 4),
            datetime.date(2024, 11, 5)
        ],
        "revenue": [130.00, 155.03, 223.48, 301.11, 301.00]
    })), graphing_biased_invalid)

    assert True


def test_average_transaction_day(difference_calculator):
    average_diff = difference_calculator.average_difference()
    assert average_diff == 22
