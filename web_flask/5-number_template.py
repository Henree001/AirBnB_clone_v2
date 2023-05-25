#!/usr/bin/python3
"""Write a script that starts a Flask web application:

Your web application must be listening on 0.0.0.0, port 5000
Routes:
/: display “Hello HBNB!”
You must use the option strict_slashes=False in your route definition"""

from flask import Flask, render_template
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


@app.route("/python/<text>", strict_slashes=False)
@app.route("/python", strict_slashes=False)
def display_pytext(text="is cool"):
    '''The python page.'''
    new_text = text.replace('_', ' ')
    return "Python {}".format(new_text)


@app.route("/number/<int:n>", strict_slashes=False)
def number_page(n):
    '''The number page.'''
    return '{} is a number'.format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    '''html page'''
    return render_template('5-number.html', Number=n)


if __name__ == '__main__':
    app.run(host='localhost', port=5000)
