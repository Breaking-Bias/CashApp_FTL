import pandas as pd

from data_access.data_access_object import DataAccessObject
from use_case.interactor_helpers.get_graph_interactor import GetGraphInteractor


class ViewResultInteractor:
    dataset: pd.DataFrame

    def __init__(self, file_name: str):
        self.dataset = DataAccessObject(file_name).read_dataset()

    def get_past_data(self):
        get_graph_interactor = GetGraphInteractor(self.dataset, "NoFilter", "NoFilter", 0)
        result = get_graph_interactor.make_graph_only_past()
        # return jsonify(result)
        return result