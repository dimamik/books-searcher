import json

from api.server import app


@app.errorhandler(404)
def error_handler(_):
    return json.dumps("No such Page, please read api docs")
