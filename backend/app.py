import pandas as pd
from flask import Flask, jsonify, request
from flask_cors import CORS

from data_reader import DataReader
from file_uploader import FileUploader
from use_case_interactor import UseCaseInteractor
from data_access_interface import DataAccessInterface


class App:
    app: Flask
    name_of_file: str
    read_dataset: pd.DataFrame
    use_case_interactor: UseCaseInteractor
    data_access_interface: DataAccessInterface

    def __init__(self):
        self.app = Flask('app')
        CORS(self.app)
        self.name_of_file = 'women_bias_data.csv'
        self.read_dataset = DataReader(self.name_of_file).read_dataset()
        self.use_case_interactor = UseCaseInteractor(self.app, self.read_dataset)
        self.data_access_interface = DataAccessInterface(self.app, self.name_of_file)

        # Register routes
        self._register_routes()

    def get_app(self):
        return self.app

    def _register_routes(self):
        self.app.add_url_rule('/getinfo', 'getinfo', self.getinfo, methods=['GET'])

        self.app.add_url_rule('/getGraphData', 'get_graph_data', self.get_graph_data, methods=['POST'])

        self.app.add_url_rule('/getPastData', 'get_past_data', self.get_past_data, methods=['POST'])
        self.app.add_url_rule('/upload-dataset', 'upload_dataset', self.upload_dataset, methods=['POST'])
        self.app.add_url_rule('/getDatasets', 'get_datasets', self.get_datasets, methods=['GET'])

    def getinfo(self):
        info = {"name": 'breaking bias', "score": "stupendous"}
        return jsonify(info)

    def get_graph_data(self):
        return self.use_case_interactor.get_graph_data()

    def get_past_data(self):
        return self.use_case_interactor.get_past_data()

    def upload_dataset(self):
        return self.data_access_interface.upload_dataset()  # In this method self.read_dataset could be mutated.

    def get_datasets(self):
        return self.data_access_interface.get_datasets()

    def run(self):
        self.app.run()


# Initialize the app and run it
if __name__ == '__main__':
    app_instance = App()
    app_instance.run()
