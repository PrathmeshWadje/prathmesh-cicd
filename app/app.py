# Simple Flask Application

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World!"

if __name__ == '__main__':
    # Listen on all interfaces and the port 80
    app.run(debug=True, port=8080,  host='0.0.0.0')
