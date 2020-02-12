PROJECT = 'news'
URL = 'http://localhost:6800/'

def make_url(link):
    link = link.replace('project=', f'project={PROJECT}')
    return f'{URL}{link}'

def scheduler_payload(spider, link=None):
    payload = {
        'project': PROJECT,
        'spider': spider
    }
    if link:
        payload['link'] = link
    return payload

def cancel_payload(spider, link):
    payload = {
        'project': PROJECT,
        'job': job
    }
    return payload
