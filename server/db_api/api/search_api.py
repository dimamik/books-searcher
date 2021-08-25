from api.server import app
from search.main_search_engine import search, search_as_you_type


# Example request is /search/Harry Potter is query
@app.route('/search/<query>')
def route_search_as_you_type(query):
    return search(query)


# Search as you type engine
@app.route('/saut/<query>')
def route_search(query):
    return search_as_you_type(query)
