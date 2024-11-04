import pytest
import pandas as pd
import os
from .. read_data import read_dataset, create_formatted_data

# Note: This is specifc to the transaction_data.csv. Change it if we use a different csv later on.
@pytest.fixture
def mock_data_file(tmp_path):
    # Create a temporary CSV file in the `tmp_path` with sample data
    data_path = tmp_path / "transaction_data.csv"
    data_path.write_text("id,amount,date\n1,100.5,2023-01-01\n2,200.75,2023-01-02")
    return data_path

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

# def test_create_formatted_data():
#     assert
    
# def create_prediction_data():
#     assert 