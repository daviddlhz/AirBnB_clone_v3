#!/usr/bin/python3
"""
Flask web application api
"""
from flask import Blueprint
from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views
import os

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_blueprint(app_views, url_prefix='/api/v1')


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()


@app.errorhandler(404)
def page_not_found(e):
        """set the 404 status"""
        return jsonify({"error": "Not found"}), 404


if __name__ == '__main__':
    my_host = os.getenv('HBNB_API_HOST')
    my_port = os.getenv('HBNB_API_PORT')
    app.run(host=my_host, port=my_port, threaded=True)
