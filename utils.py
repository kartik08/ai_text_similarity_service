import os

def make_dir(dir_path):
    try:
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
        return dir_path
    except Exception:
        raise "Error while creating Folder"

