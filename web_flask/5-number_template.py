#!/usr/bin/python3
"""
A script that starts a Flask web application
"""
from flask import Flask, render_template
app = Flask(__name__)
app.url_map.strict_slashes = False


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

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
