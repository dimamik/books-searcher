from flask import Flask
from services.search_worker import search,search_as_you_type
app = Flask(__name__)


@app.route('/search/<query>')
def example(query):
    return search(query)

# Search as you type engine
@app.route('/saut/<query>')
def example(query):
    return search_as_you_type(query)


if __name__ == '__main__':
    app.run()
