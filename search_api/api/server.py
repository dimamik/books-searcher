import os

from flask import Flask
from flask_cors import CORS

from config import init_config, init_logging

init_logging()
init_config()
app = Flask(__name__)

CORS(app)


def run_server():
    app.run(host=os.environ['SERVER_HOST'],
            port=int(os.environ['SERVER_PORT']))
