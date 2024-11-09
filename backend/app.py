from flask import Flask, jsonify, request
from flask_cors import CORS
import read_data
from data_formatter import DataFormatter
from data_reader import DataReader

app = Flask('app')
CORS(app)
women_bias_data = DataReader('women_bias_data.csv').read_dataset()


# Example of an endpoint that returns test data
@app.route('/getinfo')
def getinfo():
    info = {"name":'breaking bias', "score":"awesome"}
    return jsonify(info)


@app.route('/getPastData', methods=['POST'])
def get_past_data():
    filter_gender = request.get_json()['filtering_factor']

    past_data = (DataFormatter(women_bias_data)
                 .filter_by(filter_gender)
                 .filter_invalid_transactions()
                 .get_formatted_df())

    return jsonify(past_data)


@app.route('/predictData', methods=['POST'])
def predict_values():
    filtering_factor = request.get_json()['filtering_factor']
    forecast_steps = request.get_json()['num_points']
    new_values = read_data.create_prediction_data(filtering_factor, forecast_steps, True)
    return jsonify(new_values)


@app.route('/getPastDataUnbiased', methods=['POST'])
def get_past_data_unbiased():
    filtering_factor = request.get_json()['filtering_factor']
    data = read_data.create_formatted_data(filtering_factor, False)
    return jsonify(data)


@app.route('/predictDataUnbiased', methods=['POST'])
def predict_values_unbiased():
    filtering_factor = request.get_json()['filtering_factor']
    forecast_steps = request.get_json()['num_points']
    new_values = read_data.create_prediction_data(filtering_factor, forecast_steps, False)
    return jsonify(new_values)


# This is to test that CI/CD pipeline is working. Delete later.
@app.route('/cicd_test')
def cicd_test():
    return jsonify("Hello World")


if __name__ == '__main__':
    app.run()
