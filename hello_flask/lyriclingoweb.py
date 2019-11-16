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
    for song in songs:
        x = song.split("\n")
        titles.append(x[0])

    for i in range(len(titles)):
        titles[i] = titles[i][:-1]

@APP.route("/")
def index():
    """ Displays the index page accessible at '/'
    """
    return render_template("test.html", content=titles)
    


if __name__ == '__main__':
    APP.run(debug=True)