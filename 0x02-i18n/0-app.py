#!/usr/bin/env python3
"""Starts a flask application"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_holberton():
    """Returns template index.html"""
    return render_template('index.html')

if __name__ == "__main__":
    app.run()