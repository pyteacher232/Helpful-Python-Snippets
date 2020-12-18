import zipfile

full_zip_fname = "My_ZIP.zip"
working_dir = "Output"
with zipfile.ZipFile(full_zip_fname, 'r') as zip_ref:
    names_inside_zip = zip_ref.namelist()
    zip_ref.extractall(working_dir)