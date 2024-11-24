import pandas as pd
import datetime

from data_access.data_reader import DataReader
from data_access.file_uploader import FileUploader


class DataAccessObject:
    df: pd.DataFrame
    data_reader: DataReader
    file_uploader: FileUploader

    def __init__(self, df: pd.DataFrame):
        self.df = df

    def get_data(self) -> pd.DataFrame:
        return self.df

    def get_column(self, column_name: str) -> pd.Series:
        return self.df[column_name]

    def get_row(self, index: int) -> pd.Series:
        return self.df.iloc[index]

    def get_rows(self, start: int, end: int) -> pd.DataFrame:
        return self.df.iloc[start:end]

    def get_rows_by_date(self, start_date: datetime.date, end_date: datetime.date) -> pd.DataFrame:
        mask = (self.df['Date'] >= start_date) & (self.df['Date'] <= end_date)
        return self.df.loc[mask]

    def get_column_by_date(self, column_name: str, start_date: datetime.date, end_date: datetime.date) -> pd.Series:
        mask = (self.df['Date'] >= start_date) & (self.df['Date'] <= end_date)
        return self.df.loc[mask, column_name]