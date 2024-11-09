import pandas as pd
import os

# Read the raw dataset from the csv
# TODO: May need to change csv file depending on our final data file.
class DataReader:
    def __init__(self, file_name: str):
        self.file_name = file_name

    def read_dataset(self):
        try:
            dataset_path = os.path.join(os.path.dirname(__file__), "data", self.file_name)
            dataset = pd.read_csv(dataset_path)
            return dataset
        except FileNotFoundError:
            print(f"Error: The file {dataset_path} does not exist.")
            return None