import pandas as pd

class DataFormatter:
    """
    A class used to format and process transaction data.

    Attributes
    ----------
    _df : pd.DataFrame
        A copy of the DataFrame to be formatted.

    Methods
    -------
    get_formatted_df():
        Returns the formatted DataFrame.

    unbias():
        Adjusts the DataFrame to remove bias from the data.

    filter_by(filter_gender: str = None, filter_race: str = None, filter_state: str = None):
        Filters the DataFrame based on gender, race, or state.

    filter_invalid_transactions():
        Removes rows marked as blocked (False Positive or True Positive).

    _clean_data():
        Cleans the DataFrame by removing rows with missing values and converting the 'Timestamp' column to datetime.

    get_for_display() -> pd.DataFrame:
        Formats the data for display, grouping by date and aggregating transaction counts and revenue.
    """
    _df: pd.DataFrame


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
        """Remove any columns with missing values
         Convert the 'Timestamp' column to a datetime object."""

        self._df = self._df.dropna(axis=1)
        self._df['Timestamp'] = pd.to_datetime(self._df['Timestamp'])
        return self


    @staticmethod
    def helper_df_to_dict(df_to_convert):
        return df_to_convert.to_dict('records')


    def _helper_output_df_format(self):
        self._clean_data()

        amount_df = self._df.groupby(self._df['Timestamp'].dt.strftime('%Y-%m-%d')).agg(
            num_transactions=('Transaction_Amount_USD', 'count')
        ).reset_index()
        amount_df = amount_df.rename(columns={'Timestamp': 'date'})

        count_df = self._df.groupby(self._df['Timestamp'].dt.strftime('%Y-%m-%d')).agg(
            revenue=('Transaction_Amount_USD', 'sum')
        ).reset_index()
        count_df = count_df.rename(columns={'Timestamp': 'date'})

        return amount_df, count_df


    def get_for_display(self) -> pd.DataFrame:
        """Adjust on original_data to comform the display format for the graph."""
        amount_df, count_df = self._helper_output_df_format()
        display_format = (DataFormatter.helper_df_to_dict(amount_df), DataFormatter.helper_df_to_dict(count_df))

        return display_format


    def get_for_predicting(self) -> pd.DataFrame:
        """Adjust on original_data to comform the model prediction format for the graph."""
        amount_df, count_df = self._helper_output_df_format()

        return amount_df, count_df

