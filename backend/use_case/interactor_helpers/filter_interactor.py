import pandas as pd

from entity.filters import FilterManager, GenderFilter, RaceFilter


class FilterInteractor:
    df: pd.DataFrame

    def __init__(self, df_to_format: pd.DataFrame):
        self.df = df_to_format.copy()

    def get_df(self) -> pd.DataFrame:
        return self.df

    def unbias(self) -> 'FilterInteractor':
        """Removes bias by flipping FP to TN, only for 'Bias' rows"""
        self.df = self.df.apply(FilterInteractor._unbias_row, axis=1)
        return self

    @staticmethod
    def _unbias_row(row):
        if row['confusion_value'] == 'FP' and row['Bias'] == 1:
            row['confusion_value'] = 'TN'
            row['Bias'] = 0
        return row

    def filter_by(self, filter_gender: str = None, filter_race:
                  str = None, filter_state: str = None) -> 'FilterInteractor':
        """Filters the DataFrame based on gender, race, or state."""
        filters = [GenderFilter(filter_gender),
                   RaceFilter(filter_race)]

        filter_manager = FilterManager(self.df, filters)
        self.df = filter_manager.apply_filters()

        return self

    def filter_invalid_transactions(self) -> 'FilterInteractor':
        """Creates a new dataset without any rows marked as blocked
         (i.e. False Positive (incorrectly blocked),
          True Positive (correctly blocked))
        """
        self.df = self.df[(self.df['confusion_value'] != 'FP')
                          & (self.df['confusion_value'] != 'TP')]
        return self
