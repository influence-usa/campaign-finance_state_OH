import glob
import os
import zipfile

zip_files = glob.glob('/home/aaron/pycon/ohio_down/*.EXE')

for zip_filename in zip_files:
    dir_name = "/home/aaron/pycon/ohio_down/unzipped_exe"
    zip_handler = zipfile.ZipFile(zip_filename, "r")
    zip_handler.extractall(dir_name)
