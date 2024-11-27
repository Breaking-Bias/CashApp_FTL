import pandas as pd

from use_case.interactor_helpers.filter_interactor import FilterInteractor
from use_case.interactor_helpers.data_formatter import DataFormatter
from use_case.interactor_helpers.model_interactor import ModelInteractor
from entity.graphing_data import GraphingData
# This import is only for type annotation purpose.


class DataFactory:
    """
    Responsible for creating the data for the prediction use case.
    Manages the filtering workflows and creating unbiased/biased data.
    """
    dataset: pd.DataFrame
    filter_gender: str
    filter_race: str
    forecast_steps: int

    def __init__(self,
                 dataset: pd.DataFrame,
                 filter_gender: str,
                 filter_race: str,
                 forecast_steps: int):
        self.dataset = dataset
        self.filter_gender = filter_gender
        self.filter_race = filter_race
        self.forecast_steps = forecast_steps
        biased_dataset = self.filter_biased()
        unbiased_dataset = self.filter_unbiased()
        self.frequency_past_data_biased = (
            DataFormatter(biased_dataset.copy()).get_frequency_data()
            )
        self.revenue_past_data_biased = (
            DataFormatter(biased_dataset.copy()).get_revenue_data()
            )
        self.frequency_past_data_unbiased = (
            DataFormatter(unbiased_dataset.copy()).get_frequency_data()
            )
        self.revenue_past_data_unbiased = (
            DataFormatter(unbiased_dataset.copy()).get_revenue_data()
            )

    def filter_biased(self) -> pd.DataFrame:
        """Used to create biased dataset for DataFormatter to format."""
        filtered_biased_dataset = (
            FilterInteractor(self.dataset.copy())
            .filter_by(self.filter_gender, self.filter_race)
            .filter_invalid_transactions()
            )
        result = filtered_biased_dataset.df
        return result

    def filter_unbiased(self) -> pd.DataFrame:
        """Used to create unbiased dataset for DataFormatter to format."""
        filtered_unbiased_dataset = (
            FilterInteractor(self.dataset.copy())
            .filter_by(self.filter_gender, self.filter_race)
            .unbias()
            .filter_invalid_transactions()
            )
        result = filtered_unbiased_dataset.df
        return result

    def make_biased_data(self) -> tuple[GraphingData,
                                        GraphingData,
                                        GraphingData | None,
                                        GraphingData | None]:
        """The biased data creation workflow"""

        if self.forecast_steps > 0:
            (
                frequency_predicted_data_biased,
                revenue_predicted_data_biased
            ) = (ModelInteractor(
                (
                    self.frequency_past_data_biased,
                    self.revenue_past_data_biased
                )
            ).execute(self.forecast_steps))
        else:
            frequency_predicted_data_biased = None
            revenue_predicted_data_biased = None

        return (self.frequency_past_data_biased,
                self.revenue_past_data_biased,
                frequency_predicted_data_biased,
                revenue_predicted_data_biased)

    def make_unbiased_data(self) -> tuple[GraphingData,
                                          GraphingData,
                                          GraphingData | None,
                                          GraphingData | None]:
        """The unbiased data creation workflow"""

        if self.forecast_steps > 0:
            (
                frequency_predicted_data_unbiased,
                revenue_predicted_data_unbiased
            ) = ModelInteractor(
                (
                    self.frequency_past_data_unbiased,
                    self.revenue_past_data_unbiased
                )
            ).execute(self.forecast_steps)
        else:
            frequency_predicted_data_unbiased = None
            revenue_predicted_data_unbiased = None

        return (self.frequency_past_data_unbiased,
                self.revenue_past_data_unbiased,
                frequency_predicted_data_unbiased,
                revenue_predicted_data_unbiased)
