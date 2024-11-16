import pandas as pd


# This is the GraphingData class.
# Only a DataFrame with two columns can be store here.
# Column 1 must be labelled "date" and column 2 must be
# labelled either "frequency" or "revenue".
class GraphingData:
    def __init__(self, data: pd.DataFrame):
        assert data.shape[1] == 2
        assert data.columns[1] in ["frequency", "revenue"]
        self.data = pd.DataFrame

    def getData(self) -> pd.DataFrame:
        return self.data
