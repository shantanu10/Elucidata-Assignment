import flask
from flask import Flask, request, render_template
import numpy as np
import pandas as pd
import model


app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return flask.render_template('index.html')


@app.route('/op1', methods=['POST'])
def operation1():
	if request.method=='POST':

		# get uploaded excel file if it exists
		file = request.files['excel']
		if not file: return render_template('index.html', label="No excel file")
        
		data = pd.read_excel(file)
		#print(data.head(10))
		label = 0
		label = model.operation1(data)

		return render_template('index.html', label=label)

@app.route('/op2', methods=['POST'])
def operation2():
	if request.method=='POST':

		# get uploaded excel file if it exists
		file = request.files['excel']
		if not file: return render_template('index.html', label="No excel file")
        
		data = pd.read_excel(file)
		#print(data.head(10))
		label = 0
		label = model.operation2(data)

		return render_template('index.html', label=label)

@app.route('/op3', methods=['POST'])
def operation3():
	if request.method=='POST':

		# get uploaded excel file if it exists
		file = request.files['excel']
		if not file: return render_template('index.html', label="No excel file")
        
		data = pd.read_excel(file)
		#print(data.head(10))
		label = 0
		label = model.operation3(data)

		return render_template('index.html', label=label)
@app.route('/return-files')
def return_back():
	try:
		return send_file('D:/Projects/Elucidata Assignment/Results/result1.xlsx', attachment_filename='result.xlsx')
	except Exception as e:
		return str(e)

if __name__ == '__main__':
	
	# start api
	app.run(host='0.0.0.0', port=8000, debug=True)
