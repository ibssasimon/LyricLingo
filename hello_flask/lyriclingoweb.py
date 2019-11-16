#!/usr/bin/env python

from flask import Flask, render_template


# Create the application.
APP = Flask(__name__)

with open("../translated_lyrics.txt", "r") as f:
    content = f.read()
    songs = []
    songs = content.split("*[")
    songs.remove('')

    titles = []

@APP.route("/")
def index():
    """ Displays the index page accessible at '/'
    """
    return render_template("test.html", content=songs[1])


if __name__ == '__main__':
    APP.run(debug=True)