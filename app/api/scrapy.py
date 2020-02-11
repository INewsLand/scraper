from flask import request, jsonify

from core.scrapy import get_deamon
from core.scrapy import get_projects
from core.scrapy import get_spiders
from core.scrapy import get_jobs
from core.scrapy import set_scheduler
from core.scrapy import set_cancel

def set_all(app):

    @app.route('/deamon', methods=['GET'])
    def deamon():
        status, payload = get_deamon()
        return {
            'status': status,
            'payload': payload
        }

    @app.route('/projects', methods=['GET'])
    def projects():
        status, payload = get_projects()
        return {
            'status': status,
            'payload': payload
        }

    @app.route('/spiders', methods=['GET'])
    def spiders():
        status, payload = get_spiders()
        return {
            'status': status,
            'payload': payload
        }

    @app.route('/schedule', methods=['POST'])
    def schedule():
        json = request.get_json()
        spider = json.get('spider', '')
        link = json.get('link', '')
        status, payload = set_scheduler(spider, link)
        return {
            'status': status,
            'payload': payload
        }
