#!/usr/bin/python3
'''Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Route(s):
    /: Displays "Hello HBNB!"
    /hbnb: Displays "HBNB"
    /c/<text>: display “C ” followed by the value of the text variable
'''
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_HBNB():
    '''Displays "Hello HBNB!"'''
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    '''Displays "HBNB"'''
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    '''Displays <text> (replace any underscore with a space).'''
    text = text.replace('_', ' ')
    return "C {}".format(text)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
