import pandas as pd
from flask import Flask, jsonify, request
from flask_cors import CORS
from werkzeug.datastructures import FileStorage
import io

from data_access.data_access_object import DataAccessObject
from interface_adaptor.upload_file.upload_file_controller import UploadFileController
from interface_adaptor.view_result.view_result_controller import ViewResultController
from interface_adaptor.prediction.prediction_controller import PredictionController

# this use case interactor should be removed later on
from use_case_interactor import UseCaseInteractor

TEST_FILE_NAME = 'women_bias_data.csv'

class App:
    app: Flask
    file_name: str
    upload_file_controller: UploadFileController
    view_result_controller: ViewResultController
    prediction_controller: PredictionController

    # data_access_interface: UploadFileInteractor
    # read_dataset: pd.DataFrame
    use_case_interactor: UseCaseInteractor

    def __init__(self):
        self.app = Flask('app')
        CORS(self.app)
        self.upload_file_controller = UploadFileController()
        self.file_name = TEST_FILE_NAME
        self.view_result_controller = ViewResultController(self.file_name, )
        # following are temporary
        self.read_dataset = DataAccessObject(self.upload_file_controller.filename
                                       or TEST_FILE_NAME).read_dataset()
        
        filter_gender = request.get_json()['filtering_factor'][0]
        filter_race = request.get_json()['filtering_factor'][1]
        forecast_steps = request.get_json()['num_points']
        self.prediction_controller = PredictionController(self.read_dataset, filter_gender, filter_race, forecast_steps)
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
        """mutating many fields in App"""
        # return self.data_access_interface.upload_dataset()
        result = self.upload_file_controller.execute()
        self.file_name = self.upload_file_controller.filename
        self.view_result_controller = ViewResultController(self.file_name)
        return jsonify(result[0]), result[1]

    def get_datasets(self):
        # return self.data_access_interface.get_datasets()
        result = self.upload_file_controller.get_datasets_from_interactor()
        return jsonify(result[0]), result[1]
    
    # TODO: We don't need this anymore
    def get_graph_data(self):
        result = self.use_case_interactor.get_graph_data()
        return result

    def get_past_data(self):
        # return self.use_case_interactor.get_past_data()
        result = self.view_result_controller.get_past_data_from_interactor()
        return jsonify(result)
    
    def get_prediction_data(self):
        result = self.prediction_controller.execute()
        return jsonify(result)

    def run(self):
        self.app.run()


# Initialize the app and run it
if __name__ == '__main__':
    app_instance = App()
    app_instance.run()
