import os

from flask import Flask, render_template, redirect, url_for
from src.database import db
from src.account import account


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        app.config.from_mapping(
            SECRET_KEY=os.environ.get("SECRET_KEY"),
            SQLALCHEMY_DATABASE_URI=os.environ.get("SQLALCHEMY_DB_URI"),
            SQLALCHEMY_TRACK_MODIFICATIONS=False,
        )
    else:
        app.config.from_mapping(test_config)

    # Initialize the database
    db.app = app
    db.init_app(app)

    app.register_blueprint(account)

    @app.route('/')
    def index():
        return redirect(url_for('account.dashboard'))



    return app
