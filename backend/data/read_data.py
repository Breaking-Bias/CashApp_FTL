import pandas as pd

# Read the raw dataset from the csv
def read_dataset():
    # Temporary
    return {"data": "yes"}

# Creates the data in the format that VISX needs
def create_formatted_data():
    raw_data = read_dataset()

    desired_output = [
        {"date": "2023-07-01", "value": 50}, 
        {"date": "2023-07-02", "value": 52}, 
        {"date": "2023-07-03", "value": 55}, 
        {"date": "2023-07-04", "value": 54}, 
        {"date": "2023-07-05", "value": 57}, 

    ]

    # Temporary
    formatted_data = desired_output
    
    return formatted_data
