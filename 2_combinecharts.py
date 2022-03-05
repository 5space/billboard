import json
import os

fulldata = []
for filename in os.listdir("charts"):
    with open("charts/" + filename) as file:
        fulldata.append(json.load(file))

with open("combined_charts.json", "w+") as combined:
    json.dump(fulldata, combined, indent=4)