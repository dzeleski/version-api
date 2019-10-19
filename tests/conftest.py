import pytest
import version_api


@pytest.fixture(scope='module')
def test_client():

    flask_app = version_api.app

    testing_client = flask_app.test_client()

    ctx = flask_app.app_context()
    ctx.push()

    yield testing_client

    ctx.pop()
