"""
Module: app_start
Used to setup the DB schema before first request
"""
from flask import Blueprint
from version_api.database import postgres

mod = Blueprint('app_start', __name__)


@mod.before_app_first_request
def init_database():
    """
    Inits the database
    :return:
    """
    postgres.Applications.createTable(ifNotExists=True)
    postgres.Stages.createTable(ifNotExists=True)
