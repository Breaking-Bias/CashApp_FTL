from abc import ABC, abstractmethod
import pandas as pd


class Filter(ABC):
    data: pd.DataFrame
    filter_factor: str | int

    def __init__(self, data: pd.DataFrame, filter_factor: str | int):
        self.data = data.copy()
        self.filter_factor = filter_factor


    @abstractmethod
    def valid_filter(self) -> bool:
        """Abstract method to check if the filtering factor is valid."""
        raise NotImplemented


    @abstractmethod
    def apply_filter(self) -> pd.DataFrame:
        """Abstract method to filter the data based on a filtering factor."""
        raise NotImplementedError


# class AgeFilter(Filter):
#     raise NotImplemented


class GenderFilter(Filter):
    def valid_filter(self) -> bool:
        """Check if the filtering factor is valid."""
        valid_genders = ['Male', 'Female', 'Non-Binary', 'Other']
        result = self.filter_factor in valid_genders
        return result


    def apply_filter(self) -> pd.DataFrame:
        """Filter data based on gender."""
        return self.data[self.data['Gender'] == self.filter_factor]


class RaceFilter(Filter):
    def valid_filter(self) -> bool:
        """Check if the filtering factor is valid."""
        valid_races = ['Black', 'White', 'Asian', 'Hispanic', 'Mixed', 'Other']
        result = self.filter_factor in valid_races
        return result


    def apply_filter(self) -> pd.DataFrame:
        """Filter data based on race."""
        return self.data[self.data['Race'] == self.filter_factor]


# class StateFilter(Filter):
#     def valid_filter(self) -> bool:
#         raise NotImplemented
#
#     def apply_filter(self) -> pd.DataFrame:
#         """Filter data based on state."""
#         return self.data[self.data['State'] == self.filter_factor]

class FilterManager:
    _df: pd.DataFrame

    def __init__(self, df_to_filter: pd.DataFrame):
        self._df = df_to_filter.copy()

    def apply_filters(self, filter_gender: str = None, filter_race: str = None, filter_state: str = None) -> pd.DataFrame:
        """
        Determines the appropriate filter(s) to use based on the filter_factors
        passed through and applies it to the data.
        """
        gender_filter = GenderFilter(self._df, filter_gender)
        if gender_filter.valid_filter():
            self._df = gender_filter.apply_filter()

        race_filter = RaceFilter(self._df, filter_race)
        if race_filter.valid_filter():
            self._df = race_filter.apply_filter()

        return self._df
