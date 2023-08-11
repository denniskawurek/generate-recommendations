
from similarity.common import files, reader, writer
import numpy as np
import spacy
import tensorflow_hub as hub
from spacy.language import Language

SIMILARITIES_PROPERTY = "___similarities"
NLP_PROPERTY = "___nlp"
encoder = None

def embed(content_property, file, out_dir):
    data = reader.json_load(file)
    embedded = process(content_property, data)
    out = files.get_path(out_dir, "embedded.json")
    writer.dump_json(out, embedded)
    return out

def get_encoder():
    global encoder
    if encoder is None:
        encoder = hub.load("https://tfhub.dev/google/universal-sentence-encoder/4")
    return encoder

@Language.component("universal_sentence_encoder")
def universal_sentence_encoder_component(doc):
    encoder = get_encoder()
    doc.user_data["embedding"] = encoder([doc.text])[0]
    return doc


def process(content_property, posts):
    nlp = spacy.load("en_core_web_lg")
    nlp.add_pipe('universal_sentence_encoder')

    num_posts = len(posts)
    processed_posts = [
        {
            **post, 
            NLP_PROPERTY: nlp(post[content_property]),
            SIMILARITIES_PROPERTY: np.zeros(num_posts).tolist()
        }
        for post
        in posts
    ]

    for i in range(num_posts):
        for j in range(i, num_posts):
            similarity_score = processed_posts[i][NLP_PROPERTY].similarity(processed_posts[j][NLP_PROPERTY])

            processed_posts[i][SIMILARITIES_PROPERTY][j] = similarity_score
            processed_posts[j][SIMILARITIES_PROPERTY][i] = similarity_score
        
        del processed_posts[i][NLP_PROPERTY]
        
    return processed_posts