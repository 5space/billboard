import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
import time
import os

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

with open("song_index.json", "r") as file:
    songindex = json.load(file)

for song in songindex:
    if "track_id" in song: continue
    print(song["title"], "|||", song["artist"])