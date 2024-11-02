import pandas as pd
import os
from backend.Model import TARGET_VAR, Model

# Read the raw dataset from the csv
# TODO: May need to change csv file depending on our final data file.
def read_dataset():
    # Temporary
    # return {"data": "yes"}
    return pd.read_csv(os.path.join(os.path.dirname(__file__), "data", "transaction_data.csv"))

def create_model(filter):
    raw_data = read_dataset()
    # filtered_data = filter(raw_data, filtering_factor)  # to be checked with Carlos
    filtered_data = raw_data  # temporary
    return Model(filtered_data)

# Creates the data in the format that VISX needs
def create_formatted_data(filter):
    cleaned_data = create_model(filter).get_cleaned_data()
    formatted_data = [
        {'date': record['Date'].strftime('%Y-%m-%d'), 'value': record[TARGET_VAR]}
        for record in cleaned_data[['Date', TARGET_VAR]].drop_duplicates().to_dict(orient='records')
    ]
    return formatted_data

def create_prediction_data(filter, forecast_steps: int):
    model = create_model(filter)
    forecast_df = model.get_forecast()
    forecast_values = forecast_df['mean']
    future_dates = pd.date_range(start=model.get_cleaned_data().index[-1] + pd.DateOffset(months=0), periods=forecast_steps, freq='D')
    prediction_unformatted =  [{'date': date, 'value': value}
                        for date, value in zip(future_dates, forecast_values)]
    prediction_data = [{'date': record['date'].strftime('%Y-%m-%d'), 'value': int(record['value'])} for record in prediction_unformatted]
    return prediction_data

print(create_formatted_data('A'))



