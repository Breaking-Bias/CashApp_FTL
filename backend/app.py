import pandas as pd
from flask import Flask, jsonify, request
from flask_cors import CORS

from data_access.data_reader import DataReader
from interface_adaptor.upload_file.upload_file_controller import UploadFileController
from use_case_interactor import UseCaseInteractor
from use_case.upload_file.upload_file_interactor import UploadFileInteractor

TEST_FILE_NAME = 'women_bias_data.csv'


class App:
    app: Flask
    data_access_interface: UploadFileInteractor
    read_dataset: pd.DataFrame
    use_case_interactor: UseCaseInteractor

    def __init__(self):
        self.app = Flask('app')
        CORS(self.app)
        self.data_access_interface = UploadFileInteractor(self.app)
        self.read_dataset = DataReader(self.data_access_interface.name_of_file
                                       or TEST_FILE_NAME).read_dataset()
        self.use_case_interactor = UseCaseInteractor(self.app, self.read_dataset)


        # Register routes
        self._register_routes()

    def get_app(self):
        return self.app

    def _register_routes(self):
        self.app.add_url_rule('/getinfo', 'getinfo', self.getinfo, methods=['GET'])
        self.app.add_url_rule('/upload-dataset', 'upload_dataset', self.upload_dataset, methods=['POST'])
        self.app.add_url_rule('/getDatasets', 'get_datasets', self.get_datasets, methods=['GET'])
        self.app.add_url_rule('/getGraphData', 'get_graph_data', self.get_graph_data, methods=['POST'])
        self.app.add_url_rule('/getPastData', 'get_past_data', self.get_past_data, methods=['POST'])


    def getinfo(self):
        info = {"name": 'breaking bias', "score": "stupendous"}
        return jsonify(info)

    def upload_dataset(self):
        """self.read_dataset is mutated."""
        # return self.data_access_interface.upload_dataset()
        files = request.files
        upload_file_controller = UploadFileController(files)
        result = upload_file_controller.execute()
        return jsonify(result[0]), result[1]


    def get_datasets(self):
        return self.data_access_interface.get_datasets()

    def get_graph_data(self):
        return self.use_case_interactor.get_graph_data()

    def get_past_data(self):
        return self.use_case_interactor.get_past_data()

    def run(self):
        self.app.run()


# Initialize the app and run it
if __name__ == '__main__':
    app_instance = App()
    app_instance.run()
