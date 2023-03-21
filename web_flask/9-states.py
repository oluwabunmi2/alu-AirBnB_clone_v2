#!/usr/bin/python3
"""
Flask web application
"""

from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown_db(exception):
    """ Close the SQLAlchemy session after each request """
    storage.close()


@app.route('/states')
def list_states():
    """ Display a HTML page with a list of all State objects """
    states = storage.all(State).values()
    states = sorted(states, key=lambda state: state.name)
    return render_template('7-states_list.html', states=states)


@app.route('/states/<id>')
def show_state(id):
    """ Display a HTML page with the details of a State object """
    state = storage.get(State, id)
    if state is None:
        return render_template('7-not_found.html')
    cities = sorted(state.cities, key=lambda city: city.name)
    return render_template('9-states.html', state=state, cities=cities)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


