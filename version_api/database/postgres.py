"""
Module: Postgres
Configures SQL ORM
"""
import os
from flask import Blueprint
from sqlobject import connectionForURI, sqlhub, SQLObject, StringCol, ForeignKey, MultipleJoin

if os.environ['FLASK_ENV'] == "development":
    pg_pass = os.environ['pg_pass']
    sql = f'postgres://zfqvonjx:{pg_pass}@salt.db.elephantsql.com:5432/zfqvonjx'
    # sql = 'postgres://flask:flask@localhost:5433/version_api'
else:
    # Prod here
    sql = ''

conn = connectionForURI(sql)
sqlhub.processConnection = conn

mod = Blueprint('postgres', __name__)


class Stages(SQLObject):
    """
    Stages Table
    Used for tracking application versions in each stage
    """
    canary = StringCol(length=64)
    sn2 = StringCol(length=64)
    sn1 = StringCol(length=64)
    s0 = StringCol(length=64)
    s1 = StringCol(length=64)
    s2 = StringCol(length=64)
    s3 = StringCol(length=64)
    s4 = StringCol(length=64)
    nostage = StringCol(length=64)
    applications = ForeignKey('Applications')


class Applications(SQLObject):
    """
    Applications Table
    Used for tracking applications, these names must be unique
    """
    app_name = StringCol(length=64, unique=True)
    stages = MultipleJoin('Stages')
