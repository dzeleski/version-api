"""
Init for api application. Everything starts from here.
"""
from flask import Flask, jsonify, logging, request, Response
from flask_cors import CORS, cross_origin
from version_api.routes import app_start, get_version, set_versions, list_versions
from version_api.routes import create_application, list_applications, health
from version_api.database import postgres


app = Flask(__name__, static_url_path='/static')
CORS(app)

app.register_blueprint(app_start.mod)
app.register_blueprint(postgres.mod)
app.register_blueprint(get_version.mod)
app.register_blueprint(set_versions.mod)
app.register_blueprint(list_versions.mod)
app.register_blueprint(create_application.mod)
app.register_blueprint(list_applications.mod)
app.register_blueprint(health.mod)
