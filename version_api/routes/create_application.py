"""
Module: create_application
Used to create a new application
"""
from flask import Blueprint, Response

mod = Blueprint('create_application', __name__)


@mod.route('/create_application', methods=['GET'])
def create_application():
    """
    create_application
    :return:
    """
    return Response('{"Status": "OK"}', status=200, mimetype='application/json')
