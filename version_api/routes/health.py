"""
Module: Health
Used for monitoring if the application is up and working ok
"""
from flask import Blueprint, Response

mod = Blueprint('health', __name__)


@mod.route('/health', methods=['GET'])
def health():
    """
    returns json status msg and 200
    :return:
    """
    return Response('{"Status": "OK"}', status=200, mimetype='application/json')
