import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
import time
import os

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

with open("song_index.json", "r") as file:
    songindex = json.load(file)

for song in songindex:
    # last_req = time.time()
    artist, title, id = song["artist"], song["title"], song["id"]
    artist = artist.split(" Featuring ")[0].split(" x ")[0].split(" X ")[0].split(" & ")[0].split(", ")[0]

    search = sp.search(q=f"artist:{artist} track:{title}")
    print(json.dumps(search, indent=4))
    break
    if len(search["tracks"]["items"]) == 0:
        print("ERROR: NO RESULTS")
        continue

    songdata = search["tracks"]["items"][0]

    track_id = songdata["id"]
    album_id = songdata["album"]["id"]
    artist_id = songdata["artists"][0]["id"]

    dtitle = songdata["name"]
    dartist = songdata["artists"][0]["name"]

    song.update({
        "track_id": track_id,
        "album_id": album_id,
        "artist_id": artist_id
    })
    
    toadd = "\n" + str(id) + "\n" + title.ljust(50) + artist + "\n" + dtitle.ljust(50) + dartist
    with open("log_spotify.txt", "a", encoding="utf-8") as log:
        log.write(toadd)
    print(toadd[1:])

    with open("song_index.json", "w+") as file:
        json.dump(songindex, file, indent=4)

    # diff = time.time() - last_req
    # if diff < 4: time.sleep(4 - diff)