#!/usr/bin/python3
"""A script that starts a Flask web application"""

from models import storage
from flask import Flask, request, render_template
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    result = storage.all('State')
    return render_template('7-states_list.html', result=result)


@app.teardown_appcontext
def sess_close(self):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
