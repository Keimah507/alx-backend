#!/usr/bin/env python3
"""Starts a flask application"""

from flask import Flask, request, render_template
from flask_babel import Babel, gettext

app = Flask(__name__)
babel = Babel()


class Config(object):
    """Config languages"""
    LANGUAGES = ['en', 'es', 'fr']


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """Determines the best match with our supported languages"""
    return request.accept_languages.best_match(['LANGUAGES'])


@app.route('/', strict_slashes=False)
def hello_holberton():
    """Renders template 3-index.html"""
    return render_template('3-index.html')


if __name__ == "__main__":
    app.run()
