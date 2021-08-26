from flask import Flask
from flask_cors import CORS

# TODO Change port (and path if needed)
# TODO Handle CORS Policy!

app = Flask(__name__)

CORS(app)


def run_server():
    app.run(port=5001)
