import pandas as pd
import os
import pytest
from read_data import read_dataset, filter_by_factor, unbias, filter_for_valid_transactions


# Note: This is specifc to the transaction_data.csv. Change it if we use a different csv later on.
@pytest.fixture
def mock_data_file(tmp_path):
    # Create a temporary CSV file in the `tmp_path` with sample data
    data_path = tmp_path / "transaction_data.csv"
    data_path.write_text("id,amount,date\n1,100.5,2023-01-01\n2,200.75,2023-01-02")
    return data_path


@pytest.fixture
def sample_data():
    sample_data = pd.DataFrame({
        'Customer_ID': ['C001', 'C002', 'C003', 'C004', 'C005'],
        'confusion_value': ['FP', 'TN', 'TP', 'FN', 'FP'],
        'Transaction_Amount_USD': [100.00, 150.00, 200.00, 250.00, 300.00],
        'Gender': ['Female', 'Female', 'Male', 'Female', 'Female'],
        'was_biased': [1, 0, 1, 0, 0]
    })
    return sample_data

def test_read_dataset(monkeypatch, mock_data_file):
    # Mock the path in `read_dataset` to use the temporary `transaction_data.csv`
    monkeypatch.setattr(
        os.path, "join", lambda *args: str(mock_data_file)
    )

    # Call `read_dataset` and store the result
    df = read_dataset()

    # Check that the output is a DataFrame
    assert isinstance(df, pd.DataFrame), "Expected output to be a DataFrame"

    # Verify the contents of the DataFrame.
    # TODO: Modify this based on the dataset
    # assert list(df.columns) == ["id", "amount", "date"], "Unexpected columns in DataFrame"
    # assert len(df) == 2, "Unexpected number of rows in DataFrame"
    # assert df.iloc[0].to_dict() == {"id": 1, "amount": 100.5, "date": "2023-01-01"}
    # assert df.iloc[1].to_dict() == {"id": 2, "amount": 200.75, "date": "2023-01-02"}

def test_filter_for_valid_transactions(sample_data):
    """Test the filter_for_valid_transactions function."""
    filtered_df = filter_for_valid_transactions(sample_data)

    assert len(filtered_df) == 2  
    assert (filtered_df['confusion_value'] != 'FP').all()
    assert (filtered_df['confusion_value'] != 'TP').all()

def test_filter_for_valid_transactions_no_valid_rows(sample_data):
    """Edge case: Test filter_for_valid_transactions with no valid rows."""
    all_invalid_data = sample_data[sample_data['confusion_value'].isin(['FP', 'TP'])]
    filtered_df = filter_for_valid_transactions(all_invalid_data)
    assert filtered_df.empty  

def test_filter_for_valid_transactions_all_valid_rows(sample_data):
    """Edge case: Test filter_for_valid_transactions with all valid rows."""
    all_valid_data = sample_data[sample_data['confusion_value'] == 'TN']
    filtered_df = filter_for_valid_transactions(all_valid_data)
    assert len(filtered_df) == len(all_valid_data)

def test_unbias(sample_data):
    """Test the unbias function."""
    unbiased_df = unbias(sample_data)

    assert (unbiased_df.iloc[0, 1] == 'TN')
    assert unbiased_df.iloc[4, 1] == 'FP'

def test_unbias_no_fp_values(sample_data):
    """Edge case: Test unbias with no 'FP' values to modify."""
    no_fp_data = sample_data[sample_data['confusion_value'] == 'TN']
    unbiased_df = unbias(no_fp_data)
    pd.testing.assert_frame_equal(unbiased_df, no_fp_data)  

def test_unbias_all_fp_values(sample_data):
    """Edge case: Test unbias with all 'FP' values."""
    all_fp_data = sample_data.copy()
    all_fp_data['confusion_value'] = 'FP'
    unbiased_df = unbias(all_fp_data)
    assert (unbiased_df['confusion_value'] == 'TN').all()


#comment this in when you need to <3
# def test_filter_by_factor():
#     """Test the filter_by_factor function."""
#     filtered_df = filter_by_factor(test_data, 'Gender', 'Female')
#     assert len(filtered_df) == 3  
#     assert (filtered_df['Gender'] == 'Female').all() 
# def test_filter_by_factor_non_existent_column():
#     """Edge case: Test filter_by_factor with a non-existent column."""
#     with pytest.raises(KeyError):
#         filter_by_factor(test_data, 'NonExistentColumn', 'SomeValue')

# def test_filter_by_factor_no_matching_values():
#     """Edge case: Test filter_by_factor with no matching values."""
#     filtered_df = filter_by_factor(test_data, 'Gender', 'Nonexistent')
#     assert filtered_df.empty  # Should be empty as there are no matches

# def test_filter_by_factor_all_rows_match():
#     """Edge case: Test filter_by_factor where all rows match the value."""
#     all_female_data = test_data[test_data['Gender'] == 'Female']
#     filtered_df = filter_by_factor(test_data, 'Gender', 'Female')
#     pd.testing.assert_frame_equal(filtered_df, all_female_data) 

def test_unbias_does_not_mutate_original(sample_data):
    """Test to ensure the original DataFrame is not mutated by the unbias function."""
    # Create a copy of the original DataFrame for comparison
    original_data_copy = sample_data.copy()

    # Call the unbias function
    unbiased_df = unbias(sample_data)

    # Mutate created df
    unbiased_df['Transaction_Amount_USD'] = 0

    # Assert that the original DataFrame is unchanged
    pd.testing.assert_frame_equal(sample_data, original_data_copy, check_dtype=True)

def test_filter_for_valid_data_does_not_mutate_original(sample_data):
    """Test to ensure the original DataFrame is not mutated by the unbias function."""
    # Create a copy of the original DataFrame for comparison
    original_data_copy = sample_data.copy()

    # Call the unbias function
    filtered_df = filter_for_valid_transactions(sample_data)

    # Mutate created df
    filtered_df['Transaction_Amount_USD'] = 0

    # Assert that the original DataFrame is unchanged
    pd.testing.assert_frame_equal(sample_data, original_data_copy, check_dtype=True)
    