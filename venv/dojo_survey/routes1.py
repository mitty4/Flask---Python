from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

app.secret_key = 'blah'

@app.route('/')
def index():
  return render_template("form.html")

@app.route('/users', methods=['POST'])
def create_user():
   session['name'] = request.form['name']
   return redirect('/')

@app.route('/show')
def show_user():
  return render_template('show.html', name=session['name'])

@app.route('/reset', methods=['POST'])
def reset():
	if 'name' in session:
		session['name']="no input"
	return redirect('/')
  
app.run(debug=False)