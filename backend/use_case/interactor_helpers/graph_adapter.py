import pandas as pd
from entity.graphing_data import GraphingData


class GraphAdapter:
    """Adapter for the GraphingData class."""
    def __init__(self, revenue_past_biased_data: GraphingData,
                 revenue_predicted_biased_data: GraphingData = None,
                 revenue_past_unbiased_data: GraphingData = None,
                 revenue_predicted_unbiased_data: GraphingData = None):
        self.revenue_past_biased_data = revenue_past_biased_data
        self.revenue_past_unbiased_data = revenue_past_unbiased_data
        self.revenue_predicted_biased_data = revenue_predicted_biased_data
        self.revenue_predicted_unbiased_data = revenue_predicted_unbiased_data

    @staticmethod
    def helper_df_to_dict(df_to_convert: pd.DataFrame) -> list[dict]:
        return df_to_convert.to_dict('records')

    @staticmethod
    def helper_datetime_to_string(df_to_convert: pd.DataFrame) -> pd.DataFrame:
        df_to_convert['date'] = (pd.to_datetime(df_to_convert['date'])
                                 .dt.strftime('%Y-%m-%d'))
        return df_to_convert

    @staticmethod
    def helper_name_for_output(df_to_convert: pd.DataFrame) -> pd.DataFrame:
        if 'frequency' in df_to_convert.columns:
            df_to_convert = df_to_convert.rename(columns=({'frequency':
                                                           'value'}))
        if 'revenue' in df_to_convert.columns:
            df_to_convert = df_to_convert.rename(columns=({'revenue':
                                                           'value'}))
        return df_to_convert

    def getPastUnbiasedLine(self):
        result = self.revenue_past_unbiased_data.get_data()
        result = self.helper_datetime_to_string(result)
        result = self.helper_name_for_output(result)
        result = self.helper_df_to_dict(result)
        return result

    def getPredictedUnbiasedLine(self):
        result = self.revenue_predicted_unbiased_data.get_data()
        result = self.helper_datetime_to_string(result)
        result = self.helper_name_for_output(result)
        result = self.helper_df_to_dict(result)
        return result

    def getPastBiasedLine(self):
        result = self.revenue_past_biased_data.get_data()
        result = self.helper_datetime_to_string(result)
        result = self.helper_name_for_output(result)
        result = self.helper_df_to_dict(result)
        return result

    def getPredictedBiasedLine(self):
        result = self.revenue_predicted_biased_data.get_data()
        result = self.helper_datetime_to_string(result)
        result = self.helper_name_for_output(result)
        result = self.helper_df_to_dict(result)
        return result
