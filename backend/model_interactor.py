from model import Model
from graphing_data import GraphingData
import pandas as pd


class ModelInteractor:
    training_data: tuple[GraphingData, GraphingData]

    def __init__(self, training_data: tuple[GraphingData, GraphingData]):
        self.training_data = training_data

    @staticmethod
    def _graphingdata_to_onecol(graphing_data: GraphingData) -> pd.DataFrame:
        """Convert GraphingData to one-column date-indexed DataFrame."""
        df = graphing_data.getData().copy()
        # TODO: Remove this .copy when .copy is added in GraphingData.
        df.set_index('date', inplace=True)
        return df

    @staticmethod
    def _onecol_to_graphingdata(df: pd.DataFrame) -> GraphingData:
        """Convert one-column date-indexed DataFrame to GraphingData."""
        column_name = df.columns[0]
        df = df.reset_index()
        df.columns = ['date', column_name]
        return GraphingData(df)

    @staticmethod
    def _add_back_missing_dates(data: GraphingData) -> pd.DataFrame:
        """Returning DataFrame is one-col date-indexed."""
        df = ModelInteractor._graphingdata_to_onecol(data)
        all_dates = pd.date_range(start=df.index.min(), end=df.index.max(), freq='D')
        df = df.reindex(all_dates, fill_value=0)
        ModelInteractor._set_date_index(df)
        return df

    @staticmethod
    def _set_date_index(df):
        df.index = df.index.date
        df.index.name = 'date'

    def get_for_predicting(self) -> tuple[pd.DataFrame, pd.DataFrame]:
        """Formats the data for Model input."""
        frequency_df, revenue_df = self.training_data
        frequency_df = ModelInteractor._add_back_missing_dates(frequency_df)
        revenue_df = ModelInteractor._add_back_missing_dates(revenue_df)
        return frequency_df, revenue_df

    def execute(self, forecast_steps: int) -> tuple[GraphingData, GraphingData]:
        frequency_df, revenue_df = self.get_for_predicting()
        pred_frequency = (Model(frequency_df).predict().get_result(forecast_steps)
                          .rename(columns={'mean': 'frequency'}))
        pred_frequency = GraphingData(pred_frequency)
        pred_revenue = (Model(revenue_df).predict().get_result(forecast_steps)
                        .rename(columns={'mean': 'revenue'}))
        pred_revenue = GraphingData(pred_revenue)
        return pred_frequency, pred_revenue



