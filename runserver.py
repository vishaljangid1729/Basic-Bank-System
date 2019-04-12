"""
This script runs the FlaskWebProjectDBMS application using a development server.
"""

from os import environ
from FlaskWebProjectDBMS import app

app.config['SECRET_KEY'] = 'DontTellAnyone'

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.debug = True
    app.run(HOST, PORT)
