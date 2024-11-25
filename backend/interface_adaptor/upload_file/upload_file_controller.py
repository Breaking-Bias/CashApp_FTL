from use_case.upload_file.upload_file_interactor import UploadFileInteractor

class UploadFileController:
    # files, not putting type annotation here, otherwise the import statement would violate Dependency Inversion Rule
    upload_file_interactor: UploadFileInteractor
    filename: str | None

    def __init__(self, files):
        self.files = files
        self.upload_file_interactor = UploadFileInteractor()
        self.filename = None

    def execute(self):
        result = self.upload_file_interactor.upload_dataset(self.files)
        self.filename = result.name_of_file
        return result

    def get_datasets_from_interactor(self):
        return self.upload_file_interactor.get_datasets_from_data_access()
