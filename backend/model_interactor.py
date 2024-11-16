from model import Model
from graphing_data import GraphingData
import pandas as pd


class ModelInteractor:
    training_data: tuple[GraphingData, GraphingData]

    def __init__(self, training_data: tuple[GraphingData, GraphingData]):
        self.training_data = training_data

    @staticmethod
    def _add_back_missing(df: pd.DataFrame) -> pd.DataFrame:
        df.set_index('date', inplace=True)
        all_dates = pd.date_range(start=df.index.min(), end=df.index.max(), freq='D')
        df = ModelInteractor._reindex_with_dates(all_dates, df)
        return df

    @staticmethod
    def _reindex_with_dates(all_dates, df):
        df = df.reindex(all_dates, fill_value=0)
        df.index = df.index.date
        df.index.name = 'date'
        return df

    def get_for_predicting(self) -> tuple[pd.DataFrame, pd.DataFrame]:
        """Formats the data for out."""
        frequency_df, revenue_df = self.training_data
        frequency_df = ModelInteractor._add_back_missing(frequency_df)
        revenue_df = ModelInteractor._add_back_missing(revenue_df)
        return frequency_df, revenue_df

    def execute(self, forecast_steps: int) -> tuple[GraphingData, GraphingData]:
        frequency_df, revenue_df = self.get_for_predicting()
        model_frequency, model_revenue = Model(frequency_df), Model(revenue_df)
        pred_frequency = (model_frequency.predict().get_result(forecast_steps)
                          .rename(columns={'mean': 'frequency'}))
        pred_frequency = ModelInteractor._to_graphingdata(pred_frequency)
        pred_revenue = (model_revenue.predict().get_result(forecast_steps)
                        .rename(columns={'mean': 'revenue'}))
        pred_revenue = ModelInteractor._to_graphingdata(pred_revenue)

    @staticmethod
    def _to_graphingdata(df: pd.DataFrame) -> GraphingData:
        df['date'] = pd.to_datetime(df['date']).dt.strftime('%Y-%m-%d')
        return df


# class ModelInteractor:
#     training_data:  tuple[pd.DataFrame, pd.DataFrame]
#
#     def __init__(self, training_data:  tuple[pd.DataFrame, pd.DataFrame]):
#         self.training_data = training_data
#
#     def execute(self, forecast_steps: int) -> tuple[list[dict], list[dict]]:
#         model_amount = Model(self.training_data[0])
#         pred_trans_amount = (model_amount.predict().get_result(forecast_steps)
#                              .rename(columns={'mean': 'frequency'}))
#         pred_trans_amount = ModelInteractor._process_data(pred_trans_amount)
#
#         model_count = Model(self.training_data[1])
#         pred_trans_count = (model_count.predict().get_result(forecast_steps)
#                             .rename(columns={'mean': 'revenue'}))
#         pred_trans_count = ModelInteractor._process_data(pred_trans_count)
#         # Don't rename the columns here, otherwise frontend won't work.
#
#         return pred_trans_amount, pred_trans_count
#
#     @staticmethod
#     def _process_data(data: pd.DataFrame) -> list[dict]:
#         processed_data = DataFormatter.helper_datetime_to_string(data)
#         processed_data = DataFormatter.helper_df_to_dict(processed_data)
#
#         return processed_data
