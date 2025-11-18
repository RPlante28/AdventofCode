import os

numSafe = 0
rec = 0
trend = False
curr = False
diff = 0
safe = []
unsafe = []

with open(os.path.join(os.path.dirname(__file__), 'data.txt'), 'r') as file:
    data = file.read()

# part one

for line in data.splitlines():
    rec = 0
    trend = False
    line = [int(record) for record in line.split(' ')]
    while rec < len(line) - 1:
        curr = line[rec] < line[rec + 1]
        if rec == 0:
            trend = line[rec] < line[rec + 1]
        diff = abs(line[rec] - line[rec + 1])
        if trend != curr or (diff < 1 or diff > 3):
            unsafe.append(line)
            break
        rec += 1
        if rec == len(line) - 1:
            safe.append(line)
            numSafe += 1

print(numSafe)

# part two - problem dampener
# if you can remove one level to fix report, then it can be considered safe
print(safe)
print(unsafe)