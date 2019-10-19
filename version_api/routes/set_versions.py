"""
Module: set_versions
Used to set the versions in stages for an application
"""
from flask import Blueprint, Response

mod = Blueprint('set_versions', __name__)


@mod.route('/set_versions', methods=['GET'])
def set_versions():
    """
    set_versions
    :return:
    """
    return Response('{"Status": "OK"}', status=200, mimetype='application/json')
