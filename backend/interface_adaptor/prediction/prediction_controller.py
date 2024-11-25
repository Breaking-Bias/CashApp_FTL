from use_case.prediction.prediction_interactor import PredictionInteractor
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
        self.filtered_dataset = self.original_dataset.filter()
        self.forecast_steps = forecast_steps
        self.prediction_interactor = PredictionInteractor(self.filtered_dataset, self.forecast_steps)

    def filter(self):
        filtered_dataset = FilterInteractor(self.original_dataset).filter_by(self.filter_gender, self.filter_race)
        return filtered_dataset

    def execute(self):
        return self.prediction_interactor.make_prediction()
    