import pandas as pd
import pytest

from read_data import filter_by_factor, unbias, filter_for_valid_transactions

test_data = pd.DataFrame({
    'Customer_ID': ['C001', 'C002', 'C003', 'C004'],
    'confusion_value': ['FP', 'TN', 'TP', 'TN'],
    'Transaction_Amount_USD': [100.00, 150.00, 200.00, 250.00],
    'Gender': ['Female', 'Female', 'Male', 'Female']
})

def test_filter_for_valid_transactions():
    """Test the filter_for_valid_transactions function."""
    filtered_df = filter_for_valid_transactions(test_data)

    assert len(filtered_df) == 2  
    assert (filtered_df['confusion_value'] != 'FP').all()
    assert (filtered_df['confusion_value'] != 'TP').all()

def test_filter_for_valid_transactions_no_valid_rows():
    """Edge case: Test filter_for_valid_transactions with no valid rows."""
    all_invalid_data = test_data[test_data['confusion_value'].isin(['FP', 'TP'])]
    filtered_df = filter_for_valid_transactions(all_invalid_data)
    assert filtered_df.empty  

def test_filter_for_valid_transactions_all_valid_rows():
    """Edge case: Test filter_for_valid_transactions with all valid rows."""
    all_valid_data = test_data[test_data['confusion_value'] == 'TN']
    filtered_df = filter_for_valid_transactions(all_valid_data)
    assert len(filtered_df) == len(all_valid_data)

def test_unbias():
    """Test the unbias function."""
    test_data_with_bias = pd.DataFrame({
        'Customer_ID': ['C001', 'C002', 'C003', 'C004'],
        'confusion_value': ['FP', 'TN', 'FP', 'TN'],
        'Transaction_Amount_USD': [100.00, 150.00, 200.00, 250.00]
    })

    unbiased_df = unbias(test_data_with_bias)

    assert (unbiased_df['confusion_value'] == 'TN').all() 

def test_unbias_no_fp_values():
    """Edge case: Test unbias with no 'FP' values to modify."""
    no_fp_data = test_data[test_data['confusion_value'] == 'TN']
    unbiased_df = unbias(no_fp_data)
    pd.testing.assert_frame_equal(unbiased_df, no_fp_data)  

def test_unbias_all_fp_values():
    """Edge case: Test unbias with all 'FP' values."""
    all_fp_data = test_data.copy()
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

def test_unbias_does_not_mutate_original():
    """Test to ensure the original DataFrame is not mutated by the unbias function."""
    original_data = pd.DataFrame({
        'Customer_ID': ['C001', 'C002', 'C003', 'C004'],
        'confusion_value': ['FP', 'TN', 'FP', 'TN'],
        'Transaction_Amount_USD': [100.00, 150.00, 200.00, 250.00],
        'was_biased': [1, 0, 1, 0]
    })

    # Create a copy of the original DataFrame for comparison
    original_data_copy = original_data.copy()

    # Call the unbias function
    unbiased_df = unbias(original_data)

    # Mutate created df
    unbiased_df['Transaction_Amount_USD'] = 0

    # Assert that the original DataFrame is unchanged
    pd.testing.assert_frame_equal(original_data, original_data_copy, check_dtype=True)

def test_filter_for_valid_data_does_not_mutate_original():
    """Test to ensure the original DataFrame is not mutated by the unbias function."""
    original_data = pd.DataFrame({
        'Customer_ID': ['C001', 'C002', 'C003', 'C004'],
        'confusion_value': ['FP', 'TN', 'FP', 'TN'],
        'Transaction_Amount_USD': [100.00, 150.00, 200.00, 250.00],
        'was_biased': [1, 0, 1, 0]
    })

    # Create a copy of the original DataFrame for comparison
    original_data_copy = original_data.copy()

    # Call the unbias function
    filtered_df = filter_for_valid_transactions(original_data)

    # Mutate created df
    filtered_df['Transaction_Amount_USD'] = 0

    # Assert that the original DataFrame is unchanged
    pd.testing.assert_frame_equal(original_data, original_data_copy, check_dtype=True)
    