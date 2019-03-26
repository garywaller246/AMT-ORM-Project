from account import Account, app
from flask import Flask, render_template, request, redirect, url_for


@app.route('/', methods=['POST', 'GET'])
def index():
  if request.method == 'POST':
    account_number = request.form['account-number']
    pin = request.form['pin']

    account = Account.query.filter_by(account_number=account_number).first()
    if account.pin == int(pin):
      return redirect(url_for('menu', account_number=account_number) )

    # account = Account(account_number=account_number, pin=pin)
    # all_accounts = account.query.all()
    # for accounts in all_accounts:
    #   if account_number == accounts.account_number and pin == accounts.pin:
    #     return redirect('deposit.html')
        
    # account = Account(account_number, pin)
    # print( account.get() )

  return render_template('index.html')



@app.route('/menu/<int:account_number>/')
def menu(account_number):
  account = Account.query.filter_by(account_number=account_number).first()
  return render_template('menu.html', balance=account.balance, account_number=account_number)