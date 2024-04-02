#!/usr/bin/python3
"""Status of your API"""

from storage import models
from app_views import api.v1.views
from flask import Flask, jsonify
from flask_cors import CORS
import os


app = Flask(__name__)
app.url_map.strict_slashes = False
app.register_blueprint(app_views)
CORS(app, resources={'/*': {'origins': app_host}})


@app.teardown_appcontext
def teardown(self):
    """close storage engine"""
    return storage.close()


if __name__ == "__main__":
    host = os.getenv("HBNB_API_HOST") if os.getenv("HBNB_API_HOST") /
    else "0.0.0.0"
    port = os.getenv("HBNB_API_PORT") if os.getenv("HBNB_API_PORT") else 5000
    app.run(
        host=host,
        port=port,
        threaded=True
    )
