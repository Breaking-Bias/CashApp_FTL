import pandas as pd
from flask import Flask, jsonify, request
from backend.use_case.prediction.prediction_interactor import PredictionInteractor


class UseCaseInteractor:
    app: Flask
    dataset: pd.DataFrame

    def __init__(self, app: Flask, dataset: pd.DataFrame):
        """app should be mutated by CORS() before calling this method."""
        self.app = app
        self.dataset = dataset

    def get_graph_data(self):
        filter_gender = request.get_json()['filtering_factor'][0]
        filter_race = request.get_json()['filtering_factor'][1]
        forecast_steps = request.get_json()['num_points']
        get_graph_interactor = PredictionInteractor(self.dataset, filter_gender, filter_race, forecast_steps)
        result = get_graph_interactor.make_prediction()
        return jsonify(result)

    # def get_past_data(self):
    #     get_graph_interactor = GetGraphInteractor(self.dataset, "NoFilter", "NoFilter", 0)
    #     result = get_graph_interactor.make_graph_only_past()
    #     return jsonify(result)
