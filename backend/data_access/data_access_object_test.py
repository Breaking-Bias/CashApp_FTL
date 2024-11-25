from data_access.data_access_object import DataAccessObject
import pandas as pd
import pytest
import os


# @pytest.fixture
# def test_read_dataset():
#     # Mock the path in `read_dataset` to use the temporary `transaction_data.csv`
#     df = DataAccessObject("women_bias_data.csv").read_dataset()

#     # Check that the output is a DataFrame
#     assert isinstance(df, pd.DataFrame), "Expected output to be a DataFrame"
    
@pytest.fixture
def data_access_object():
    # Define the file name
    file_name = "women_bias_data.csv"
    # Initialize DataAccessObject with the test file
    return DataAccessObject(file_name)

def test_read_dataset(data_access_object):
    dataset = data_access_object.dataset

    # Check if the dataset is read correctly
    assert dataset is not None, "Dataset should not be None"
    assert isinstance(dataset, pd.DataFrame), "Dataset should be a DataFrame"
    assert not dataset.empty, "Dataset should not be empty"

if __name__ == "__main__":
    pytest.main()