import json

def dump_json(path, data):
    with open(path, 'w') as file:
        json.dump(data, file)

def dump(path, data):
    with open(path, 'w') as file:
        file.write(data)