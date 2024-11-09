import pandas as pd

class DataFormatter:
    def __init__(self, df_to_format: pd.DataFrame):
        self._df = df_to_format.copy()


    def get_formatted_df(self):
        return self._df


    def unbias(self):
        self._df =  self._df.apply(DataFormatter._unbias_row, axis=1)
        return self


    @staticmethod
    def _unbias_row(row):
        # TODO only flip bits that have bias == 1
        if row['confusion_value'] == 'FP' and row['Bias'] == 1:
            row['confusion_value'] = 'TN'
            row['Bias'] = 0
        return row


    def filter_by(self, filter_gender: str = None, filter_race: str = None, filter_state: str = None):
        # ---- TODO: remove this code once PR with the updated filtering code is merged
        if filter_gender in ['Female', 'Male', 'Non-Binary', 'Other']:  # Check for Gender
            self._df = self._df[self._df['Gender'] == filter_gender]
        # ----
        # if filter_gender:
        #     # call formatter_gender on self.formatted_df
        # if filter_race:
        #     # call formatter_race on self.formatted_df
        # if filter_state:
        #     # call formatter_state on self.formatted_df
        return self


    def filter_invalid_transactions(self):
        """Creates a new dataset without any rows marked as blocked (i.e. False Positive (incorrectly blocked), True Positive (correctly blocked))
        """
        self._df = self._df[(self._df['confusion_value'] != 'FP') & (self._df['confusion_value'] != 'TP')]
        return self


    def _clean_data(self):
        """Remove any rows with missing values
         Convert the 'Timestamp' column to a datetime object."""

        self._df = self._df.dropna(axis=1)
        self._df['Timestamp'] = pd.to_datetime(self._df['Timestamp'])
        return self


    def get_for_display(self) -> pd.DataFrame:
        """Adjust on original_data to comform the display format for the graph."""
        self._clean_data()

        amount_df = self._df.groupby(self._df['Timestamp'].dt.strftime('%Y-%m-%d')).agg(
            num_transactions=('Transaction_Amount_USD', 'count')
        ).reset_index()
        amount_df = amount_df.rename(columns={'Timestamp': 'date'})

        count_df = self._df.groupby(self._df['Timestamp'].dt.strftime('%Y-%m-%d')).agg(
            revenue=('Transaction_Amount_USD', 'sum')
        ).reset_index()
        count_df = count_df.rename(columns={'Timestamp': 'date'})

        display_format = (amount_df.to_dict('records'), count_df.to_dict('records'))
        return display_format