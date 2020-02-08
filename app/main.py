from flask import Flask, request, escape

app = Flask(__name__)

@app.route('/run')
def run():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
