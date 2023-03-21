#!/usr/bin/python3
""" Start Flask web application """


from flask import Flask, render_template
from models import storage
from models.state import State
from flask import flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown_db(exception):
    """  SQLAlchemy session closed after """
    storage.close()


@app.route('/states')
def list_states():
    """ List all states """
    states = storage.all(State).values()
    states = sorted(states, key=lambda state: state.name)
    return render_template('7-states_list.html', states=states)


@app.route('/states/<id>')
def show_state(id):
    """ Show states """
    state = storage.get(State, id)
    if state is None:
        return render_template('7-not_found.html')
    cities = sorted(state.cities, key=lambda city: city.name)
    return render_template('9-states.html', state=state, cities=cities)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

