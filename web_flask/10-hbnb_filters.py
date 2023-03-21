#!/usr/bin/python3
"""
Starts a Flask web application
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def hbnb_close(self):
    storage.close()


@app.route('/')
def hello_hbnb():
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    return 'HBNB'


@app.route('/c/<string:name>')
def cname(name=None):
    name = name.replace("_", " ")
    return "C {}".format(name)


@app.route('/python/', defaults={'text': "is cool"})
@app.route('/python/<string:text>')
def pythontext(text="is cool"):
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route('/number/<int:num>')
def isnumber(num=None):
    return "{} is a number".format(num)


@app.route('/number_template/<int:num>')
def return_page(num=None):
    return render_template("5-number.html", value=num)


@app.route('/states_list')
def state_list(num=None):
    states = storage.all(State).values()
    return render_template("7-states_list.html", states=states)


@app.route('/states/', defaults={'id': None})
@app.route('/states/<id>')
def statest(id=None):
    inlist = 0
    states = storage.all(State).values()
    for data in states:
        inlist = 1
        if (id == data.id):
            return render_template("9-states.html", states=data)
    if (id is not None and inlist == 1):
        return render_template("9-states.html", states=None)
    return render_template("9-states.html", states=states)


@app.route('/cities_by_states')
def cities_state_list(num=None):
    states = storage.all(State).values()
    return render_template("8-cities_by_states.html", states=states)


@app.route('/hbnb_filters')
def hbnb_display():
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    return render_template("10-hbnb_filters.html", states=states,
                           amenities=amenities)


@app.route('/number_odd_or_even/<int:num>')
def return_page_even(num=None):
    if (num & 1):
        data = "{} is odd".format(num)
        return render_template("6-number_odd_or_even.html", value=data)
    else:
        data = "{} is even".format(num)
        return render_template("6-number_odd_or_even.html", value=data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
