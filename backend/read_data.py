import pandas as pd
import os
from Model import TARGET_VAR, Model

# Read the raw dataset from the csv
def read_dataset():
    # Temporary
    # return {"data": "yes"}
    return pd.read_csv(os.path.join(os.path.dirname(__file__), "data", "transaction_data.csv"))

# Creates the data in the format that VISX needs
def create_formatted_data():
    raw_data = read_dataset()
    cleaned_data = Model(raw_data).cleaned_data
    # formatted_data = cleaned_data[['Date', TARGET_VAR]].to_dict(orient='records')  # list of dicts
    formatted_data = [
        {'date': record['Date'].strftime('%Y-%m-%d'), 'value': record[TARGET_VAR]}
        for record in cleaned_data[['Date', TARGET_VAR]].to_dict(orient='records')
    ]
    return formatted_data

def create_prediction_data():
    ...

print(create_formatted_data())

