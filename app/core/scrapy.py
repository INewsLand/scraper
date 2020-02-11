import requests
from config.const import make_url
from config.const import scheduler_payload
from config.const import cancel_payload

def get_deamon():
    call = requests.get(make_url('daemonstatus.json'))
    return call.status_code, call.json()

def get_projects():
    call = requests.get(make_url('listprojects.json'))
    return call.status_code, call.json()

def get_spiders():
    call = requests.get(make_url('listspiders.json?project='))
    return call.status_code, call.json()

def get_jobs():
    call = requests.get(make_url('listjobs.json?project='))
    return call.status_code, call.json()

def set_scheduler(spider, link):
    call = requests.post(make_url('schedule.json'), scheduler_payload(spider, link))
    return call.status_code, call.json()

def set_cancel(job):
    call = requests.post(make_url('cancel.json'), cancel_payload(job))
    return call.status_code, call.json()
