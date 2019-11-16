#!/usr/bin/env python3
import requests
import string
from bs4 import BeautifulSoup as bs
import re
 
def main():
    urls = []
    with open('disney_links.txt','r') as f:
        urls = f.read().split('\n')
    lyrics = []
    for u in urls:
        print("parsing", u)
        x = parse_lyrics(get_html(u))
        lyrics.append(x)
        with open('disney_lyrics.txt', 'a') as f:
            f.write(x + "\n\n\n")
    lyrics = "\n\n\n".join(lyrics)
    with open('disney_lyrics_all.txt', 'w') as f:
        f.write(lyrics)
 

# Function to get HTML 
def get_html(URL):
    r = requests.get(URL)
    return r

def parse_lyrics(html):
    # Parse for lyrics using BeautifulSoap
    soup = bs(html.text, 'html.parser')
    song_body = soup.find(class_="lyrics")
    lyrics = song_body.find('p')
    lyrics = re.sub("<(?:a\b[^>]*>|/a>)", "", lyrics.text)
    return lyrics


def construct_song_URL(artist, song_title):

    #Replacing punctuation
    for c in string.punctuation:
        song_title = song_title.replace(c, "")

    artist_URL = ""
    song_URL = ""

    artist_list = artist.split(" ")


    song_title_list = song_title.split(" ")

    for i in artist_list:
        artist_URL += i + "-"

    for j in range(0, len(song_title_list)):
        song_URL += song_title_list[j] + "-"
    return(artist_URL + song_URL + "lyrics")



if __name__ == "__main__":
    main()
