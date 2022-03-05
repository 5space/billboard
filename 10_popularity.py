import json

with open("combined_charts.json", "r") as file:
    fulldata = json.load(file)

with open("song_index.json", "r") as file:
    songindex = json.load(file)

key = {(s["title"], s["artist"]): s["id"] for s in songindex}

remaining = set(s["id"] for s in songindex)

for chart in fulldata:
    print(chart["date"])
    for song_entry in chart["entries"]:
        id = key[song_entry["title"], song_entry["artist"]]
        if id not in remaining: continue

        peak_pos = song_entry["peakPos"]

        songindex[id].update({"popularity": {
            "peak_pos": peak_pos
        }})
        remaining.remove(id)

with open("song_index.json", "w+") as file:
    json.dump(songindex, file, indent=4)