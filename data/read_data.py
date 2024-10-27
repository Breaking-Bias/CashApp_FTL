import pandas as pd

# Read the raw dataset from the csv
def read_dataset():
    # Temporary
    return {"data": "yes"}

# Creates the data in the format that VISX needs
def create_formatted_data():
    raw_data = read_dataset()

    desired_output = [
        {"2023-07-01": 50}, 
        {"2023-07-02": 52}, 
        {"2023-07-03": 55},
        {"2023-07-04": 54},
        {"2023-07-03": 57}
    ]

    # Temporary
    formatted_data = desired_output
    
    return formatted_data
