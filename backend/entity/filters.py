from abc import ABC, abstractmethod
import pandas as pd


class Filter(ABC):
    """Abstract class for filtering data"""
    filter_factor: str | int

    def __init__(self, filter_factor: str | int):
        self.filter_factor = filter_factor

    @abstractmethod
    def valid_filter(self) -> bool:
        """Abstract method to check if the filtering factor is valid."""
        raise NotImplementedError

    @abstractmethod
    def apply_filter(self, data: pd.DataFrame) -> pd.DataFrame:
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

    def apply_filter(self, data: pd.DataFrame) -> pd.DataFrame:
        """Filter data based on gender."""
        return data[data['Gender'] == self.filter_factor]


class RaceFilter(Filter):
    def valid_filter(self) -> bool:
        """Check if the filtering factor is valid."""
        valid_races = ['Black', 'White', 'Asian', 'Hispanic', 'Mixed', 'Other']
        result = self.filter_factor in valid_races
        return result

    def apply_filter(self, data: pd.DataFrame) -> pd.DataFrame:
        """Filter data based on race."""
        return data[data['Race'] == self.filter_factor]


# class StateFilter(Filter):
#     def valid_filter(self) -> bool:
#         raise NotImplemented
#
#     def apply_filter(self) -> pd.DataFrame:
#         """Filter data based on state."""
#         return self.data[self.data['State'] == self.filter_factor]

class FilterManager:
    _df: pd.DataFrame
    filters: list[Filter]

    def __init__(self, df_to_filter: pd.DataFrame, filters: list[Filter]):
        self._df = df_to_filter.copy()
        self.filters = filters

    def apply_filters(self) -> pd.DataFrame:
        """
        Determines the appropriate filter(s) to use based on the filter_factors
        passed through and applies it to the data.
        """
        # Uses polymorphism to apply each filter
        for filter in self.filters:
            if filter.valid_filter():
                self._df = filter.apply_filter(self._df)

        return self._df
