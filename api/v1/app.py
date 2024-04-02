#!/usr/bin/python3
"""Status of your API"""

from models import storage
from api.v1.views import app_views
from flask import Flask, jsonify
from os import getenv


app = Flask(__name__)
app.url_map.strict_slashes = False
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown(self):
    """close storage engine"""
    return storage.close()


@app.errorhandler(404)
def ErrNotFound(err):
    """returns a JSON-formatted 404 status code response"""
    return jsonify('"error": "Not found"'), 404


if __name__ == "__main__":
    host = getenv('HBNB_API_HOST')
    port = getenv('HBNB_API_PORT')
    if not host:
        host = '0.0.0.0'
    if not port:
        port = '5000'
    app.run(
        host=host,
        port=port,
        threaded=True
    )
