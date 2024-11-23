import pandas as pd
import os
from data_access.data_access_object import DataAccessObject


# TODO: May need to change csv file depending on our final data file.
class DataReader:
    file_name: str

    def __init__(self, file_name: str):
        self.file_name = file_name

    def read_dataset(self):
        try:
            dataset_path = os.path.join(os.path.dirname(__file__), "data", self.file_name)
            dataset = pd.read_csv(dataset_path)
            data_access_object = DataAccessObject(dataset)
            # return data_access_object
            return dataset
        except FileNotFoundError:
            print(f"Error: The file {dataset_path} does not exist.")
            return None