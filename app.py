#!/usr/bin/env python

from flask import Flask, request, render_template, url_for, redirect, session, flash
import json
import settings
import os


port = 2000
app = Flask(__name__)
app.secret_key = settings.SECRET_KEY



@app.route('/', methods=['GET', 'POST'])
def index():
	isAvailable = "red"
	stuff = open("session", "rb").read()

	if(stuff == ""):
		isAvailable = "green"

	if request.method == 'POST':

		if open("session", "rb").read() == "":
			random = os.urandom(10)
			session['access_token'] = random
			f = open("session", "w")
			f.write(random)
			f.close()
			return redirect(url_for('control', _external=True))
		else:
			return redirect(url_for('index', _external=True)) 

	robots = [
		{"name": "Teemo", "status": isAvailable},
		{"name": "Jayce", "status": "darkred"},
		{"name": "Kayle", "status": "darkred"}]
	return render_template('index.html', robots=robots, isAvailable=isAvailable)

@app.route('/control', methods=['GET', 'POST'])
def control():
	if request.method == 'POST':
		#session.pop('access_token', None)
		session['access_token'] = None
		f = open("session", "w")
		f.write("")
		f.close()

		return redirect(url_for('index', _external=True))
	return render_template('control.html', port=port)

if __name__ == '__main__':
	app.run(debug=True)