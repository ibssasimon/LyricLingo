#!/usr/bin/env python

from flask import Flask, render_template


# Create the application.
APP = Flask(__name__)


@APP.route("/")
def index():
    """ Displays the index page accessible at '/'
    """
    return render_template("index.html")


if __name__ == '__main__':
    APP.run(debug=True)