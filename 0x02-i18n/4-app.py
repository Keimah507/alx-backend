#!/usr/bin/env python3
"""Starts a Flask application"""
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel()


class Config(object):
    """Config languages"""
    LANGUAGES = ['en', 'fr']


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """Determines the best match with our supported languages"""
    locale = request.args.get('locale')
    if locale:
        return locale
    return request.accept_languages.best_match(['LANGUAGES'])


@app.route('/', strict_slashes=False)
def hello_holberton():
    """Renders template 4-index.html"""
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run()
