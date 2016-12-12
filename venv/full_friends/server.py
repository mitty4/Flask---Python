from flask import Flask, request, redirect, render_template
from mysqlconnection import MySQLConnector
import datetime
app = Flask(__name__)
mysql = MySQLConnector(app,'the_wall')


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/friends', methods=['POST'])
def create():
    data = {
    	"first_name": request.form['first_name'],
    	"last_name": request.form['last_name'],
    	"email": request.form['email'],
    	"created_at": datetime.datetime.now()
    }
    mysql.query_db("INSERT INTO friends (first_name, last_name, email, created_at) VALUES (:first_name, :last_name, :email, :created_at)", data)
    return redirect('/')


app.run(debug=False)








