#!/usr/bin/python3
"""Write a script that starts a Flask web application:

Your web application must be listening on 0.0.0.0, port 5000
Routes:
/: display “Hello HBNB!”
You must use the option strict_slashes=False in your route definition"""

from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def display():
    '''The home page.'''
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def display_hbnb():
    '''The hbnb page.'''
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def display_text(text):
    '''The c page.'''
    new_text = text.replace('_', ' ')
    return "C {}".format(new_text)


if __name__ == '__main__':
    app.run(host='localhost', port=5000)
