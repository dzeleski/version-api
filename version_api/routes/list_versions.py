"""
Module: list_versions
Used to list the correct application version based on stage
"""
from flask import Blueprint, Response

mod = Blueprint('list_versions', __name__)


@mod.route('/list_versions', methods=['GET'])
def list_version():
    """
    list_versions
    :return:
    """
    return Response('{"Status": "OK"}', status=200, mimetype='application/json')
