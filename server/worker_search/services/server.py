from services.search_worker.main_search_engine import search_as_you_type, search
from flask import Flask
from flask import request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
# Example request is /search?q=This is query


@app.route('/search/<query>')
def route_search_as_you_type(query):
    return search(query)


# Search as you type engine
@app.route('/saut/<query>')
def route_search(query):
    return search_as_you_type(query)


def run_server():
    app.run()


if __name__ == '__main__':
    app.run()
