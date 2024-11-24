import pytest
import pandas as pd

from entity.graphing_data import GraphingData
from data_formatter import DataFormatter
from data_access.data_access_helper.data_reader import DataReader
from filter_interactor import FilterInteractor


@pytest.fixture
def sample_data():
    sample_data = pd.DataFrame({
        'Customer_ID': ['C001', 'C002', 'C003', 'C004', 'C005'],
        'confusion_value': ['FP', 'TN', 'TP', 'FN', 'FP'],
        'Transaction_Amount_USD': [100.00, 150.00, 200.00, 250.00, 300.00],
        'Gender': ['Female', 'Other', 'Male', 'Female', 'Female'],
        'Bias': [1, 0, 1, 0, 0]
    })
    return sample_data


@pytest.fixture
def real_data():
    real_data = DataReader("women_bias_data_test.csv").read_dataset().head(100)
    return real_data


def test_unbias(sample_data):
    """Test the unbias function."""
    unbiased_df = FilterInteractor(sample_data).unbias().get_df()

    # Check that the first row has been modified and bias undone
    assert (unbiased_df.iloc[0, 1] == 'TN')
    assert (unbiased_df.iloc[0, 4] == 0)

    assert unbiased_df.iloc[4, 1] == 'FP'


def test_unbias_no_fp_values(sample_data):
    """Edge case: Test unbias with no 'FP' values to modify."""
    no_fp_data = sample_data[sample_data['confusion_value'] == 'TN']
    unbiased_df = FilterInteractor(no_fp_data).unbias().get_df()
    pd.testing.assert_frame_equal(unbiased_df, no_fp_data)


def test_unbias_all_fp_values(sample_data):
    """Edge case: Test unbias with all 'FP' values."""
    all_fp_data = sample_data.copy()
    all_fp_data['confusion_value'] = 'FP'
    unbiased_df = FilterInteractor(all_fp_data).unbias().get_df()
    assert (unbiased_df['confusion_value'] == 'TN').sum() == (
                all_fp_data['Bias'] == 1).sum()


def test_filter_by_factor(sample_data):
    """Test the filter_by_factor function."""
    filtered_df = FilterInteractor(sample_data).filter_by(
        'Female').get_df()
    assert len(filtered_df) == 3
    assert (filtered_df['Gender'] == 'Female').all()


def test_filter_by_factor_no_matching_values(sample_data):
    """Edge case: Test filter_by_factor with no matching values."""
    filtered_df = FilterInteractor(sample_data).filter_by(
        'Nonexistent_gender',
        'Nonexistent_race',
        'Nonexistent_state'
    ).get_df()
    assert filtered_df.equals(sample_data)  # Should return the original dataset


def test_filter_by_factor_all_rows_match(sample_data):
    """Edge case: Test filter_by_factor where all rows match the value."""
    all_female_data = sample_data[sample_data['Gender'] == 'Female']
    filtered_df = FilterInteractor(sample_data).filter_by(
        'Female').get_df()
    pd.testing.assert_frame_equal(filtered_df, all_female_data)


def test_unbias_does_not_mutate_original(sample_data):
    """Test to ensure the original df is not mutated by the unbias function."""
    # Create a copy of the original DataFrame for comparison
    original_data_copy = sample_data.copy()

    # Call the unbias function
    unbiased_df = FilterInteractor(sample_data).unbias().get_df()

    # Mutate created df
    unbiased_df['Transaction_Amount_USD'] = 0

    # Assert that the original DataFrame is unchanged
    pd.testing.assert_frame_equal(sample_data, original_data_copy,
                                  check_dtype=True)


def test_get_revenue_data(real_data):
    revenue_data = GraphingData(pd.DataFrame({
        'date': [pd.to_datetime('2024-05-01').date(),
                 pd.to_datetime('2024-05-02').date()],
        'revenue': [1306375.68, 1361639.44]
    }))

    gotten_revenue_data = DataFormatter(real_data).get_revenue_data()

    pd.testing.assert_frame_equal(revenue_data.get_data(),
                                  gotten_revenue_data.get_data())

def test_get_frequency_data(real_data):
    frequency_data = GraphingData(pd.DataFrame({
        'date': [pd.to_datetime('2024-05-01').date(),
                 pd.to_datetime('2024-05-02').date()],
        'frequency': [52, 48]
    }))

    gotten_frequency_data = DataFormatter(real_data).get_frequency_data()

    pd.testing.assert_frame_equal(frequency_data.get_data(),
                                  gotten_frequency_data.get_data())
