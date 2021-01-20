#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.teardown_appcontext
def closes(self):
    """closes session"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def state_l():
    """"return list states"""
    list_st = storage.all(State).values()
    return render_template('7-states_list.html', states=list_st)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
