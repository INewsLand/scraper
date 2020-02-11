PROJECT = 'news'
URL = 'http://localhost:6800/'

def make_url(link):
    link = link.replace('project=', f'project={PROJECT}')
    return f'{URL}{link}'
