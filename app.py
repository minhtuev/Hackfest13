#!/usr/bin/env python

from flask import Flask, request, render_template, url_for, redirect, session, flash
import json
import settings
import os

app = Flask(__name__)
app.secret_key = settings.SECRET_KEY

# our main page
@app.route('/', methods=['GET', 'POST'])
def index():
	isAvailable = "red"
	# open file, read in the user state from the file
	stuff = open("session", "wb+").read()

	# if empty file, then robot is available
	if(stuff == ""):
		isAvailable = "green"

	if request.method == 'POST':
		# if we are trying to write to the file & the file is available
		# then write it
		if open("session", "rb").read() == "":
			random = os.urandom(10)
			session['access_token'] = random
			# write the token to the file
			with open("session", "w") as f:
				f.write(random)
			return redirect(url_for('control', _external=True))
		else:
			return redirect(url_for('index', _external=True)) 

	robots = [
		{"name": "Teemo", "status": isAvailable},
		{"name": "Jayce", "status": "darkred"},
		{"name": "Kayle", "status": "darkred"}]
	return render_template('index.html', robots=robots, isAvailable=isAvailable)

# our control page
@app.route('/control', methods=['GET', 'POST'])
def control():
	# 	return redirect(url_for('index', _external=True))
	if open("session", "rb").read() == session['access_token']:
		return render_template('control.html')

	return redirect(url_for('index', _external=True)) 

# this should be the url when we leave
@app.route('/leave', methods=['GET'])
def leave():
	# clearing the cookie
	session.pop('access_token', None)
	# clearing the server file
	with open("session", "w") as f:
		f.write("")

	return redirect(url_for('index', _external=True))

if __name__ == '__main__':
	app.run(debug=True)