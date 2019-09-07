#!/usr/bin/python3
"""A script that starts a Flask web application"""

from models import storage, State, Amenity, Place
from flask import Flask, request, render_template
app = Flask(__name__)


@app.route('/hbnb')
def hbnb_filters():
    states = storage.all('State')
    amenities = storage.all('Amenity')
    places = storage.all('Place')
    return render_template('100-hbnb.html', places=places,
                           states=states, amenities=amenities)


@app.teardown_appcontext
def sess_close(self):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
