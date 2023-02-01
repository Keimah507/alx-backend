#!/usr/bin/env python3
"""Starts a flask application"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import str 
import pytz


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
    u_id = request.args.get("login_as")
    if u_id:
        user = get_user(u_id)
        if user.get('locale') in Config.LANGUAGES:
            return user.get('locale')
    header_locale = request.headers.get('locale')
    if header_locale:
        return header_locale
    return request.accept_languages.best_match(['LANGUAGES'])


@babel.timezoneselector
def get_timezone() -> str:
    """get most appropriate timezone"""
    timezone = request.args.get('timezone')
    u_id = request.args.get('login_as')
    localTimeZone = users[int(u_id)]['timezone']
    if not timezone and not localTimeZone:
        return app.config['BABEL_DEFAULT_TIMEZONE']
    if timezone in pytz.all_timezones:
        return timezone
    elif localTimeZone in pytz.all_timezones:
        return localTimeZone
    else:
        raise pytz.exceptions.UnknownTimeZoneError
    


@app.route('/', strict_slashes=False)
def hello_holberton():
    """Renders template 6-index.html"""
    return render_template('6-index.html')


if __name__ == "__main__":
    app.run()
