import pandas as pd
from entity.graphing_data import GraphingData  # This import is only for type annotation purpose.


class DifferenceCalculator:
    df_unbiased: pd.DataFrame
    df_biased: pd.DataFrame
    
    def __init__(self, df_unbiased: GraphingData, df_biased: GraphingData):
        self.df_unbiased = df_unbiased.get_data()
        self.df_biased = df_biased.get_data()

        
    def _valid_input(self) -> bool:
        unbiased_col_name = self.df_unbiased.columns[1]
        biased_col_name = self.df_biased.columns[1]
        return unbiased_col_name == biased_col_name


    def volume_difference(self) -> int:
        # Expect second (index 1) column to always be the column of interest
        if not self._valid_input():
            raise ValueError("The columns of interest do not match between the"
                             " unbiased and biased dataframes.")

        difference = self.df_unbiased.iloc[:, 1] - self.df_biased.iloc[:, 1]
        difference = round(difference.sum())

        return difference
    

    def average_difference(self) -> int:
        difference = self.df_unbiased.iloc[:, 1] - self.df_biased.iloc[:, 1]

        average_diff = difference.mean()

        return int(average_diff)