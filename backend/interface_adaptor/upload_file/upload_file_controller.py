from use_case.upload_file.upload_file_interactor import UploadFileInteractor

class UploadFileController:
    upload_file_interactor: UploadFileInteractor

    def __init__(self, upload_file_interactor: UploadFileInteractor):
        self.upload_file_interactor = upload_file_interactor

    def execute(self):
        self.upload_file_interactor.upload_dataset()
