import pandas as pd

from use_case.interactor_helpers.data_formatter import DataFormatter
from use_case.interactor_helpers.model_interactor import ModelInteractor
from entity.graphing_data import GraphingData  # This import is only for type annotation purpose.


class DataFactory:
    dataset: pd.DataFrame
    forecast_steps: int

    def __init__(self, dataset: pd.DataFrame, forecast_steps: int):
        self.dataset = dataset
        self.forecast_steps = forecast_steps
        self.frequency_past_data_biased = DataFormatter(self.dataset.copy()).get_frequency_data()
        self.revenue_past_data_biased = DataFormatter(self.dataset.copy()).get_revenue_data()
        self.frequency_past_data_unbiased = DataFormatter(self.dataset.copy()).get_frequency_data()
        self.revenue_past_data_unbiased = DataFormatter(self.dataset.copy()).get_revenue_data()

    def make_biased_data(self) -> tuple[GraphingData, 
                                        GraphingData,
                                        GraphingData | None, 
                                        GraphingData | None]:

        # TODO: figure out what get_df() does?
        # frequency_past_data_biased = DataFormatter(self.dataset.copy()).get_frequency_data()
        # revenue_past_data_biased = DataFormatter(self.dataset.copy()).get_revenue_data()

        if self.forecast_steps > 0:
            frequency_predicted_data_biased, revenue_predicted_data_biased = (
                ModelInteractor((self.frequency_past_data_biased,
                                 self.revenue_past_data_biased))
                .execute(self.forecast_steps))
        else:
            frequency_predicted_data_biased, revenue_predicted_data_biased = None, None

        return (self.frequency_past_data_biased, 
                self.revenue_past_data_biased,
                frequency_predicted_data_biased, 
                revenue_predicted_data_biased)

    def make_unbiased_data(self) -> tuple[GraphingData, 
                                          GraphingData,
                                          GraphingData | None, 
                                          GraphingData | None]:
        
        # TODO: figure out what get_df() does?
        # frequency_past_data_unbiased = DataFormatter(self.dataset.copy()).get_frequency_data()
        # revenue_past_data_unbiased = DataFormatter(self.dataset.copy()).get_revenue_data()

        if self.forecast_steps > 0:
            frequency_predicted_data_unbiased, revenue_predicted_data_unbiased = (
                ModelInteractor((self.frequency_past_data_unbiased,
                                 self.revenue_past_data_unbiased))
                .execute(self.forecast_steps))
        else:
            frequency_predicted_data_unbiased, revenue_predicted_data_unbiased = None, None

        return (self.frequency_past_data_unbiased, 
                self.revenue_past_data_unbiased,
                frequency_predicted_data_unbiased,
                revenue_predicted_data_unbiased)
