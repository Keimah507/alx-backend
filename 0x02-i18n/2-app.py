#!/usr/bin/python3
"""Starts a flask app"""

from flask import Flask, request, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel()


class Config(object):
    """Config languages"""
    LANGUAGES = ['en', 'es', 'fr']


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """Determine best match with our supported languages"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def hello_holberton():
    """Returns template 2-index.html"""
    return render_template('2-index.html')


if __name__ == "__main__":
    app.run()
