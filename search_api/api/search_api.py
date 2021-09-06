from api.server import app
from search.search_engine import search, search_as_you_type


@app.route('/search/<query>')
def route_search(query):
    """
    Should be used to get search results
    Includes more information about books (f.e. description)
    Example request is /search/Harry Potter
    """
    return search(query)


@app.route('/saut/<query>')
def route_search_as_you_type(query):
    """
    Should be used to get search hints
    """
    return search_as_you_type(query)
