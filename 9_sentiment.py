import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import word_tokenize
import nltk.data

import json
import os
import re

from matplotlib import pyplot as plt

sid = SentimentIntensityAnalyzer()


def clean(lyrics_txt):
    lyrics_txt = lyrics_txt.lower()
    lyrics_txt = re.sub(r"\[[^\[\]]+\]|\(|\)", "", lyrics_txt)
    lyrics_txt = lyrics_txt.replace("\n", " ").replace(r"[^\w\d'\s]+", "")
    lyrics_txt = lyrics_txt.strip()
    return lyrics_txt


def get_song_sentiment(lyrics_txt):
    scores = sid.polarity_scores(lyrics_txt)
    return scores["pos"], scores["neg"], scores["neu"], scores["compound"]


with open("song_index.json", "r") as file:
    songindex = json.load(file)


x = []

for song in songindex:
    if "track_id" not in song: continue

    id = song["id"]
    path = "lyrics/" + str(id).zfill(4) + ".txt"
    if not os.path.exists(path): continue

    with open(path, "r", encoding="utf-8") as file:
        print(id)
        lyrics_txt = clean(file.read())
    pos, neg, neu, com = get_song_sentiment(lyrics_txt)
    song.update({"sentiment": {
        "pos": pos,
        "neg": neg,
        "neu": neu,
        "com": com
    }})
    x.append(com)

with open("song_index.json", "w+") as file:
    json.dump(songindex, file, indent=4)

plt.hist(x, density=True, bins=30)
plt.show()