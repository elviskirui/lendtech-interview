import os
os.environ['DATABASE_URL'] = 'sqlite:///'  # use an in-memory database for tests

import unittest
from flask import current_app
from src import create_app, db


class TestWebApp(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.appctx = self.app.app_context()
        self.appctx.push()
        db.create_all()
        self.client = self.app.test_client()

    def tearDown(self):
        db.drop_all()
        self.appctx.pop()
        self.app = None
        self.appctx = None
        self.client = None

    def test_app(self):
        assert self.app is not None
        assert current_app == self.app

    def test_home_page_redirect(self):
        response = self.client.get('/auth/login', follow_redirects=True)
        assert response.status_code == 200
        assert response.request.path == '/auth/login'

    def test_request_example(self):
        response = self.client.get("auth/login")
        assert b"Log In" in response.data
        assert response.status_code == 200

    # Test redirects to login on loading the homepage
    # @pytest.mark.usefixtures('client_class')
    def test_loading_dashboard_redirects_to_login(self):
        response = self.client.get("payments")
        assert response.status_code == 401

    # Test login form submission
    # Test registration submission
    # Test registration page available for guests visisting the platform
    def test_registration_page_available_to_guests(self):
        response = self.client.get("/auth/register")
        assert b"Register" in response.data
        assert b"First name" in response.data
        assert b"Register" in response.data
        assert response.status_code == 200
    # Test registration validation
    #  - phone
    #  - email
    #  - password
    #  - password matching
    #  -first name
    #  - last name

    # Test registration success
    # Test account creation results in wallet creation too
    # Test login redirects to homepage
    # Test can query transactions/payments
    # Test payments page available for a logged in user
    # Test search functionality returns results
    # Test homepage/dashboard available for logged in user
    # Test wallet balance available for user
    # Test transactions available for user logged in