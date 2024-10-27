from flask import Flask, jsonify, request
from flask_cors import CORS
from data.arima_test import create_sample_data
from data.read_data import create_formatted_data

app = Flask('server')
CORS(app)

# Example of an endpoint that returns test data
@app.route('/getinfo')
def getinfo():
    info = {"name":'breaking bias', "score":"awesome"}
    return jsonify(info)

@app.route('/getOriginalData')
def getOriginalData():
    data = create_formatted_data()
    return jsonify(data)

@app.route('/predictValues', methods=['POST'])
def predictValues():
    data = request.get_json()
    num_points = data['numPoints']

    # Replace with actual predict function
    # new_values = predict(num_points)
    new_values = {}

    return jsonify(new_values)

@app.route('/getDummyData')
def getDummyData():
    data = create_sample_data().to_json()
    return data

# This is to test that CI/CD pipeline is working. Delete later.
def cicd_test():
    print("CI/CD is cooking")
    return None


if __name__ == '__main__':
    app.run()
