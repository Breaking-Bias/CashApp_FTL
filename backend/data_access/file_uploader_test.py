import os
import pytest
from werkzeug.datastructures import FileStorage
from io import BytesIO

# Adjust this import as needed
from data_access.file_uploader import FileUploader


@pytest.fixture
def file_uploader():
    upload_folder = 'test_data'
    allowed_extensions = {'txt', 'csv'}
    uploader = FileUploader(upload_folder=upload_folder,
                            allowed_extensions=allowed_extensions)
    yield uploader
    # Clean up: remove all files and delete test upload folder
    for f in os.listdir(upload_folder):
        os.remove(os.path.join(upload_folder, f))
    os.rmdir(upload_folder)


def test_allowed_file(file_uploader):
    # Test allowed extension
    assert file_uploader.allowed_file("data.csv") is True
    assert file_uploader.allowed_file("image.png") is False
    assert file_uploader.allowed_file("notes.txt") is True
    assert file_uploader.allowed_file("report.pdf") is False


def test_save_file(file_uploader):
    # Test saving a file with allowed extension
    file = FileStorage(
        stream=BytesIO(b"Test file content"),
        filename="test_file.csv",
        content_type="text/csv"
    )
    file_path = file_uploader.save_file(file)
    assert file_path is not None
    assert os.path.exists(file_path)

    # Test saving a file with disallowed extension
    disallowed_file = FileStorage(
        stream=BytesIO(b"Disallowed file content"),
        filename="test_file.pdf",
        content_type="application/pdf"
    )
    file_path = file_uploader.save_file(disallowed_file)
    assert file_path is None


def test_list_datasets(file_uploader):
    # Create dummy files in the upload folder
    filenames = ["file1.csv", "file2.txt"]
    for filename in filenames:
        with open(os.path.join(file_uploader.upload_folder,
                               filename), 'w') as f:
            f.write("dummy content")

    datasets = file_uploader.list_datasets()
    assert set(datasets) == set(filenames)
