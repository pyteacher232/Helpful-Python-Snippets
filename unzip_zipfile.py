import zipfile

with zipfile.ZipFile(full_zip_fname, 'r') as zip_ref:
    zip_ref.extractall(self.working_dir)