import nltk
from nltk.corpus import stopwords

from similarity.common import files, writer
from similarity.common import reader
nltk.download('stopwords')

removable_words = [
        "also"
]

stopwords_list = stopwords.words('english')

'''
Removes stop words and pre-defined fill words of the content.
'''
def clean(content_property, paths, out_dir, extra_words=[]):
    removable_words.append(extra_words)

    cleaned_files = []
    for filepath in paths:
        cleaned = process(content_property, filepath)
        
        filename = files.get_filename(filepath)
        out = files.get_path(out_dir, "cleaned-" + filename)
        writer.dump_json(out, cleaned)

        cleaned_files.append(out)

    return cleaned_files

def process(content_property, filepath):
    data = reader.json_load(filepath)

    for post in data:
        words = post["content"].split()
        words = [word for word in words if word.lower() not in stopwords_list and word.lower() not in removable_words]
        words = " ".join(words)
        post[content_property] = words
    return data