import random
from account import Account, db
from faker import Faker


def generate_account_number():
    generate_account_number = random.randint(100000, 999999)

    while Account.query.filter_by(account_number=generate_account_number).first() != None:
        generate_account_number = random.randint(100000, 999999)

    return generate_account_number


def generate_pin_number():
    return random.randint(100,999)


def generate_balance():
    return random.randint(0,10000)


def generate_fake_account():
    return Account (
        account_number = generate_account_number(),
        pin=generate_pin_number(),
        balance=generate_balance()
    )

def generate_fake_name_ccNumber():
    fake = Faker ()
    for account in Account.query.all():
        account.name = fake.name()
        account.creditcard_number = fake.credit_card_number()
    db.session.commit()


def generate_accounts(max_number):
    for x in range (max_number):
        account = generate_fake_account()
        db.session.add(account)

    db.session.commit()

# generate_accounts(1000)

generate_fake_name_ccNumber()