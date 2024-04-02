#!/usr/bin/python3
"""index module"""


from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status')
def status():
    """status of the API"""
    return jsonify(status='OK')
