
import numpy as np
from similarity.common import files, reader, writer

SIMILARITIES_PROPERTY = "___similarities"


def get_top_similarities(file, num_scores, identifier_key, out_dir):
    data = reader.json_load(file)
    top_similarities = {}
    for i in range(0,len(data)):
        scores = data[i][SIMILARITIES_PROPERTY]
        top_indices = np.argsort(scores)[::-1][:num_scores+1]
        top_indices_without_current_doc = np.delete(top_indices, np.where(top_indices == i))

        similarities = []
        for index in top_indices_without_current_doc:
             similarities.append(data[index])

        top_similarities[data[i][identifier_key]] = similarities
    
    
    out = files.get_path(out_dir, "top_"+ str(num_scores) +".json")
    writer.dump_json(out, top_similarities)
    
    return out