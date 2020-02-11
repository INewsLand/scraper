from flask import Flask, request, jsonify
from api.spiders import get_deamon
from api.spiders import get_projects
from api.spiders import get_spiders

app = Flask(__name__)

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

if __name__ == "__main__":
    app.run('0.0.0.0', 5000, debug=True)
