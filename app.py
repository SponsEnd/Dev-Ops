from flask import Flask
import requests
from flask import request

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/sendRequest")
def send_request():
    transcript = request.args.get("id")
    print(transcript)
    requests.get("http://192.168.176.121:5000/sponsor?id={transcript}")
    return "<p>Hello, World!</p>"