import os

def get_filename(path):
    return os.path.basename(path)

def get_path(dir, filename):
    return os.path.join(dir, filename)