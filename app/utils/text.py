import unicodedata

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
