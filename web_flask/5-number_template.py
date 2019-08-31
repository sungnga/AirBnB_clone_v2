#!/usr/bin/python3
"""A script that starts a Flask web application"""

from flask import Flask, request, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hello_hbnb():
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def hello_c(text):
    return 'C %s' % text.replace("_", " ")

@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    return 'Python {}'.format(text.replace("_", " "))

@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return '%d is a number' % n

@app.route('/number_template/<int:n>', strict_slashes=False)
def num_temp(n):
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
