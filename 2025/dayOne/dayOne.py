import os

file_name = 'data.txt'
filepath = os.path.join(os.path.dirname(__file__), file_name)

direction = 0
amount = []
pos = 50
count = 0
count_zero = 0

# unpack file
with open(filepath, 'r') as r:
    file = r.read().splitlines()

def update_pos(curr_pos, rot_amnt) -> int:
    curr_pos += rot_amnt
    if curr_pos == 100: curr_pos = 0
    if curr_pos < 0: curr_pos = 99
    return curr_pos

for line in file:
    direction = 1 if line[0] == 'R' else -1
    amount = int(line[1::])

    for i in range(amount):
        pos = update_pos(pos, direction)
        if pos == 0: count += 1


print(count)