"""
Module: get_version
Used to get the correct application version based on stage
"""
from flask import Blueprint, Response

mod = Blueprint('get_version', __name__)


@mod.route('/get_version', methods=['GET'])
def get_version():
    """
    get_version
    :return:
    """
    return Response('{"Status": "OK"}', status=200, mimetype='application/json')
