import pandas as pd
import os
from Model import TARGET_VAR, Model

# Read the raw dataset from the csv
# TODO: May need to change csv file depending on our final data file.
def read_dataset():
    # Temporary
    # return {"data": "yes"}
    try:
        file_path = os.path.join(os.path.dirname(__file__), "data", "women_bias_data.csv")
        dataset = pd.read_csv(file_path)
        return dataset
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
        return None

def filter_by_factor(data: pd.DataFrame, filtering_factor: str):
    """Returns a dataset of all the transactions from the given group in filtering_factor.  
    Parameters:
    - data: pd.DataFrame
    - filtering_factor: str
    Returns:
    - displayed_data: pd.DataFrame
    """
    pass


def unbias(display_data: pd.DataFrame):
    """Filters out all the bias within a dataset.
    It flips all the transactions that have been marked as biased to unbiased, and return a fully unbiased dataset.
    Changes all the false positives to true negatives
    Parameter:
    - display_data: pd.DataFrame
    Returns:
    - unbiased_data: pd.DataFrame
    """
    new_dataframe=display_data.apply(apply_helper_for_unbias, axis=1)
    return new_dataframe


def apply_helper_for_unbias(row):
    if row['confusion_value']=='FP':
        row['confusion_value']='TN'
    return row



def filter_for_valid_transactions(display_data: pd.DataFrame):
    """Creates a new dataset without any rows marked as blocked (i.e. False Positive (incorrectly blocked), True Positive (correctly blocked))
    """
    filtered_df = display_data[(display_data['confusion_value'] != 'FP') & (display_data['confusion_value'] != 'TP')]
    return filtered_df


    

def create_model(filtering_factor, bias: bool):
    """Creates an arima model for a given dataset.
    Gives the option to create a model for a dataset with (True) or without bias (False).
    """
    raw_data = read_dataset()
    # filtered_data = filter(raw_data, filtering_factor)  # to be checked with Carlos
    filtered_data = raw_data  # temporary

    # displayed_data = display(raw_data, filtering_factor)
    # if bias == False
    #       unbiased_displayed_data = unbias(displayed_data)
    # return Model(unbiased_displayed_data)
    return Model(filtered_data)

# Creates the data in the format that VISX needs
def create_formatted_data(filtering_factor, bias: bool):
    """Formats the data to adhere to the frontend requirements.
    """
    cleaned_data = create_model(filtering_factor, bias).get_cleaned_data()
    formatted_data = [
        {'date': record['Date'].strftime('%Y-%m-%d'), 'value': record[TARGET_VAR]}
        for record in cleaned_data[['Date', TARGET_VAR]].drop_duplicates().to_dict(orient='records')
    ]
    return formatted_data

def create_prediction_data(filtering_factor, forecast_steps: int, bias: bool):
    """Returns the data that the arima model predicts 
    """
    model = create_model(filtering_factor, bias)
    forecast_df = model.get_forecast()
    forecast_values = forecast_df['mean']
    future_dates = pd.date_range(start=model.get_cleaned_data().index[-1] + pd.DateOffset(months=0), periods=forecast_steps, freq='D')
    prediction_unformatted =  [{'date': date, 'value': value}
                        for date, value in zip(future_dates, forecast_values)]
    prediction_data = [{'date': record['date'].strftime('%Y-%m-%d'), 'value': int(record['value'])} for record in prediction_unformatted]
    return prediction_data

