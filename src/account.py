from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from src.database import Wallet, db, Payment

account = Blueprint('account',__name__,url_prefix='/')

# TODO Add pagination to all pages

@account.route('/')
@login_required
def dashboard():
    wallet = Wallet.query.filter_by(user_id=current_user.id).first()
    recent_payments = Payment.query.filter_by(user_id=current_user.id).order_by(Payment.created_at.desc()).limit(20).all()
    return render_template('account/dashboard.html', wallet=wallet, recent_payments=recent_payments)


@account.route('/payments')
def payments():
    payments = Payment.query.filter_by(user_id=current_user.id).order_by(Payment.created_at.desc()).limit(
        20).all()
    return render_template('account/payments.html', payments=payments)

@account.get('/payments/filter')
def filter_payments():
    date_from = request.args.get("date_from")
    date_to = request.args.get("date_to")

    payments = Payment.query.filter_by(user_id=current_user.id)\
        .order_by(Payment.created_at.desc())\
        .filter(Payment.created_at.between(date_from, date_to))\
        .all()

    return render_template('account/payments.html',payments=payments)