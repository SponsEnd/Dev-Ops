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
    requests.get("http://sponsend1.pagekite.me/sponsor?id={transcript}")
    return "<p>Hello, World!</p>"