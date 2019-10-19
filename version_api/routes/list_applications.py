"""
Module: list_applications
Used to list applications
"""
from flask import Blueprint, Response

mod = Blueprint('list_applications', __name__)


@mod.route('/list_applications', methods=['GET'])
def list_applications():
    """
    list_applications
    :return:
    """
    return Response('{"Status": "OK"}', status=200, mimetype='application/json')
