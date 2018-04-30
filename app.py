from flask import Flask,render_template, request
import numpy as np
import pandas as pd
import pickle

app = Flask(__name__)
app.vars = {}
predictor = pickle.load(open('predictor-gd.pkl', 'rb'))

def findSum(a, b, estimator):
	X = pd.DataFrame([[a,b]])
	result = estimator.predict(X)
	return result[0]

@app.route('/', methods =['GET', 'POST'])
def index():
	if request.method == 'GET':
		return render_template('index.html', sum = 0, n1 = 0, n2 = 0)

	else:
		try:
			app.vars['n1'] = request.form['number1']
			app.vars['n2'] = request.form['number2']
			app.vars['sum'] = findSum(float(app.vars['n1']), float(app.vars['n2']), predictor)
		except:
			return render_template('index.html', sum = "%s + %s" % (app.vars['n1'], app.vars['n2']), n1 = app.vars['n1'], n2 = app.vars['n2'])
		return render_template('index.html', sum = app.vars['sum'], n1 = app.vars['n1'], n2 = app.vars['n2'])

@app.route('/backdoor/', methods = ['GET'])
def backdoor():
	x = float(request.args['x'])
	y = float(request.args['y'])
	sum = findSum(x, y, predictor)
	return str(sum)

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=33507, debug = True)