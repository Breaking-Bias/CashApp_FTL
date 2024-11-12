import pytest
import pandas as pd
from data_formatter import DataFormatter
from data_reader import DataReader


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
    unbiased_df = DataFormatter(sample_data).unbias().get_formatted_df()

    # Check that the first row has been modified and bias undone
    assert (unbiased_df.iloc[0, 1] == 'TN')
    assert (unbiased_df.iloc[0, 4] == 0)

    assert unbiased_df.iloc[4, 1] == 'FP'


def test_unbias_no_fp_values(sample_data):
    """Edge case: Test unbias with no 'FP' values to modify."""
    no_fp_data = sample_data[sample_data['confusion_value'] == 'TN']
    unbiased_df = DataFormatter(no_fp_data).unbias().get_formatted_df()
    pd.testing.assert_frame_equal(unbiased_df, no_fp_data)


def test_unbias_all_fp_values(sample_data):
    """Edge case: Test unbias with all 'FP' values."""
    all_fp_data = sample_data.copy()
    all_fp_data['confusion_value'] = 'FP'
    unbiased_df = DataFormatter(all_fp_data).unbias().get_formatted_df()
    assert (unbiased_df['confusion_value'] == 'TN').sum() == (
                all_fp_data['Bias'] == 1).sum()


def test_filter_by_factor(sample_data):
    """Test the filter_by_factor function."""
    filtered_df = DataFormatter(sample_data).filter_by(
        'Female').get_formatted_df()
    assert len(filtered_df) == 3
    assert (filtered_df['Gender'] == 'Female').all()


def test_filter_by_factor_no_matching_values(sample_data):
    """Edge case: Test filter_by_factor with no matching values."""
    filtered_df = DataFormatter(sample_data).filter_by(
        'Nonexistent_gender',
        'Nonexistent_race',
        'Nonexistent_state'
    ).get_formatted_df()
    assert filtered_df.equals(sample_data)  # Should return the original dataset


def test_filter_by_factor_all_rows_match(sample_data):
    """Edge case: Test filter_by_factor where all rows match the value."""
    all_female_data = sample_data[sample_data['Gender'] == 'Female']
    filtered_df = DataFormatter(sample_data).filter_by(
        'Female').get_formatted_df()
    pd.testing.assert_frame_equal(filtered_df, all_female_data)


def test_unbias_does_not_mutate_original(sample_data):
    """Test to ensure the original df is not mutated by the unbias function."""
    # Create a copy of the original DataFrame for comparison
    original_data_copy = sample_data.copy()

    # Call the unbias function
    unbiased_df = DataFormatter(sample_data).unbias().get_formatted_df()

    # Mutate created df
    unbiased_df['Transaction_Amount_USD'] = 0

    # Assert that the original DataFrame is unchanged
    pd.testing.assert_frame_equal(sample_data, original_data_copy,
                                  check_dtype=True)


def test_get_for_display(real_data):
    frequency_data = [{'date': '2024-05-01', 'frequency': 52},
                      {'date': '2024-05-02', 'frequency': 48}]
    revenue_data = [{'date': '2024-05-01', 'revenue': 1306375.68},
                    {'date': '2024-05-02', 'revenue': 1361639.44}]

    display_data = DataFormatter(real_data).get_for_display()

    assert display_data[0] == frequency_data
    assert display_data[1] == revenue_data


def test_get_for_predicting(real_data):
    frequency_df = (pd.DataFrame({
        'date': [pd.to_datetime('2024-05-01').date(),
                 pd.to_datetime('2024-05-02').date()],
        'frequency': [52, 48]
    }))
    frequency_df.set_index('date', inplace=True)
    revenue_df = pd.DataFrame({
        'date': [pd.to_datetime('2024-05-01').date(),
                 pd.to_datetime('2024-05-02').date()],
        'revenue': [1306375.68, 1361639.44]
    })
    revenue_df.set_index('date', inplace=True)

    prediction_data = DataFormatter(real_data).get_for_predicting()
    pd.testing.assert_frame_equal(prediction_data[0], frequency_df)
    pd.testing.assert_frame_equal(prediction_data[1], revenue_df)


def test_helper_df_to_dict(sample_data):
    sample_data = sample_data.iloc[:2, :2]
    expected_result = [{'Customer_ID': 'C001', 'confusion_value': 'FP'},
                       {'Customer_ID': 'C002', 'confusion_value': 'TN'}]

    calculated_result = DataFormatter.helper_df_to_dict(sample_data)
    assert calculated_result == expected_result
