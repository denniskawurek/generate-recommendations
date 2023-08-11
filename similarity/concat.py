

from similarity.common import files, writer
from similarity.common.reader import json_load

def concat(filepaths, out_dir):
    concat_data = process(filepaths)
    out = files.get_path(out_dir, "concat.json")
    writer.dump_json(out , concat_data)
    return out

def process(filepaths):
    concatenated_data = []
    
    for filepath in filepaths:
        data = json_load(filepath)
        concatenated_data.extend(data)
    return concatenated_data