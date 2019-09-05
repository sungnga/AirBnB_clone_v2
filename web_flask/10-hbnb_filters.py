#!/usr/bin/python3
"""A script that starts a Flask web application"""

from models import storage
from flask import Flask, request, render_template
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def cities_list(id=None):
    states = storage.all('State')
    cities = storage.all('City')
    if id:
        id = '{}.{}'.format('State', id)
    return render_template('9-states.html',
                           states=states, id=id)


@app.route('/hbnb_filters')
def hbnb_filters():
    states = storage.all('State')
    amenities = storage.all('Amenity')
    return render_template('10-hbnb_filters.html',
                           states=states, amenities=amenities)


@app.teardown_appcontext
def sess_close(self):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
