from flask import Flask, jsonify, request
from flask_cors import CORS
from data_formatter import DataFormatter
from data_reader import DataReader
from model_interactor import ModelInteractor
from file_uploader import FileUploader

app = Flask('app')
CORS(app)
women_bias_data = DataReader('women_bias_data.csv').read_dataset()


# Example of an endpoint that returns test data
@app.route('/getinfo')
def getinfo():
    info = {"name": 'breaking bias', "score": "stupendous"}
    return jsonify(info)


@app.route('/getPastData', methods=['POST'])
def get_past_data():
    filter_gender = request.get_json()['filtering_factor']

    past_data = (DataFormatter(women_bias_data)
                 .filter_by(filter_gender)
                 .filter_invalid_transactions()
                 .get_for_display())
    print(past_data)
    return jsonify(past_data)


@app.route('/predictData', methods=['POST'])
def predict_values():
    filter_gender = request.get_json()['filtering_factor']
    forecast_steps = request.get_json()['num_points']
    training_data = (DataFormatter(women_bias_data)
                     .filter_by(filter_gender)
                     .filter_invalid_transactions()
                     .get_for_predicting())

    return_data = ModelInteractor(training_data).execute(forecast_steps)
    return jsonify(return_data)


@app.route('/getPastDataUnbiased', methods=['POST'])
def get_past_data_unbiased():
    filter_gender = request.get_json()['filtering_factor']

    past_data = (DataFormatter(women_bias_data)
                 .filter_by(filter_gender)
                 .unbias()
                 .filter_invalid_transactions()
                 .get_for_display())

    return jsonify(past_data)


@app.route('/predictDataUnbiased', methods=['POST'])
def predict_values_unbiased():
    filter_gender = request.get_json()['filtering_factor']
    forecast_steps = request.get_json()['num_points']
    training_data = (DataFormatter(women_bias_data)
                     .filter_by(filter_gender)
                     .unbias()
                     .filter_invalid_transactions()
                     .get_for_predicting())

    return_data = ModelInteractor(training_data).execute(forecast_steps)
    return jsonify(return_data)

@app.route('/upload-dataset', methods=['POST'])
def upload_dataset():
    """Endpoint to handle file upload."""
    # Initialize FileUploader within the route
    file_uploader = FileUploader(upload_folder='data', allowed_extensions={'csv', 'xlsx', 'pq'})

    if 'file' not in request.files:
        return jsonify({"message": "No file part"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"message": "No selected file"}), 400
    file_path = file_uploader.save_file(file)
    if file_path:
        return jsonify({"message": "File uploaded successfully", "file_path": file_path}), 200
    else:
        return jsonify({"message": "Invalid file format. Only CSV and XLSX are allowed."}), 400
    
@app.route('/getDatasets', methods=['GET'])
def get_datasets():

    file_uploader = FileUploader(upload_folder='data', allowed_extensions={'csv', 'xlsx', 'pq'})
    try:
        datasets = file_uploader.list_datasets()
        return jsonify({"datasets": datasets}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500






if __name__ == '__main__':
    app.run()
