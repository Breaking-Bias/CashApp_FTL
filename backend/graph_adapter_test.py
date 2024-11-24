import pytest
import pandas as pd
import datetime
from entity.graphing_data import GraphingData
from graph_adapter import GraphAdapter

# Sample data for testing
def create_sample_data():
    data = {
        "date": [datetime.date(2023, 1, 1), datetime.date(2023, 1, 2)],
        "revenue": [100, 200]
    }
    return pd.DataFrame(data)

@pytest.fixture
def sample_data():
    # Sample data to test
    return create_sample_data()

@pytest.fixture
def graphing_data(sample_data):
    # Wrap the sample data in GraphingData objects
    return GraphingData(sample_data)

@pytest.fixture
def graph_adapter(graphing_data):
    # Create GraphAdapter with the same data for all fields
    return GraphAdapter(
        revenue_past_biased_data=graphing_data,
        revenue_predicted_biased_data=graphing_data,
        revenue_past_unbiased_data=graphing_data,
        revenue_predicted_unbiased_data=graphing_data
    )

# Test for GraphingData class initialization and validation
def test_graphing_data_initialization(graphing_data):
    # Ensure that data is initialized properly
    assert isinstance(graphing_data, GraphingData)
    assert graphing_data.get_data().shape == (2, 2)  # Check if DataFrame has 2 rows and 2 columns
    assert graphing_data.get_data().columns.tolist() == ["date", "revenue"]  # Ensure column names are correct

def test_invalid_data_initialization():
    # Test invalid data: data with more than 2 columns
    data = pd.DataFrame({
        "date": [datetime.date(2023, 1, 1), datetime.date(2023, 1, 2)],
        "revenue": [100, 200],
        "extra_column": [1, 2]
    })
    with pytest.raises(AssertionError):
        GraphingData(data)

    # Test invalid data: column 1 not labeled "date"
    data = pd.DataFrame({
        "not_date": [datetime.date(2023, 1, 1), datetime.date(2023, 1, 2)],
        "revenue": [100, 200]
    })
    with pytest.raises(AssertionError):
        GraphingData(data)

    # Test invalid data: second column not labeled "revenue" or "frequency"
    data = pd.DataFrame({
        "date": [datetime.date(2023, 1, 1), datetime.date(2023, 1, 2)],
        "invalid_column": [100, 200]
    })
    with pytest.raises(AssertionError):
        GraphingData(data)

# # Test for GraphAdapter methods
# def test_graph_adapter_methods(graph_adapter):
#     # Test helper_df_to_dict conversion
#     dict_data = graph_adapter.helper_df_to_dict(graph_adapter.revenue_past_biased_data.get_data())
#     assert isinstance(dict_data, list)
#     assert len(dict_data) == 2  # 2 rows in the sample data
#     assert "date" in dict_data[0]
#     assert "revenue" in dict_data[0]
#
#     # Test the specific methods for fetching data
#     past_unbiased = graph_adapter.getPastUnbiasedLine()
#     assert past_unbiased == dict_data  # It should return the same as helper_df_to_dict for the given data
#
#     predicted_unbiased = graph_adapter.getPredictedUnbiasedLine()
#     assert predicted_unbiased == dict_data  # Same data for now
#
#     past_biased = graph_adapter.getPastBiasedLine()
#     assert past_biased == dict_data  # Same data for now
#
#     predicted_biased = graph_adapter.getPredictedBiasedLine()
#     assert predicted_biased == dict_data  # Same data for now

# Test for GraphAdapter and GraphingData with edge cases
def test_graph_adapter_edge_cases():
    empty_data = pd.DataFrame({
        "date": [],
        "revenue": []
    })

    empty_graphing_data = GraphingData(empty_data)
    empty_graph_adapter = GraphAdapter(
        revenue_past_biased_data=empty_graphing_data,
        revenue_predicted_biased_data=empty_graphing_data,
        revenue_past_unbiased_data=empty_graphing_data,
        revenue_predicted_unbiased_data=empty_graphing_data
    )

    # Test empty data handling
    assert empty_graph_adapter.getPastUnbiasedLine() == []
    assert empty_graph_adapter.getPredictedUnbiasedLine() == []
    assert empty_graph_adapter.getPastBiasedLine() == []
    assert empty_graph_adapter.getPredictedBiasedLine() == []

