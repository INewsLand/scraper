import unicodedata
import re

def remove_blank_lines(text):
    text = text.replace('\n', '')
    text = text.replace('\r', '')
    return text

def unidecode_data(text):
    return unicodedata.normalize('NFKD', text)

def normalize_titles(text):
    text = remove_blank_lines(text)
    text = unidecode_data(text)
    return text

def no_tags(text):
    aux = re.sub(r'<\b[^>]*>?'," ", text)
    aux = re.sub(r'</[a-zA-Z]+>'," ", aux)
    return aux