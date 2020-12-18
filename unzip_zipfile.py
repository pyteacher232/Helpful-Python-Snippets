import zipfile

full_zip_fname = "My_ZIP.zip"
working_dir = "Output"
with zipfile.ZipFile(full_zip_fname, 'r') as zip_ref:
    zip_ref.extractall(working_dir)