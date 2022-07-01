from flask import Flask,url_for
import pytest
import os

# Test availability of register
# def test_register(client):
#     response = client.post("/auth/login", data={
#         "first_name": "elvis",
#         "second_name": "dark",
#         "phone": "dark",
#         "email": "dark",
#         "password1":"testpassword123",
#         "password2": "testpassword123",
#     })
#     assert response.status_code == 200

# Test login available
def test_request_example(client):
    response = client.get("auth/login")
    assert b"Log In" in response.data
    assert response.status_code == 200


# Test redirects to login on loading the homepage
# @pytest.mark.usefixtures('client_class')
def test_loading_dashboard_redirects_to_login(client):
    response = client.get("/payments")
    assert response.status_code == 401
# Test login form submission
# Test registration submission
# Test registration page available for guests visisting the platform
def test_registration_page_available_to_guests(client):
    response = client.get("/auth/register")
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
