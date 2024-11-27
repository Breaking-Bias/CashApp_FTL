from use_case.upload_file.upload_file_interactor import UploadFileInteractor
from flask import jsonify, request


class UploadFileController:
    """Controller for the upload file use case."""
    upload_file_interactor: UploadFileInteractor
    filename: str | None

    def __init__(self):
        self.files = None
        self.upload_file_interactor = UploadFileInteractor()
        self.filename = None

    def execute(self):
        """Executes the upload file use case via upload_file_interactor"""
        self.files = request.files
        result = self.upload_file_interactor.upload_dataset(self.files)
        self.filename = result.name_of_file
        return jsonify(result[0]), result[1]

    def get_datasets_from_interactor(self):
        result = self.upload_file_interactor.get_datasets_from_data_access()
        return jsonify(result[0]), result[1]
