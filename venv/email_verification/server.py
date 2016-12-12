from flask import Flask, render_template, redirect, session, request, flash
from mysqlconnection import MySQLConnector
import re
import datetime
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-z]*$')
app = Flask(__name__)
app.secret_key = 'blah'

mysql = MySQLConnector(app, 'email_verification')


@app.route('/')
def index():
	return render_template('index.html')


@app.route('/register')
def register():
	mydict = {
		'email': session['email'],
		'created_at': datetime.datetime.now(),
	}
	email = mysql.query_db("INSERT INTO emails (email_address, created_at) VALUES (:email, :created_at)", mydict)
	return redirect('/')


@app.route('/check', methods=['POST'])
def check():
	if len(request.form['email']) < 1:
		flash('Too Empty')
	elif not EMAIL_REGEX.match(request.form['email']):
		flash('not a valid address')
	elif EMAIL_REGEX.match(request.form['email']):
		flash('success!'+request.form['email']+'was added!')
		session['email'] = request.form['email']
		return redirect('/register')
	return redirect('/')


@app.route('/success')
def success():
	return render_template('success.html', rows = mysql.query_db("SELECT email_address, created_at FROM emails"))

app.run(debug=False)