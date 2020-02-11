from flask import Flask, request, jsonify
from api.scrapy import set_all

app = Flask(__name__)

set_all(app)

if __name__ == "__main__":
    app.run('0.0.0.0', 5000, debug=True)
