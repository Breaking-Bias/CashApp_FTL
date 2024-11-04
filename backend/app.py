from flask import Flask, jsonify, request
from flask_cors import CORS
import read_data

app = Flask('app')
CORS(app)

# Example of an endpoint that returns test data
@app.route('/getinfo')
def getinfo():
    info = {"name":'breaking bias', "score":"awesome"}
    return jsonify(info)

@app.route('/getOriginalData')
def getOriginalData():
    data = backend.read_data.create_formatted_data('female')  # Filter is temporarily hardcoded.

    # # TEMPORARY FOR FRONTEND TESTING
    # data = [
    #     {
    #         "date": "2024-08-01",
    #         "value": 50
    #     },
    #     {
    #         "date": "2024-08-02",
    #         "value": 55
    #     },
    #     {
    #         "date": "2024-08-03",
    #         "value": 70
    #     },
    #     {
    #         "date": "2024-08-04",
    #         "value": 60
    #     },
    # ]
    return jsonify(data)

@app.route('/predictValues', methods=['POST'])
def predictValues():
    data = request.get_json()
    forecast_steps = data['numPoints']
    new_values = backend.read_data.create_prediction_data('A', forecast_steps)

    # # TEMPORARY FOR FRONTEND TESTING
    # new_values = [
    #     {
    #         "date": "2024-08-05",
    #         "value": 73
    #     },
    #     {
    #         "date": "2024-08-06",
    #         "value": 88
    #     },
    #     {
    #         "date": "2024-08-07",
    #         "value": 82
    #     }
    # ]

    return jsonify(new_values)

@app.route('/getDummyData')
def getFormattedData():
    data = backend.read_data.create_formatted_data().to_json()
    return jsonify(data)


# This is to test that CI/CD pipeline is working. Delete later.
@app.route('/cicd_test')
def cicd_test():
    return jsonify("Hello World")


if __name__ == '__main__':
    app.run()
