import pandas as pd
from data_access.data_access_object import DataAccessObject
from use_case.interactor_helpers.data_creator import DataCreator
from entity.difference_calculator import DifferenceCalculator
from use_case.interactor_helpers.graph_adapter import GraphAdapter
from entity.graphing_data import GraphingData


class PredictionInteractor:
    """Interactor for the prediction use case."""
    dataset: pd.DataFrame
    forecase_steps: int

    frequency_past_data_biased: GraphingData
    revenue_past_data_biased: GraphingData
    frequency_predicted_data_biased: GraphingData
    revenue_predicted_data_biased: GraphingData
    frequency_past_data_unbiased: GraphingData
    revenue_past_data_unbiased: GraphingData
    frequency_predicted_data_unbiased: GraphingData
    revenue_predicted_data_unbiased: GraphingData

    def __init__(self, file_name: str,
                 filter_gender: str,
                 filter_race: str,
                 forecast_steps: int):
        self.dataset = DataAccessObject(file_name).read_dataset()
        data_creator = DataCreator(self.dataset,
                                   filter_gender,
                                   filter_race,
                                   forecast_steps)

        (self.frequency_past_data_biased,
         self.revenue_past_data_biased,
         self.frequency_predicted_data_biased,
         self.revenue_predicted_data_biased) \
            = data_creator.make_biased_data()

        (self.frequency_past_data_unbiased,
         self.revenue_past_data_unbiased,
         self.frequency_predicted_data_unbiased,
         self.revenue_predicted_data_unbiased) \
            = data_creator.make_unbiased_data()

    def _calculate_difference(self) -> dict[str, int]:
        """Calculate difference between biased and unbiased data"""

        revenue_difference_calculator_past = DifferenceCalculator(
            self.revenue_past_data_unbiased,
            self.revenue_past_data_biased
        )
        revenue_difference_calculator_predicted = DifferenceCalculator(
            self.revenue_predicted_data_unbiased,
            self.revenue_predicted_data_biased
        )
        frequency_difference_calculator_past = DifferenceCalculator(
            self.frequency_past_data_unbiased,
            self.frequency_past_data_biased
        )
        frequency_difference_calculator_predicted = DifferenceCalculator(
            self.frequency_predicted_data_unbiased,
            self.frequency_predicted_data_biased
        )

        result = {
            "revenue_total_difference":
                revenue_difference_calculator_past.volume_difference() +
                revenue_difference_calculator_predicted.volume_difference(),
            "revenue_average_difference":
                revenue_difference_calculator_past.average_difference() +
                revenue_difference_calculator_predicted.average_difference(),
            "frequency_total_difference":
                frequency_difference_calculator_past.volume_difference() +
                frequency_difference_calculator_predicted.volume_difference(),
            "frequency_average_difference":
                frequency_difference_calculator_past.average_difference() +
                frequency_difference_calculator_predicted.average_difference(),
        }
        return result

    def make_prediction(self) -> dict[str, dict[str, list[dict]]]:
        """Creates complete data for the prediction use case."""

        difference_dict = self._calculate_difference()
        revenue_total_difference = (
            difference_dict["revenue_total_difference"]
            )
        revenue_average_difference = (
            difference_dict["revenue_average_difference"]
            )
        frequency_total_difference = (
            difference_dict["frequency_total_difference"]
            )
        frequency_average_difference = (
            difference_dict["frequency_average_difference"]
            )

        # Collect all the data
        revenue_graph = GraphAdapter(self.revenue_past_data_biased,
                                     self.revenue_predicted_data_biased,
                                     self.revenue_past_data_unbiased,
                                     self.revenue_predicted_data_unbiased)

        frequency_graph = GraphAdapter(self.frequency_past_data_biased,
                                       self.frequency_predicted_data_biased,
                                       self.frequency_past_data_unbiased,
                                       self.frequency_predicted_data_unbiased)

        revenue_graph = {
            "past_biased_line": revenue_graph.getPastBiasedLine(),
            "predicted_biased_line": revenue_graph.getPredictedBiasedLine(),
            "past_unbiased_line": revenue_graph.getPastUnbiasedLine(),
            "predicted_unbiased_line": (
                revenue_graph.getPredictedUnbiasedLine()),

            "total_difference": revenue_total_difference,
            "average_difference": revenue_average_difference,
        }

        frequency_graph = {
            "past_biased_line": frequency_graph.getPastBiasedLine(),
            "predicted_biased_line": frequency_graph.getPredictedBiasedLine(),
            "past_unbiased_line": frequency_graph.getPastUnbiasedLine(),
            "predicted_unbiased_line": (
                frequency_graph.getPredictedUnbiasedLine()),

            "total_difference": frequency_total_difference,
            "average_difference": frequency_average_difference,
        }

        result = {
            "revenue_graph": revenue_graph,
            "frequency_graph": frequency_graph
        }
        return result
