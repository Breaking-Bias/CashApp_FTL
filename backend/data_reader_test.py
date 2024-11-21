from data_reader import DataReader
import pandas as pd

def test_read_dataset():
    # Mock the path in `read_dataset` to use the temporary `transaction_data.csv`
    df = DataReader("women_bias_data.csv").read_dataset()

    # Check that the output is a DataFrame
    assert isinstance(df, pd.DataFrame), "Expected output to be a DataFrame"