import pandas as pd


# This is the GraphingData class.
# Only a DataFrame with two columns can be store here.
# Column 1 must be labelled "date" and column 2 must be
# labelled either "frequency" or "revenue".
class GraphingData:
    data: pd.DataFrame

    def __init__(self, data: pd.DataFrame):
        assert data.shape[1] == 2, "Data must have exactly 2 columns."
        assert data.columns[0] == "date", "First column header must be 'data'."
        assert data.columns[1] in ["frequency", "revenue"], "Second column header must be 'frequency' or 'revenue'."
        self.data = data

    def getData(self) -> pd.DataFrame:
        return self.data
