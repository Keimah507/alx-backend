#!/usr/bin/env python3
"""Starts a flask application"""
from flask import Flask, render_template, request, g
from flask_babel import Babel


app = Flask(__name__)
babel = Babel()


class Config(object):
    """Config languages"""
    LANGUAGES = ['en', 'fr']


app.config.from_object(Config)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(login_as):
    """Gets a user from request"""
    if login_as and int(login_as) in users:
        return users.get(int(login_as))
    return None


@app.before_request
def before_request():
    """Executed before each request"""
    u_id = request.args.get("login_as")
    if u_id:
        user = get_user(u_id)
        g.user = user
    else:
        g.user = None



@babel.localeselector
def get_locale():
    """Determines the best match with our supported languages"""
    locale = request.args.get('locale')
    if locale:
        return locale
    return request.accept_languages.best_match(['LANGUAGES'])


@app.route('/', strict_slashes=False)
def hello_holberton():
    """Renders template 5-index.html"""
    return render_template('5-index.html')


if __name__ == "__main__":
    app.run()
