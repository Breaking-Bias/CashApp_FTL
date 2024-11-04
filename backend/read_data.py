import pandas as pd
import os
from Model import TARGET_VAR, Model

# Read the raw dataset from the csv
# TODO: May need to change csv file depending on our final data file.
def read_dataset():
    # Temporary
    # return {"data": "yes"}
    return pd.read_csv(os.path.join(os.path.dirname(__file__), "data", "women_bias_data.csv"))

def filter_by_factor(data: pd.DataFrame, filtering_factor: str):
    """Returns a dataset of only the transaction in the given group in filtering_factor.  
    Parameters:
    - data: pd.DataFrame
    - filtering_factor: str
    Returns:
    - displayed_data: pd.DataFrame
    """
    filtered_data = data.copy()

    if isinstance(filtering_factor, int):  # Check for Age
        if 0 <= filtering_factor < 18:
            filtered_data = filtered_data[(filtered_data['Age'] >= 0) & (filtered_data['Age'] < 18)]
        elif 18 <= filtering_factor < 35:
            filtered_data = filtered_data[(filtered_data['Age'] >= 18) & (filtered_data['Age'] < 35)]
        elif 35 <= filtering_factor < 65:
            filtered_data = filtered_data[(filtered_data['Age'] >= 35) & (filtered_data['Age'] < 65)]
        elif 65 <= filtering_factor:
            filtered_data = filtered_data[(filtered_data['Age'] >= 65)]
        else:  # Negative number will raise error (this won't be the case, however we should keep it for clean code)
            raise ValueError("Invalid filtering_factor: negative age is not allowed.")
    # TODO: having 'Other' categories in Gender and Race may cause bugs. We should rename one of these.
    elif filtering_factor in ['Female', 'Male', 'Non-Binary', 'Other']:  # Check for Gender
        filtered_data = filtered_data[filtered_data['Gender'] == filtering_factor]
    elif filtering_factor in ['Black', 'White', 'Asian', 'Hispanic', 'Mixed', 'Other']:  # Check for Race
        filtered_data = filtered_data[filtered_data['Race'] == filtering_factor]
    elif isinstance(filtering_factor, str) and len(filtering_factor) == 2 and filtering_factor.isupper():  # Check for State
        filtered_data = filtered_data[filtered_data['State'] == filtering_factor]
    else:
        raise ValueError("Invalid filtering_factor: does not match any known filter type.")

    return filtered_data

def unbias(display_data: pd.DataFrame):
    """Filters out all the bias within a dataset.
    It flips all the transactions that have been marked as biased to unbiased, and return a fully unbiased dataset.
    Changes all the false positives to true negatives
    Parameter:
    - display_data: pd.DataFrame
    Returns:
    - unbiased_data: pd.DataFrame
    """
    pass

def filter_for_valid_transactions():
    """Creates a new dataset without any rows marked as blocked (i.e. False Positive (incorrectly blocked), True Positive (correctly blocked))
    """
    pass

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
