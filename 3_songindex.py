import json

with open("combined_charts.json", "r") as file:
    fulldata = json.load(file)

all_songs = set()
for chart in fulldata:
    for entry in chart["entries"]:
        all_songs.add((entry["artist"], entry["title"]))

all_songs_sorted = sorted(list(all_songs), key=lambda x: (x[0]+x[1]).lower())
full_index = [{"artist": a, "title": t, "id": i} for i, (a, t) in enumerate(all_songs_sorted)]

with open("song_index.json", "w+") as file:
    json.dump(full_index, file, indent=4)