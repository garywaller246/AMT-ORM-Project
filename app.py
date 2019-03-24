from account import Account, app
from flask import Flask, render_template, request, redirect, url_for


@app.route('/', methods=['POST', 'GET'])
def index():
  if request.method == 'POST':
    account_number = request.form['account-number']
    pin = request.form['pin']

    account = Account(account_number=account_number, pin=pin)
    all_accounts = account.query.all()
    for accounts in all_accounts:
        print(accounts.id, accounts.account_number, accounts.pin)

    # account = Account(account_number, pin)
    # print( account.get() )

  return render_template('index.html')



@app.route('/menu/<int:account_number>/')
def menu(account_number):
  # balance = ...... a vous de trouver la balance avec SQL
  return render_template('menu.html', balance=balance)