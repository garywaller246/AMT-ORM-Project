from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///atm.db'
db = SQLAlchemy(app)

#Model of the class
class Account(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	account_number = db.Column(db.Integer, unique=True, nullable=False)
	pin = db.Column(db.Integer, nullable=False)
	balance = db.Column(db.Integer)
	name = db.Column(db.Text)
	creditcard_number = db.Column(db.Integer)
	# def login()

