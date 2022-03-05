import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
import time

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

with open("song_index.json", "r") as file:
    songindex = json.load(file)

for song in songindex:
    if "artist_id" not in song: continue

    artist_id = song["artist_id"]
    id = song["id"]

    artist = sp.artist("spotify:artist:" + artist_id)
    print(id, artist["genres"])

    song.update({"genres": artist["genres"]})

    with open("song_index.json", "w+") as file:
        json.dump(songindex, file, indent=4)