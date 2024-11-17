import pandas as pd


# This is the GraphingData class.
# Only a DataFrame with two columns can be store here.
# Column 1 must be labelled "date" and column 2 must be
# labelled either "frequency" or "revenue".
class GraphingData:
    data: pd.DataFrame

    def __init__(self, data: pd.DataFrame):
        assert data.shape[1] == 2, "Data must have exactly 2 columns."

        assert data.columns[0] == "date", "First column header must be 'date'."
        assert all(self._is_valid_date(val) for val in data.iloc[:, 0]),\
            "All values in the date col must be pd.to_datetime().date objects."

        assert data.columns[1] in ["frequency", "revenue"], \
            "Second column header must be 'frequency' or 'revenue'."
        self.data = data

    @staticmethod
    def _is_valid_date(val) -> bool:
        return (isinstance(val, pd.Timestamp) and
                val.time() == pd.Timestamp.min.time())

    def get_data(self) -> pd.DataFrame:
        return self.data
