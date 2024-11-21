import pandas as pd
from flask import Flask, jsonify, request
from flask_cors import CORS

from difference_calculator import DifferenceCalculator
from graph_adapter import GraphAdapter
from data_formatter import DataFormatter
from data_reader import DataReader
from model_interactor import ModelInteractor
from file_uploader import FileUploader
from use_case_interactor import UseCaseInteractor


class App:
    app: Flask
    name_of_file: str
    read_dataset: pd.DataFrame
    use_case_interactor: UseCaseInteractor

    def __init__(self):
        self.app = Flask('app')
        CORS(self.app)
        self.name_of_file = 'women_bias_data.csv'
        self.read_dataset = DataReader(self.name_of_file).read_dataset()
        self.use_case_interactor = UseCaseInteractor(self.app, self.read_dataset)

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
        """Endpoint to handle file upload."""
        print('firstfile:', self.name_of_file)
        # Initialize FileUploader within the route
        file_uploader = FileUploader(upload_folder='data', allowed_extensions={'csv', 'xlsx', 'pq'})

        if 'file' not in request.files:
            return jsonify({"message": "No file part"}), 400
        file = request.files['file']
        if file.filename == '':
            return jsonify({"message": "No selected file"}), 400
        file_path = file_uploader.save_file(file)
        if file_path:
            self.name_of_file = file_uploader.nameoffile
            self.read_dataset = DataReader(self.name_of_file).read_dataset()
            print(self.name_of_file)
            return jsonify({"message": "File uploaded successfully", "file_path": file_path}), 200
        else:
            return jsonify({"message": "Invalid file format. Only CSV and XLSX are allowed."}), 400

    def get_datasets(self):
        file_uploader = FileUploader(upload_folder='data', allowed_extensions={'csv', 'xlsx', 'pq'})
        try:
            datasets = file_uploader.list_datasets()
            return jsonify({"datasets": datasets}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    def run(self):
        self.app.run()

# Initialize the app and run it
if __name__ == '__main__':
    app_instance = App()
    app_instance.run()
