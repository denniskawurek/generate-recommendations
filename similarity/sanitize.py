from bs4 import BeautifulSoup
import re

from similarity.common import files, reader, writer

'''
Sanitizes the files in a way that they're further processable.
This means: No HTML, no code, ...
'''
def sanitize_files(paths, out_dir):
    sanitized_filepaths = []
    for filepath in paths:
        sanitized = process(filepath)
        
        filename = files.get_filename(filepath)
        out = files.get_path(out_dir, "sanitized-" + filename)
        
        writer.dump(out, sanitized)

        sanitized_filepaths.append(out)

    return sanitized_filepaths

def remove_html_tags(text):
    soup = BeautifulSoup(text, 'html.parser')
    clean_text = soup.get_text(separator='\n')
    return clean_text

def process(filepath):
    text = reader.load(filepath)

    sanitized_content = re.sub(r'```.*?```', '', text, flags=re.DOTALL)
    sanitized_content = re.sub(r'\#', '', sanitized_content, flags=re.DOTALL)
    sanitized_content = re.sub(r'\*', '', sanitized_content, flags=re.DOTALL)

    return sanitized_content

def remove_invalid_double_quotes(json_text):
    sanitized_text = json_text
    in_string = False
    escape_next = False

    for i in range(len(json_text)):
        if json_text[i] == '"' and not escape_next:
            in_string = not in_string
        elif json_text[i] == '\\' and in_string:
            escape_next = not escape_next
        elif json_text[i] == '"' and escape_next:
            sanitized_text = sanitized_text[:i] + sanitized_text[i+1:]

        escape_next = False

    return sanitized_text