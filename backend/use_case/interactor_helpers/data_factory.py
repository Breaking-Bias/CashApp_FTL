import pandas as pd

from use_case.interactor_helpers.data_formatter import DataFormatter
from use_case.interactor_helpers.filter_interactor import FilterInteractor
from use_case.interactor_helpers.model_interactor import ModelInteractor
from entity.graphing_data import GraphingData  # This import is only for type annotation purpose.


class DataFactory:
    dataset: pd.DataFrame
    filter_gender: str
    filter_race: str
    forecast_steps: int

    def __init__(self, dataset: pd.DataFrame, filter_gender: str, filter_race: str, forecast_steps: int):
        self.dataset = dataset
        self.filter_gender = filter_gender
        self.filter_race = filter_race
        self.forecast_steps = forecast_steps

    def make_biased_data(self) -> tuple[GraphingData, GraphingData,
                                        GraphingData | None, GraphingData | None]:
        formatted_past_data = (FilterInteractor(self.dataset)
                               .filter_by(self.filter_gender, self.filter_race)
                               .filter_invalid_transactions())

        frequency_past_data_biased = DataFormatter(formatted_past_data.get_df()).get_frequency_data()
        revenue_past_data_biased = DataFormatter(formatted_past_data.get_df()).get_revenue_data()
        if self.forecast_steps > 0:
            frequency_predicted_data_biased, revenue_predicted_data_biased = (
                ModelInteractor((frequency_past_data_biased,
                                 revenue_past_data_biased))
                .execute(self.forecast_steps))
        else:
            frequency_predicted_data_biased, revenue_predicted_data_biased = None, None

        return (frequency_past_data_biased, revenue_past_data_biased,
                frequency_predicted_data_biased, revenue_predicted_data_biased)

    def make_unbiased_data(self) -> tuple[GraphingData, GraphingData,
                                          GraphingData | None, GraphingData | None]:
        formatted_past_data_unbiased = (FilterInteractor(self.dataset)
                                        .filter_by(self.filter_gender,
                                                   self.filter_race)
                                        .unbias()
                                        .filter_invalid_transactions())

        frequency_past_data_unbiased = DataFormatter(formatted_past_data_unbiased.get_df()).get_frequency_data()
        revenue_past_data_unbiased = DataFormatter(formatted_past_data_unbiased.get_df()).get_revenue_data()
        if self.forecast_steps > 0:
            frequency_predicted_data_unbiased, revenue_predicted_data_unbiased = (
                ModelInteractor((frequency_past_data_unbiased,
                                 revenue_past_data_unbiased))
                .execute(self.forecast_steps))
        else:
            frequency_predicted_data_unbiased, revenue_predicted_data_unbiased = None, None

        return (frequency_past_data_unbiased, revenue_past_data_unbiased,
                frequency_predicted_data_unbiased,
                revenue_predicted_data_unbiased)
