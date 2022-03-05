import csv
import lyricsgenius
import os

genius = lyricsgenius.Genius(os.environ["GENIUS_CLIENT_ID"]))

rows = []
with open("stuff.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    key = reader.__next__()
    for row in reader:
        rows.append(row)

rows = sorted(rows, key=lambda x: x[0])[::-1]
rows = [(row[5], row[3], row[4]) for row in rows]
unique_songs = list(dict.fromkeys(rows).keys())

for id, song_name, artist_name in unique_songs:
    song = genius.search_song(song_name, artist_name)
    id = id.replace("/", "|")
    with open("lyrics/" + id + ".txt", "w+") as file:
        if song is None:
            print("Song", id, "not found")
            continue
        text = song.title + "\n" + song.artist + "\n\n" + song.lyrics
        file.write(text)
        print(song.title, song.artist)