import json
from matplotlib import pyplot as plt
import numpy as np

with open("song_index.json", "r") as file:
    songindex = json.load(file)

x = []
y = []

for song in songindex:
    if "sentiment" not in song: continue
    #if not any(("pop" in g) for g in song["genres"]): continue

    x.append(song["sentiment"]["com"])
    y.append(song["popularity"]["peak_pos"])

fig, ax = plt.subplots()
ax.set_ylim(100, 1)

plt.title("All Genres - Compound Sentiment vs. Popularity")
plt.ylabel("Peak Position")
plt.xlabel("Compound Score")

plt.yticks([1, 20, 40, 60, 80, 100])

plt.scatter(x, y, s=2)

z = np.polyfit(x, y, 2)
p = np.poly1d(z)
plt.plot(sorted(x), p(sorted(x)), "r--")

plt.show()