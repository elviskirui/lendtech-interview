from flask import Blueprint, request, render_template, flash, redirect, url_for
from src.database import User, db, Wallet
from werkzeug.security import check_password_hash, generate_password_hash
from  flask_login import login_user, logout_user, login_required
import validators

auth = Blueprint('auth', __name__, url_prefix='/auth')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    # check if the request is post of get to process the login or render the login form
    if request.method == 'POST':
        phone = request.form.get('phone', '')
        password = request.form.get('password', '')

        user = User.query.filter_by(phone=phone).first()
        if user:
            if check_password_hash(user.password, password):
                # flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('account.dashboard'))
            else:
                flash('Invalid credentials, try again.', category='error')
        else:
            flash('Invalid credentials.', category='error')

    return render_template('auth/login.html')


@auth.route('/register', methods=['GET', 'POST'])
def register():
    # check if the request is post of get to process the registration or show the login form
    if request.method == 'POST':
        email = request.form.get('email', '')
        phone = request.form.get('phone', '')
        first_name = request.form.get('first_name', '')
        last_name = request.form.get('last_name', '')
        password1 = request.form.get('password1', '')
        password2 = request.form.get('password2', '')

        # Handle validations
        if len(first_name) < 3:
            flash('First name must have at least than 3 characters.', category='error')

        elif len(last_name) < 3:
            flash('First name must have at least than 3 characters.', category='error')

        elif len(phone) != 12:
            flash('Invalid phone number. Use the format 25471234568.', category='error')

        elif not validators.email(email):
            flash('Please provide a valid email.', category='error')

        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')

        elif len(password1) < 1:
            flash('Password must be at least 7 characters.', category='error')

        elif User.query.filter_by(email=email).first():
            flash('Email already exists.', category='error')

        elif User.query.filter_by(phone=phone).first():
            flash('Phone already exists.', category='error')

        else:
            # Register the user
            user = User(first_name=first_name, last_name=last_name, email=email, phone=phone, password=generate_password_hash(password1))
            db.session.add(user)
            db.session.commit()

            # Create the users wallet
            wallet = Wallet(user_id=user.id, amount=0)
            db.session.add(wallet)
            db.session.commit()

            flash('Registration successful.Please login to continue!', category='success')
            return redirect(url_for('auth.login'))
    return render_template('auth/register.html')


@auth.get('/logout')
@login_required
def logout():
    # Logout the user
    logout_user()
    flash("Your have successfully logged out", category='success')
    return redirect(url_for('auth.login'))
