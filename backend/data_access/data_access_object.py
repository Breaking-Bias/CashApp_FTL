import pandas as pd
import os


# TODO: May need to change csv file depending on our final data file.
class DataAccessObject:
    """Data Access Object for reading the dataset.
    Reads csv files and returns as a pandas DataFrame.
    """
    file_name: str

    def __init__(self, file_name: str):
        self.file_name = file_name
        self.dataset = self.read_dataset()

    def read_dataset(self):
        try:
            dataset_path = os.path.join(os.path.dirname(__file__), "data", self.file_name)
            dataset = pd.read_csv(dataset_path)
            return dataset
        except FileNotFoundError:
            print(f"Error: The file {dataset_path} does not exist.")
            return None
