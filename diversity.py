from matplotlib import pyplot as plt
import csv

array = []
with open("stuff.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        array.append(row)

key = array.pop(0)
array.sort(key=lambda x: x[0])
print(array[0])

memory = {}
for row in array:
    year = int(row[1][-4:])
    rank = int(row[2])
    # if rank > 10: continue
    if year not in memory:
        memory[year] = set()
    memory[year].add(row[4])

x = memory.keys()
y = [len(n) for n in memory.values()]

plt.plot(x, y)
plt.show()