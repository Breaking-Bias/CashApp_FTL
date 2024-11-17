import pandas as pd
import datetime


# This is the GraphingData class.
# Only a DataFrame with two columns can be store here.
# Column 1 must be labelled "date" and column 2 must be
# labelled either "frequency" or "revenue".
class GraphingData:
    data: pd.DataFrame

    def __init__(self, data: pd.DataFrame):
        assert data.shape[1] == 2, "Data must have exactly 2 columns."

        assert data.columns[0] == "date", "First column header must be 'date'."

        assert all(data.iloc[:, 0].apply(self._is_valid_date)),\
            "All values in the first column must be pd.Timestamp.date objects."

        assert data.columns[1] in ["frequency", "revenue"], \
            "Second column header must be 'frequency' or 'revenue'."
        self.data = data.copy()

    @staticmethod
    def _is_valid_date(val) -> bool:
        return isinstance(val, datetime.date)

    def get_data(self) -> pd.DataFrame:
        return self.data
    
    def is_equal(self, other: 'GraphingData') -> bool:
        if not isinstance(other, GraphingData):
            return False
        return self.data.equals(other.data)
