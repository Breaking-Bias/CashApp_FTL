from use_case.upload_file.upload_file_interactor import UploadFileInteractor
from flask import Flask, jsonify, request

class UploadFileController:
    # files
    upload_file_interactor: UploadFileInteractor
    filename: str | None

    def __init__(self):
        self.files = None
        self.upload_file_interactor = UploadFileInteractor()
        self.filename = None

    def execute(self):
        self.files = request.files
        result = self.upload_file_interactor.upload_dataset(self.files)
        self.filename = self.upload_file_interactor.name_of_file
        print(self.filename)
        return jsonify(result[0]), result[1]

    def get_datasets_from_interactor(self):
        result = self.upload_file_interactor.get_datasets_from_data_access()
        return jsonify(result[0]), result[1]
