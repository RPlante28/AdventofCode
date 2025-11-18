import os

total = 0
listOne = []
listTwo = []

with open(os.path.join(os.path.dirname(__file__), 'list.txt'), 'r') as file:
    data = file.read()

for line in data.splitlines():
    line = line.split('   ')
    listOne.append(int(line[0]))
    listTwo.append(int(line[1]))

listOne = sorted(listOne)
listTwo = sorted(listTwo)

for i in range(len(listOne)):
    total += abs(listOne[i] - listTwo[i])

# part one
print(total)

# want to go back and see if I can optimize

# part two
similarity = 0
count = 0

for i in range(len(listOne)):
    count = 0
    for j in range(len(listTwo)):
        if listOne[i] == listTwo[j]:
            count += 1
    similarity += listOne[i] * count

print(similarity)