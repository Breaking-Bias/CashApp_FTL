import pandas as pd
from use_case.interactor_helpers.model_interactor import ModelInteractor
from backend.use_case.prediction.prediction_interactor import PredictionInteractor
from use_case.interactor_helpers.data_factory import DataFactory
from entity.difference_calculator import DifferenceCalculator
from use_case.interactor_helpers.graph_adapter import GraphAdapter
from entity.graphing_data import GraphingData


class PredictionInteractor:
    original_dataset: pd.DataFrame
    forecast_steps: int
    prediction_dataset: pd.DataFrame

    frequency_past_data_biased: GraphingData
    revenue_past_data_biased: GraphingData
    frequency_predicted_data_biased: GraphingData
    revenue_predicted_data_biased: GraphingData
    frequency_past_data_unbiased: GraphingData
    revenue_past_data_unbiased: GraphingData
    frequency_predicted_data_unbiased: GraphingData
    revenue_predicted_data_unbiased: GraphingData

    def __init__(self, original_dataset: pd.DataFrame, forecast_steps: int):
        self.original_dataset = original_dataset
        self.forecast_steps = forecast_steps
        self.prediction_dataset = self.make_prediction(original_dataset)

    def make_prediction(self, original_dataset: pd.DataFrame) -> tuple[GraphingData,
                                                                        GraphingData,
                                                                        GraphingData,
                                                                        GraphingData]:
        """Makes a prediction based on the original dataset,
        and returns four datasets:

        - frequency_predicted_data_biased
        - revenue_predicted_data_biased
        - frequency_predicted_data_unbiased
        - revenue_predicted_data_unbiased
        """
        # model_interactor = ModelInteractor(original_dataset)
        # frequency_predicted_data_biased, revenue_predicted_data_biased = model_interactor.execute(self.forecast_steps)
        # frequency_predicted_data_unbiased, revenue_predicted_data_unbiased = model_interactor.execute(self.forecast_steps)
        # return (frequency_predicted_data_biased,
        #         revenue_predicted_data_biased,
        #         frequency_predicted_data_unbiased,
        #         revenue_predicted_data_unbiased)

        get_graph_interactor = PredictionInteractor(self.dataset, self.forecast_steps)
        result = get_graph_interactor.make_prediction()
        return result
