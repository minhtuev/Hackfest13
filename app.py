#!/usr/bin/env python

from flask import Flask, request, render_template, url_for, redirect, session, flash
import json
import settings


port = 2000
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/control', methods=['GET'])
def control():
    return render_template('control.html', port=port)

if __name__ == '__main__':
    app.run(debug=True)