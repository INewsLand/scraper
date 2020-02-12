from flask import Flask, request, jsonify
from api.scrapy import scrapy_router

app = Flask(__name__)

scrapy_router(app)

if __name__ == "__main__":
    app.run('0.0.0.0', 5000, debug=True)
