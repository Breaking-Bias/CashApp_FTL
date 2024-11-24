from flask import Flask, jsonify, request
from data_access.data_access_helper.data_reader import DataReader
from data_access.data_access_helper.file_uploader import FileUploader


class UploadFileInteractor:
    app: Flask
    name_of_file: str | None

    def __init__(self, app: Flask):
        """app should be mutated by CORS() before calling this method."""
        self.app = app
        self.name_of_file = None

    def upload_dataset(self):
        """Endpoint to handle file upload."""
        # print('firstfile:', self.name_of_file)
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
            self.app.read_dataset = DataReader(self.name_of_file).read_dataset()
            print(self.name_of_file)
            return jsonify({"message": "File uploaded successfully", "file_path": file_path}), 200
        else:
            return jsonify({"message": "Invalid file format. Only CSV and XLSX are allowed."}), 400

    @staticmethod
    def get_datasets():
        file_uploader = FileUploader(upload_folder='data', allowed_extensions={'csv', 'xlsx', 'pq'})
        try:
            datasets = file_uploader.list_datasets()
            return jsonify({"datasets": datasets}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
