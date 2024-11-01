import pandas as pd
import os
from backend.Model import TARGET_VAR, Model

# Read the raw dataset from the csv
# TODO: May need to change csv file depending on our final data file.
def read_dataset():
    # Temporary
    # return {"data": "yes"}
    return pd.read_csv(os.path.join(os.path.dirname(__file__), "data", "transaction_data.csv"))

# Creates the data in the format that VISX needs
# TODO: Indicate return type (pandas.DataFrame)
def create_formatted_data():
    raw_data = read_dataset()
    cleaned_data = Model(raw_data).cleaned_data
    # formatted_data = cleaned_data[['Date', TARGET_VAR]].to_dict(orient='records')  # list of dicts
    formatted_data = [
        {'date': record['Date'].strftime('%Y-%m-%d'), 'value': record[TARGET_VAR]}
        for record in cleaned_data[['Date', TARGET_VAR]].to_dict(orient='records')
    ]
    return formatted_data

# TODO: dataset: str is temporary; need to figure out the return type of create_formatted_data()
def create_prediction_data(dataset: str, bias: any):
    """This function filters the given dataset based on the given bias.
    Returns a filtered dataset.
    For example:
    create_prediction_data(data, "Female")
    returns:
    data with all "Female" rows marked with bias removed.

    Precondition: dataset is already formatted and cleaned (i.e. dates are in datetime format, redundant rows have been deleted)
    """
    data = dataset.copy()

    # TODO: There may be issues with 'Other' since it exists in both race and gender/
    if bias == 'Female' or bias == 'Male' or bias == 'Non-Binary' or bias == 'Other':
        data_gen = data[~((data['Is_Action_Biased'] == 'approve') & (data['Gender'] == bias))]
    elif bias == 'Black' or bias == 'White' or bias == 'Asian' or bias == 'Hispanic' or bias == 'Mixed' or bias == 'Other':
        data_gen = data[~((data['Is_Action_Biased'] == 'approve') & (data['Race'] == bias))]
    elif isinstance(bias, int):
        data_gen = data[~((data['Is_Action_Biased'] == 'approve') & (data['Age'] == bias))]
    else:
        pass
    return data

print(create_formatted_data())

