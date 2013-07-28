#!/usr/bin/env python

from flask import Flask, request, render_template, url_for, redirect, session, flash
import json
import settings


port = 2000
app = Flask(__name__)
app.secret_key = settings.SECRET_KEY

@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		session['access_token'] = request.cookies.get('remember_token')
		return redirect(url_for('control', _external=True))
	robots = [
		{"name": "Roomba1", "status": "green"},
		{"name": "Roomba2", "status": "red"},
		{"name": "Roomba3", "status": "red"}]
	return render_template('index.html', robots=robots)

@app.route('/control', methods=['GET', 'POST'])
def control():
	if request.method == 'POST':
		session.pop('remember_token', None)
		return redirect(url_for('index', _external=True))
	return render_template('control.html', port=port)

if __name__ == '__main__':
	app.run(debug=True)