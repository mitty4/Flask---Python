from flask import Flask, render_template, session, request, redirect
from random import randint
import datetime
app = Flask(__name__)
app.secret_key = "blah"

@app.route('/')
def index():
	if 'gold' not in session:
		session['gold']=0
	if 'act' not in session:
		session['act'] = []
	if 'spend' not in session:
		session['spend'] = []
	return render_template('index.html', gold=session['gold'], activity=reversed(session['act']), reset=session['spend'])

@app.route('/process_money', methods=["POST"])
def gold():
	session['spend']=[]
	time_now = datetime.datetime.now()
	location = request.form['location']
	if location == 'farm':
		gold_amt=randint(10,20)
		session['gold'] += gold_amt
		msg = "Earned {} golds from ({})".format(gold_amt, time_now)
		dictmsg = {
			'act':msg,
			'color': 'green'
			}
		session['act'].append(dictmsg)
	elif location == 'cave':
		gold_amt=randint(5,10)
		session['gold'] += gold_amt
		msg = "Earned {} golds from ({})".format(gold_amt,time_now)
		dictmsg = {
			'act':msg,
			'color': 'green'
			}
		session['act'].append(dictmsg)

	elif location == 'house':
		gold_amt=randint(2,5)
		session['gold'] += gold_amt
		msg = "Earned {} golds from ({})".format(gold_amt,time_now)
		dictmsg = {
			'act':msg,
			'color': 'green'
			}
		session['act'].append(dictmsg)

	elif location == 'casino':
		gold_amt=randint(-50,50)
		session['gold'] += gold_amt
		if gold_amt<0:
			msg = 'Entered a casino and lost {} golds...ouch.. ({})'.format(gold_amt,time_now)
			dictmsg = {
			'act':msg,
			'color': 'red'
			}
			session['act'].append(dictmsg)
		else:
			msg = 'Entered a casino and won {} golds... woo!.. ({})'.format(gold_amt,time_now)
			dictmsg = {
			'act':msg,
			'color': 'green'
			}
			session['act'].append(dictmsg)
	return redirect('/')

@app.route('/reset')
def reset():
	session['gold']=0
	session['act']=[]
	session['spend']=[]
	msg = "No more gold :("
	session['spend'].append(msg)
	return redirect('/')


app.run(debug=False)