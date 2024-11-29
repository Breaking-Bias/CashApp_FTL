# import pytest
# import pandas as pd
#
# from use_case.interactor_helpers.data_factory import DataFactory
# from use_case.interactor_helpers.filter_interactor import FilterInteractor
#
#
# @pytest.fixture
# def sample_df():
#     sample_df = pd.DataFrame({
#         'date': []
#         'Customer_ID': ['C001', 'C002', 'C003', 'C004', 'C005'],
#         'confusion_value': ['FP', 'TN', 'TP', 'FN', 'FP'],
#         'Transaction_Amount_USD': [100.00, 150.00, 200.00, 250.00, 300.00],
#         'Gender': ['Female', 'Other', 'Male', 'Female', 'Female'],
#         'Bias': [1, 0, 1, 0, 0]
#     })
#     return sample_df
#
# @pytest.fixture
# def sample_formatted_past_data(sample_df):
#     sample_formatted_past_data = (FilterInteractor(sample_df).filter_by("Female", "NoFilter")
#                                   .filter_invalid_transactions())
#     return sample_formatted_past_data
#
# def test_make_data_positive_step(sample_df):
#     result = DataFactory._make_data(sample_df, 5)
