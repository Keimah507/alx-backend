#!/usr/bin/env python3
"""Starts a Flask app"""

from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel()


class Config(object):
    """Config languages"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'utc'


app.config.from_object(Config)


@app.route('/', strict_slashes=False)
def hello_holberton():
    """Returns template 1-index.html"""
    return render_template('1-index.html')
