#!/usr/bin/env python

from flask import Flask, request, render_template, url_for, redirect, session, flash
import json
import socket
import settings

from gevent.pywsgi import WSGIServer
from geventwebsocket.handler import WebSocketHandler

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        redirect_uri = url_for('roomba', _external=True)
        authorize_url = get_authorize_url(redirect_uri)
        return redirect(authorize_url)

    # Display intro page with login button that posts to here
    return render_template('index.html')

def wsgi_app(environ, start_response):
    path = environ["PATH_INFO"]
    if path == "/":
        return app(environ, start_response)
    elif path == "/websocket":
        handle_websocket(environ["wsgi.websocket"])
    else:  
        return app(environ, start_response)

def handle_websocket(ws):
    while True:
        message = ws.receive()
        if message is None:
            break
        message = json.loads(message)
        ws.send(json.dumps({'output': message['output']}))

@app.route('/control', methods=['GET'])
def control():
    return render_template('control.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for(''))

if __name__ == '__main__':
    http_server = WSGIServer((host,port), wsgi_app, handler_class=WebSocketHandler)
    print('Server started at %s:%s'%(host,port))
    app.run(debug=True)
    http_server.serve_forever()