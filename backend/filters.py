from abc import ABC, abstractmethod
import pandas as pd

class Filter(ABC):
    def __init__(self, data: pd.DataFrame):
        self.data = data.copy()

    @abstractmethod
    def filter(self, filtering_factor: str) -> pd.DataFrame:
        """Abstract method to filter the data based on a filtering factor."""
        pass


class AgeFilter(Filter):
    # Age ranges can be modified if needed, or even passed in dynamically
    AGE_RANGES = [
        (0, 18),    # Age group: 0-18
        (18, 35),   # Age group: 18-35
        (35, 65),   # Age group: 35-65
        (65, float('inf'))  # Age group: 65+
    ]

    def filter(self, filtering_factor: str) -> pd.DataFrame:
        """Filter data based on age."""
        try:
            age = int(filtering_factor)
        except ValueError:
            raise ValueError(f"Invalid age: '{filtering_factor}'. Must be an integer.")

        for min_age, max_age in self.AGE_RANGES:
            if min_age <= age < max_age:
                return self.data[(self.data['Age'] >= min_age) & (self.data['Age'] < max_age)]

        raise ValueError(f"Age {age} is out of valid ranges: {self.AGE_RANGES}.")


class GenderFilter(Filter):
    def filter(self, filtering_factor: str) -> pd.DataFrame:
        """Filter data based on gender."""
        valid_genders = ['Female', 'Male', 'Non-Binary', 'Other']
        if filtering_factor in valid_genders:
            return self.data[self.data['Gender'] == filtering_factor]
        else:
            raise ValueError(f"Invalid gender: '{filtering_factor}' is not a recognized gender.")


class RaceFilter(Filter):
    def filter(self, filtering_factor: str) -> pd.DataFrame:
        """Filter data based on race."""
        valid_races = ['Black', 'White', 'Asian', 'Hispanic', 'Mixed', 'Other']
        if filtering_factor in valid_races:
            return self.data[self.data['Race'] == filtering_factor]
        else:
            raise ValueError(f"Invalid race: '{filtering_factor}' is not a recognized race.")


class StateFilter(Filter):
    def filter(self, filtering_factor: str) -> pd.DataFrame:
        """Filter data based on state."""
        if len(filtering_factor) == 2 and filtering_factor.isupper():
            return self.data[self.data['State'] == filtering_factor]
        else:
            raise ValueError(f"Invalid state: '{filtering_factor}' is not a recognized state code.")
