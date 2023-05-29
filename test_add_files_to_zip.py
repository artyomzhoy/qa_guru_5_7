import os
import zipfile

from os_path.os_path_scripts import PROJECT_ROOT_PATH


def test_add_files_to_zip():
    zip_path = os.path.join(PROJECT_ROOT_PATH, '..', 'resources')
    zip_name = "test.zip"
    with zipfile.ZipFile(zip_name, "w") as zip_file:
        for file_name in os.listdir(zip_path):
            file_path = os.path.join(zip_path, file_name)
            zip_file.write(file_path, file_name)

    with zipfile.ZipFile(zip_name, "r") as zip_file:
        for file_name in os.listdir(zip_path):
            assert file_name in zip_file.namelist()
