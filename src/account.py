from flask import Blueprint, render_template

account = Blueprint('account',__name__,url_prefix='/account')

@account.route('/')
def dashboard():
    return render_template('account/dashboard.html')


@account.route('/payment_history')
def payments():
    return render_template('account/payments.html')
