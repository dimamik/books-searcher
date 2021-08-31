from flask import Flask
from flask_cors import CORS
import os

# TODO Change port (and path if needed)
# TODO Handle CORS Policy!
app = Flask(__name__)
CORS(app)


def run_server():
    app.run()


if __name__ == '__main__':
    app.run(host=os.environ['SERVER_HOST'],
            port=int(os.environ['SERVER_PORT']))
