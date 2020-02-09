"""
A simple web app
"""
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    """
    A function that runs every time a user accesses the / route
    """
    return 'Hello World'


@app.route('/<name>')
def hello_name(name):
    """
    A function that runs every tie a user accesses the / route
    """
    return 'Hello %s' % name
