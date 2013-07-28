#!/usr/bin/env python

from flask import Flask, request, render_template, url_for, redirect, session, flash
import json

import settings

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        redirect_uri = url_for('roomba', _external=True)
        authorize_url = get_authorize_url(redirect_uri)
        return redirect(authorize_url)

    # Display intro page with login button that posts to here
    return render_template('index.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for(''))

if __name__ == '__main__':
    app.run(debug=True)
