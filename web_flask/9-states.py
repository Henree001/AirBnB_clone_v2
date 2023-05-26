#!/usr/bin/python3
"""Write a script that starts a Flask web application:

Your web application must be listening on 0.0.0.0, port 5000
Routes:
/: display “Hello HBNB!”
You must use the option strict_slashes=False in your route definition"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
data = storage.all(State).values()


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def state_list(id=None):
    """displays a HTML page of the list of states"""
    return render_template('9-states.html', data=data, id=id)


@app.teardown_appcontext
def teardown_session(exception):
    """Removes the current SQLAlchemy Session after each request"""
    storage.close()


if __name__ == '__main__':
    app.run(host='localhost', port=5000)
