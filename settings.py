from os import environ as env

try:
    # Any seeting happens here. For example, you can do the following:
    # OAuth2 client ID and secret
    # CLIENT_ID = env['CLIENT_ID']
    # CLIENT_SECRET = env['CLIENT_SECRET']
    # SECRET_KEY = env['SECRET_KEY']
    pass

except KeyError:
    print 'You need to set SECRET_KEY in the environment for this app'
    print 'e.g `SECRET_KEY=XXXX python app.py`'
    exit(1)

