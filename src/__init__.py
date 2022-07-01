import os

from flask import Flask, render_template, redirect, url_for
from src.database import db, User
from src.account import account
from src.auth import auth
from flask_login import LoginManager
from src.helpers import create_sample_data


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        app.config.from_mapping(
            SECRET_KEY="jhdskhsduiuy8fsdf98sd",
            SQLALCHEMY_DATABASE_URI='postgresql://ybtkjilpmhzqji:8051c5d34ec89e45f892548d1375d8a26616875a1b8773542a481abaa2dbddab@ec2-3-222-74-92.compute-1.amazonaws.com:5432/d4i3l5tk1f5bvl',
            SQLALCHEMY_TRACK_MODIFICATIONS=False,
        )
    else:
        app.config.from_mapping(test_config)

    # Initialize the database
    db.app = app
    db.init_app(app)

    app.register_blueprint(account)
    app.register_blueprint(auth)

    # Flask login config
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    # Route to create random data for the transactions and wallets
    # This has not been optimized to check on the wallet balance and risks having negative balance
    # @app.route('/generate_random_data')
    # def generate_data():
    #     return create_sample_data()
    #
    # @app.route('/create_all')
    # def generate_data():
    #     return db.create_all()

    return app

