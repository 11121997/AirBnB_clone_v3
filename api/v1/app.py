#!/usr/bin/python3
"""Status of your API"""

from storage import models
from api.v1.views import app_views
from flask import Flask, jsonify
from flask_cors import CORS
from os import getenv


app = Flask(__name__)
app.url_map.strict_slashes = False
app.register_blueprint(app_views)
CORS(app, resources={r"/api/*": {"origins": "0.0.0.0"}})


@app.teardown_appcontext
def teardown(self):
    """close storage engine"""
    return storage.close()


if __name__ == "__main__":
    host = getenv("HBNB_API_HOST") if getenv("HBNB_API_HOST") else "0.0.0.0"
    port = os.getenv("HBNB_API_PORT") if os.getenv("HBNB_API_PORT") else 5000
    app.run(
        host=host,
        port=port,
        threaded=True
    )
