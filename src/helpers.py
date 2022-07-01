from src.database import User, db, Wallet, Payment
from src.constants.transactions import TRANSACTION_TYPE_DEPOSIT, TRANSACTION_TYPE_SENDING, ACCOUNT_TYPE_BANK, \
    ACCOUNT_TYPE_PHONE
from faker import Faker
import random


def top_up_wallet(user_id, amount, transaction_type):
    wallet = Wallet.query.filter_by(id=user_id).first()
    wallet_balance = wallet.amount

    if transaction_type == TRANSACTION_TYPE_DEPOSIT:
        new_balance = wallet_balance + amount
    else:
        new_balance = wallet_balance + amount

    # Update the wallet balance
    # TODO For the cases off creating sample data, this value may go to negative

    wallet.amount = new_balance
    db.session.commit()


def create_sample_data():
    # Get all users
    users = User.query.all()

    if not users:
        return "Please register some test accounts first."
    try:
        for user in users:
            # Call create sample transactions function
            create_sample_transactions(user.id)

        return "Successfully generated random data"

    except:
        return "Failed to generate random data"


def create_sample_transactions(user_id):
    faker = Faker()
    transaction_types = [TRANSACTION_TYPE_SENDING, TRANSACTION_TYPE_DEPOSIT]
    account_types = [ACCOUNT_TYPE_PHONE, ACCOUNT_TYPE_BANK]
    currencies = ['KES', 'BXC', 'UGH', 'GHC']
    for i in range(10):
        transaction_type = random.choices(transaction_types)
        amount = random.randint(300, 20000)
        account_type = random.choices(account_types)
        # TODO find a better way to handle this
        if account_type == 'PHONE':
            account = '254' + str(random.randint(100000000, 999999999))
        else:
            account = random.randint(1000000000, 9999999999)

        created_at = faker.date_time_between(start_date='-1y', end_date='now')
        transaction = Payment(name=faker.name(),
                              amount=amount,
                              type=transaction_type,
                              account_number=account,
                              account_type=account_type,
                              currency=random.choices(currencies),
                              user_id=user_id,
                              created_at=created_at)
        db.session.add(transaction)
        db.session.commit()

        # Top up the users wallet
        top_up_wallet(user_id, amount, transaction_type)
