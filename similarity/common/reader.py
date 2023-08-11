import json

def load(filepath):
    with open(filepath, 'r') as file:
        return file.read()

def json_load(filepath):
    with open(filepath, 'r') as file:
        return json.load(file)