import pytest
import os
from src import create_app
from src.database import db

@pytest.fixture()
def app():
    app = create_app()
    app.config.update({
        'SECRET_KEY': os.environ.get("TEST_SECRET_KEY"),
        'SQLALCHEMY_DATABASE_URI': os.environ.get("TEST_SQLALCHEMY_DB_URI"),
        'SQLALCHEMY_TRACK_MODIFICATIONS': False,
    })

    # other setup can go here

    yield app

    # clean up / reset resources here


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()
