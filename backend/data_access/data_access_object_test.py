from data_access.data_access_object import DataAccessObject
import pandas as pd

def test_read_dataset():
    # Mock the path in `read_dataset` to use the temporary `transaction_data.csv`
    df = DataAccessObject("women_bias_data.csv").read_dataset()

    # Check that the output is a DataFrame
    assert isinstance(df, pd.DataFrame), "Expected output to be a DataFrame"