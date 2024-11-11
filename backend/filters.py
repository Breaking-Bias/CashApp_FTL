from abc import ABC, abstractmethod
import pandas as pd

class Filter(ABC):
    def __init__(self, data: pd.DataFrame):
        self.data = data.copy()

    @abstractmethod
    def apply_filter(self, filtering_factor: str) -> pd.DataFrame:
        """Abstract method to filter the data based on a filtering factor."""
        pass


# class AgeFilter(Filter):
#     raise NotImplemented


class GenderFilter(Filter):
    def apply_filter(self, filtering_factor: str) -> pd.DataFrame:
        """Filter data based on gender."""
        return self.data[self.data['Gender'] == filtering_factor]

class RaceFilter(Filter):
    def apply_filter(self, filtering_factor: str) -> pd.DataFrame:
        """Filter data based on race."""
        return self.data[self.data['Race'] == filtering_factor]


# class StateFilter(Filter):
#     def apply_filter(self, filtering_factor: str) -> pd.DataFrame:
#         """Filter data based on state."""
#         return self.data[self.data['State'] == filtering_factor]
        
class FilterManager:
    def __init__(self, df_to_filter: pd.DataFrame):
        self._df = df_to_filter.copy()
    
    def apply_filters(self, filter_gender: str = None, filter_race: str = None, filter_state: str = None) -> pd.DataFrame:
        """
        Determines the appropriate filter to use based on the filtering_factor
        and applies it to the data.
        """      
        if filter_gender in ['Male', 'Female', 'Non-Binary', 'Other']:
            self._df = GenderFilter(self._df).apply_filter(filter_gender)
        if filter_race in ['Black', 'White', 'Asian', 'Hispanic', 'Mixed', 'Other']:
            self._df = RaceFilter(self._df).apply_filter(filter_race)
            
        return self._df