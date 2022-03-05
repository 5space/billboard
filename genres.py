from matplotlib import pyplot as plt
import csv


array1 = []
with open("stuff.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        array1.append(row)

key1 = array1.pop(0)
array1.sort(key=lambda x: x[0])
print(array1[0])

song_index = {n[5]: n for n in array1}


array2 = []
with open("features.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        array2.append(row)

key2 = array2.pop(0)
array2.sort(key=lambda x: x[0])

memory = {y: [] for y in range(1958, 2020)}
for row in array2:
    if row[0] in song_index:
        song_row = song_index[row[0]]
    else:
        print("error")
        continue
    year = int(song_row[1][-4:])
    rank = int(song_row[2])
    # if rank > 10: continue
    genres = row[3][2:-2].split(", ")
    if any("rock" in b for b in genres):
        memory[year].append(1)
    else:
        memory[year].append(0)

x = memory.keys()
y = [sum(n)/len(n) for n in memory.values()]

plt.plot(x, y)
plt.show()