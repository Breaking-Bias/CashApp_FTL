import pandas as pd

class DifferenceCalculator:
    # df_unbiased: pd.DataFrame
    # df_biased: pd.DataFrame
    #
    # def __init__(self, file_name: str):
    #     self.file_name = file_name
    @staticmethod
    def _valid_input(df_unbiased: pd.DataFrame, df_biased: pd.DataFrame) -> bool:
        unbiased_col_name = df_unbiased.columns[1]
        biased_col_name = df_biased.columns[1]
        return unbiased_col_name == biased_col_name


    @staticmethod
    def volume(df_unbiased: pd.DataFrame, df_biased: pd.DataFrame) -> int:
        # Expect second (index 1) column to always be the column of interest
        if not DifferenceCalculator._valid_input(df_unbiased, df_biased):
            raise ValueError("The columns of interest do not match between the"
                             " unbiased and biased dataframes.")

        difference = df_unbiased.iloc[:, 1] - df_biased.iloc[:, 1]
        difference = round(difference.sum())

        return difference