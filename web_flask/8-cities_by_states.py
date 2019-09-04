#!/usr/bin/python3
"""A script that starts a Flask web application"""

from models import storage
from flask import Flask, request, render_template
app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_list():
    states = storage.all('State')
    cities = storage.all('City')
    return render_template('8-cities_by_states.html',
                           states=states, cities=cities)


@app.teardown_appcontext
def sess_close(self):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
