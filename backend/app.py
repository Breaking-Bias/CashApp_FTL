from flask import Flask, jsonify, request
from flask_cors import CORS
import read_data
import os 
from werkzeug.utils import secure_filename 
from file_uploader import FileUploader
# import logging

# logging.basicConfig(level=logging.DEBUG)

app = Flask('app')
CORS(app)

# Example of an endpoint that returns test data
@app.route('/getinfo')
def getinfo():
    info = {"name":'breaking bias', "score":"awesome"}
    return jsonify(info)


@app.route('/getPastData', methods=['POST'])
def getPastData():
    filtering_factor = request.get_json()['filtering_factor']
    data = read_data.create_formatted_data(filtering_factor, True)
    return jsonify(data)


@app.route('/predictData', methods=['POST'])
def predictValues():
    filtering_factor = request.get_json()['filtering_factor']
    forecast_steps = request.get_json()['num_points']
    new_values = read_data.create_prediction_data(filtering_factor, forecast_steps, True)
    return jsonify(new_values)


@app.route('/getPastDataUnbiased', methods=['POST'])
def getPastDataUnbiased():
    filtering_factor = request.get_json()['filtering_factor']
    data = read_data.create_formatted_data(filtering_factor, False)
    return jsonify(data)


@app.route('/predictDataUnbiased', methods=['POST'])
def predictValuesUnbiased():
    filtering_factor = request.get_json()['filtering_factor']
    forecast_steps = request.get_json()['num_points']
    new_values = read_data.create_prediction_data(filtering_factor, forecast_steps, False)
    return jsonify(new_values)

#This is where it startsONS

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

    # Use FileUploader to save the file
    file_path = file_uploader.save_file(file)
    if file_path:
        return jsonify({"message": "File uploaded successfully", "file_path": file_path}), 200
    else:
        return jsonify({"message": "Invalid file format. Only CSV and XLSX are allowed."}), 400


    # try:

    #     df = pd.read_csv(file)
        
    #     data_head = df.head().to_dict(orient='records')
        
    #     return jsonify({
    #         "message": "File uploaded successfully!",
    #         "data_head": data_head
    #     })
    # except Exception as e:
    #     return jsonify({"message": f"Error processing file: {str(e)}"}), 400

 

#this is where it ends

# This is to test that CI/CD pipeline is working. Delete later.
@app.route('/cicd_test')
def cicd_test():
    return jsonify("Hello World")


if __name__ == '__main__':
    app.run()
