from model import Model
from data_formatter import DataFormatter
import pandas as pd


class ModelInteractor:
    training_data:  tuple[pd.DataFrame, pd.DataFrame]

    def __init__(self, training_data:  tuple[pd.DataFrame, pd.DataFrame]):
        self.training_data = training_data

    def execute(self, forecast_steps: int) -> tuple[list[dict], list[dict]]:
        model_amount = Model(self.training_data[0])
        pred_trans_amount = (model_amount.predict().get_result(forecast_steps)
                             .rename(columns={'mean': 'frequency'}))
        pred_trans_amount = ModelInteractor._process_data(pred_trans_amount)

        model_count = Model(self.training_data[1])
        pred_trans_count = (model_count.predict().get_result(forecast_steps))
                            # .rename(columns={'mean': 'revenue'}))
        pred_trans_count = ModelInteractor._process_data(pred_trans_count)
        # Don't rename the columns here, otherwise frontend won't work.

        return pred_trans_amount, pred_trans_count

    @staticmethod
    def _process_data(data: pd.DataFrame) -> list[dict]:
        processed_data = DataFormatter.helper_datetime_to_string(data)
        processed_data = DataFormatter.helper_df_to_dict(processed_data)

        return processed_data
