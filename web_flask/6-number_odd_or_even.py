#!/usr/bin/python3
"""starts a Flask web application"""
from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def h_HBNB():
    """return hello hbnb"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def h_HBNB_():
    """display hbnb"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def text(text):
    """display c followed by value"""
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/')
@app.route('/python/<text>', strict_slashes=False)
def text_py(text='is cool'):
    """display “Python ” followed by value"""
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def num(n):
    """display “n if is a number” followed by value"""
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def num_route(n):
    """display a HTML page only if n is an intege"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def num_odd(n):
    """display a HTML page only if n is an integer"""
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port="5000")
