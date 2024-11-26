from backend.use_case.prediction.old_prediction_interactor import PredictionInteractor
from use_case.interactor_helpers.filter_interactor import FilterInteractor
import pandas as pd

class PredictionController:
    original_dataset: pd.DataFrame
    filter_gender: str
    filter_race: str
    filtered_dataset: pd.DataFrame
    forecast_steps: int
    prediction_interactor: PredictionInteractor

    def __init__(self, original_dataset: pd.DataFrame, filter_gender: str, filter_race: str, forecast_steps: int):
        self.original_dataset = original_dataset
        self.filter_gender = filter_gender
        self.filter_race = filter_race
        self.forecast_steps = forecast_steps
        self.filtered_biased_dataset = self.original_dataset.copy().filter_biased()
        self.filtered_unbiased_dataset = self.original_dataset.copy().filter_unbiased()
        self.prediction_interactor = PredictionInteractor(self.filtered_dataset, self.forecast_steps)

    def filter_biased(self) -> pd.DataFrame:
        filtered_biased_dataset = (FilterInteractor(self.original_dataset)
                                .filter_by(self.filter_gender, self.filter_race)
                                .filter_invalid_transactions())
        return filtered_biased_dataset

    def filter_unbiased(self) -> pd.DataFrame:
        filtered_unbiased_dataset = (FilterInteractor(self.original_dataset)
                                .filter_by(self.filter_gender, self.filter_race)
                                .unbias()
                                .filter_invalid_transactions())
        return filtered_unbiased_dataset

    def execute(self) -> dict[str, dict[str, list[dict]]]:
        """Returns a dictionary containing:
        {"revenue_graph": revenue_graph, "frequency_graph": frequency_graph}

        Note that revenue_graph and frequency_graph are the formatted
        """
        return self.prediction_interactor.make_prediction()
    