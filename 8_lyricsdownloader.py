import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import lyricsgenius
import json
import time
import os

from requests.exceptions import Timeout

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())


def get_song_info(song_id):
    search = sp.track(song_id)
    return search["name"], search["artists"][0]["name"]


genius = lyricsgenius.Genius("ijURGVtZnqKS7YOgitbHhprRYKY48zzLf5qegglWdDvue9MBfqv7nZMJr2y8cCJd")
log = open("log.txt", "a")


with open("song_index.json", "r") as file:
    songindex = json.load(file)


for song in songindex[1684:]:
    if "track_id" not in song: continue
    # last_req = time.time()

    id = song["id"]
    title, artist = get_song_info(song["track_id"])
    title = title.split(" (")[0].split(" - The Voice")[0]
    toadd = "\n" + str(id) + "\n" + title.ljust(50) + artist

    while True:
        try:
            response = genius.search_song(title, artist)
            break
        except Timeout:
            print("TIMEOUT")
            continue

    if response is not None:
        response_json = json.loads(response.to_json())
        with open("lyrics/" + str(id).zfill(4) + ".txt", "w+", encoding="utf-8") as file:
            file.write(response.to_text())
        toadd += "\n" + response_json["title"].ljust(50) + response_json["artist"]
    else:
        toadd += "\n" + "ERROR"
    
    with open("log.txt", "a", encoding="utf-8") as log:
        log.write(toadd)
    print(toadd[1:])

    # diff = time.time() - last_req
    # if diff < 5: time.sleep(5 - diff)