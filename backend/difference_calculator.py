import pandas as pd

class DifferenceCalculator:
    # df_unbiased: pd.DataFrame
    # df_biased: pd.DataFrame
    #
    # def __init__(self, file_name: str):
    #     self.file_name = file_name
    @staticmethod
    def volume(df_unbiased: pd.DataFrame, df_biased: pd.DataFrame) -> int:
        # Expect second (index 1) column to always be the column of interest
        difference = df_unbiased.iloc[:, 1] - df_biased.iloc[:, 1]
        difference = round(difference.sum())

        return difference