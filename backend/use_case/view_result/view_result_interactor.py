import pandas as pd

from data_access.data_access_object import DataAccessObject
from use_case.interactor_helpers.graph_adapter import GraphAdapter
from use_case.interactor_helpers.data_factory import DataFactory

TEST_FILE_NAME = 'women_bias_data.csv'


class ViewResultInteractor:
    """Interactor for the view result use case."""
    dataset: pd.DataFrame
    data_factory: DataFactory

    def __init__(self, file_name=TEST_FILE_NAME):
        self.dataset = DataAccessObject(file_name).read_dataset()
        self.data_factory = DataFactory(self.dataset,
                                        "NoFilter",
                                        "NoFilter",
                                        0)

    def make_graph_only_past(self):
        """Collect data for the past graph only."""
        revenue_graph = GraphAdapter(
            self.data_factory.revenue_past_data_biased
            )
        frequency_graph = GraphAdapter(
            self.data_factory.frequency_past_data_biased
            )
        revenue_graph = {
            "past_biased_line": revenue_graph.getPastBiasedLine()
        }
        frequency_graph = {
            "past_biased_line": frequency_graph.getPastBiasedLine()
        }

        result = {
            "revenue_graph": revenue_graph,
            "frequency_graph": frequency_graph
        }

        return result
