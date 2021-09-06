import os

from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

CORS(app)


def run_server():
    """
    Runs Flask initial server instance on port and host specified in config.py
    Needs config to be inited
    """
    app.run(host=os.environ['SERVER_HOST'],
            port=int(os.environ['SERVER_PORT']))
