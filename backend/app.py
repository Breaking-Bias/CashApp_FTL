from flask import Flask, jsonify, request
from flask_cors import CORS

from difference_calculator import DifferenceCalculator
from graph_adapter import GraphAdapter
from data_formatter import DataFormatter
from data_reader import DataReader
from model_interactor import ModelInteractor
from file_uploader import FileUploader

class App:
    def __init__(self):
        self.app = Flask('app')
        CORS(self.app)
        self.name_of_file = 'women_bias_data.csv'
        self.read_dataset = DataReader(self.name_of_file).read_dataset()

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
        filter_gender = request.get_json()['filtering_factor'][0]
        filter_race = request.get_json()['filtering_factor'][1]
        forecast_steps = request.get_json()['num_points']

        # initialize biased data
        formatted_past_data = (DataFormatter(self.read_dataset)
                               .filter_by(filter_gender, filter_race)
                               .filter_invalid_transactions())

        frequency_past_data_biased = formatted_past_data.get_frequency_data()
        revenue_past_data_biased = formatted_past_data.get_revenue_data()

        frequency_predicted_data_biased, revenue_predicted_data_biased = (
            ModelInteractor((frequency_past_data_biased,
                             revenue_past_data_biased))
            .execute(forecast_steps))

        # initialize unbiased  data
        formatted_past_data_unbiased = (DataFormatter(self.read_dataset)
                                        .filter_by(filter_gender, filter_race)
                                        .unbias()
                                        .filter_invalid_transactions())

        frequency_past_data_unbiased = formatted_past_data_unbiased.get_frequency_data()
        revenue_past_data_unbiased = formatted_past_data_unbiased.get_revenue_data()

        frequency_predicted_data_unbiased, revenue_predicted_data_unbiased = (
            ModelInteractor((frequency_past_data_unbiased,
                             revenue_past_data_unbiased))
            .execute(forecast_steps))

        # Calculate difference between biased and unbiased data
        revenue_difference_calculator_past = DifferenceCalculator(
            revenue_past_data_unbiased, revenue_past_data_biased)
        revenue_difference_calculator_predicted = DifferenceCalculator(
            revenue_predicted_data_unbiased, revenue_predicted_data_biased)

        frequency_difference_calculator_past = DifferenceCalculator(
            frequency_past_data_unbiased, frequency_past_data_biased)
        frequency_difference_calculator_predicted = DifferenceCalculator(
            frequency_predicted_data_unbiased, frequency_predicted_data_biased)

        # Collect all the data
        revenue_graph = GraphAdapter(revenue_past_data_biased,
                                     revenue_predicted_data_biased,
                                     revenue_past_data_unbiased,
                                     revenue_predicted_data_unbiased)

        frequency_graph = GraphAdapter(frequency_past_data_biased,
                                       frequency_predicted_data_biased,
                                       frequency_past_data_unbiased,
                                       frequency_predicted_data_unbiased)

        revenue_graph = {
            "past_biased_line": revenue_graph.getPastBiasedLine(),
            "predicted_biased_line": revenue_graph.getPredictedBiasedLine(),
            "past_unbiased_line": revenue_graph.getPastUnbiasedLine(),
            "predicted_unbiased_line": revenue_graph.getPredictedUnbiasedLine(),

            "total_difference":
                revenue_difference_calculator_past.volume_difference() +
                revenue_difference_calculator_predicted.volume_difference(),
            "average_difference":
                revenue_difference_calculator_past.average_difference() +
                revenue_difference_calculator_predicted.average_difference(),
        }

        frequency_graph = {
            "past_biased_line": frequency_graph.getPastBiasedLine(),
            "predicted_biased_line": frequency_graph.getPredictedBiasedLine(),
            "past_unbiased_line": frequency_graph.getPastUnbiasedLine(),
            "predicted_unbiased_line": frequency_graph.getPredictedUnbiasedLine(),

            "total_difference":
                frequency_difference_calculator_past.volume_difference() +
                frequency_difference_calculator_predicted.volume_difference(),
            "average_difference":
                frequency_difference_calculator_past.average_difference() +
                frequency_difference_calculator_predicted.average_difference(),
        }

        result = {
            "revenue_graph": revenue_graph,
            "frequency_graph": frequency_graph
        }
        return jsonify(result)

    def get_past_data(self):
        formatted_past_data = (DataFormatter(self.read_dataset)
                               .filter_invalid_transactions())

        frequency_past_data_biased = formatted_past_data.get_frequency_data()
        revenue_past_data_biased = formatted_past_data.get_revenue_data()

        # Collect all the data
        revenue_graph = GraphAdapter(revenue_past_data_biased)

        frequency_graph = GraphAdapter(frequency_past_data_biased)

        revenue_graph = {
            "past_biased_line": revenue_graph.getPastBiasedLine()
        }

        frequency_graph = {
            "past_biased_line": frequency_graph.getPastBiasedLine()
        }

        result = {
            "revenue_graph": revenue_graph,
            "frequency_graph": frequency_graph
        }


        return jsonify(result)

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
