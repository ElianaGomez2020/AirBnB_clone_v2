#!/usr/bin/python3
"""starts a Flask web application"""
from flask import Flask
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def h_HBNB():
    """return hello hbnb"""
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def h_HBNB():
    """display hbnb"""
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def text(text):
    """display c followed by value"""
    return 'C {}'.format(text.replace('_',' '))
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port="5000")