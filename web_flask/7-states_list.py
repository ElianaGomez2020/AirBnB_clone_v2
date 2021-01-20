#!/usr/bin/python3
"""script that starts a Flask web application"""
from Flask import Flask
from Flask import render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.teardown_appcontext
def closes():
    """closes session"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def state_l():
    """"return list states"""
    storage.close()
    return render_template('7-states_list.html',
                           states=storage.all('State').values())

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
