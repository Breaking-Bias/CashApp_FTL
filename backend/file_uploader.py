import os
from werkzeug.utils import secure_filename


class FileUploader:
    def __init__(self, upload_folder='data', allowed_extensions=None):
        self.upload_folder = upload_folder
        self.allowed_extensions = allowed_extensions
        self.nameoffile=None

        # Ensure the upload folder exists
        if not os.path.exists(self.upload_folder):
            os.makedirs(self.upload_folder)

    def allowed_file(self, filename):
        """Check if the file has an allowed extension."""
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in self.allowed_extensions

    def save_file(self, file):
        """Save the file if it meets the allowed extension criteria."""
        if file and self.allowed_file(file.filename): #"test_upload.csv"
            filename = secure_filename(file.filename)
            file_path = os.path.join(self.upload_folder, filename)
            file.save(file_path)
            self.nameoffile=filename
            return file_path
        return None
    def list_datasets(self):
        """Return a list of filenames in the upload folder."""
        try:
            # List all files in the upload folder
            datasets = [
                f for f in os.listdir(self.upload_folder)
                if os.path.isfile(os.path.join(self.upload_folder, f))
            ]
            return datasets
        except Exception as e:
            raise Exception(f"Error listing datasets: {str(e)}")
