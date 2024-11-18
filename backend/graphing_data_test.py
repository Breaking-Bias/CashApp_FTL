import pytest
import pandas as pd
from graphing_data import GraphingData

def test_valid_data_frequency():
    data = pd.DataFrame({
        "date": [pd.Timestamp("2023-01-01").date(),
                 pd.Timestamp("2023-01-02").date()],
        "frequency": [10, 20]
    })
    graphing_data = GraphingData(data)
    assert graphing_data.get_data().equals(data)

def test_valid_data_revenue():
    data = pd.DataFrame({
        "date": [pd.Timestamp("2023-01-01").date(),
                 pd.Timestamp("2023-01-02").date()],
        "revenue": [1000, 2000]
    })
    graphing_data = GraphingData(data)
    assert graphing_data.get_data().equals(data)

def test_invalid_column_count():
    data = pd.DataFrame({
        "date": [pd.Timestamp("2023-01-01").date(),
                 pd.Timestamp("2023-01-02").date()],
        "frequency": [10, 20],
        "extra": [1, 2]
    })
    with pytest.raises(AssertionError,
                       match="Data must have exactly 2 columns."):
        GraphingData(data)

def test_invalid_first_column_name():
    data = pd.DataFrame({
        "wrong": [pd.Timestamp("2023-01-01").date(),
                 pd.Timestamp("2023-01-02").date()],
        "frequency": [10, 20]
    })
    with pytest.raises(AssertionError,
                       match="First column header must be 'date'."):
        GraphingData(data)

def test_invalid_second_column_name():
    data = pd.DataFrame({
        "date": [pd.Timestamp("2023-01-01").date(),
                 pd.Timestamp("2023-01-02").date()],
        "wrong": [10, 20]
    })
    with pytest.raises(AssertionError,
                       match="Second column header must be 'frequency' or 'revenue'."):
        GraphingData(data)

def test_invalid_date_values():
    data = pd.DataFrame({
        "date": ["2023-01-01", "2023-01-02"],
        "frequency": [10, 20]
    })
    with pytest.raises(AssertionError,
                       match="All values in the first column must be pd.Timestamp.date objects."):
        GraphingData(data)


def test_equals():
    data = pd.DataFrame({
        "date": [pd.Timestamp("2023-01-01").date(),
                 pd.Timestamp("2023-01-02").date()],
        "frequency": [10, 20]
    })
    graphing_data1 = GraphingData(data)
    graphing_data2 = GraphingData(data)
    assert graphing_data1.equals(graphing_data2)
