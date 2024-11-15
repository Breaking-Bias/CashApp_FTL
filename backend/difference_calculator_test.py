from difference_calculator import DifferenceCalculator
import pandas as pd
import pytest


@pytest.fixture
def sample_data_biased():
    sample_data_biased = pd.DataFrame({
        'Date': ['1', '2', '3', '4', '5'],
        'Transaction_Amount_USD': [100.00, 150.00, 200.00, 250.00, 300.00]
    })
    return sample_data_biased


@pytest.fixture
def sample_data_unbiased():
    sample_data_unbiased = pd.DataFrame({
        'Date': ['1', '2', '3', '4', '5'],
        'Transaction_Amount_USD': [130.00, 155.03, 223.48, 301.11, 301.00]
    })
    return sample_data_unbiased

def test_volume_zero_on_same(sample_data_biased):
    volume = DifferenceCalculator.volume(sample_data_biased,
                                         sample_data_biased)

    assert volume == 0


def test_volume_calculation(sample_data_biased, sample_data_unbiased):
    volume = DifferenceCalculator.volume(sample_data_unbiased,
                                         sample_data_biased)

    assert volume == 111