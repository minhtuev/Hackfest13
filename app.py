import os
import json
from gevent.pywsgi import WSGIServer
from geventwebsocket.handler import WebSocketHandler
import flask
app = flask.Flask(__name__)
app.secret_key = os.urandom(24)
app.debug = True
host,port='localhost',8000
 
@app.route('/')
def index():
    return flask.render_template('index.html')

@app.route('/control')
def control():
    return flask.render_template('control.html', port=port)

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
        print message
        ws.send(json.dumps({'output': message['output']}))
if __name__ == '__main__':
    http_server = WSGIServer((host,port), wsgi_app, handler_class=WebSocketHandler)
    print('Server started at %s:%s'%(host,port))
    http_server.serve_forever()