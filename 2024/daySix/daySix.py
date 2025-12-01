# need to go back and finsish part two

import os

filepath = os.path.join(os.path.dirname(__file__), 'data.txt')

map = []
indicator = '^'

# unpack
with open(filepath, 'r') as reader:
    file = reader.read().splitlines()
    for line in file:
        map.append(list(line))

def find_self(char:str) -> tuple:
    for row in range(len(map)):
        if char in map[row]:
            return (row, map[row].index(indicator))
    
    return ()

def move(dir:tuple) -> tuple:
    global indicator
    y, x = find_self(indicator)
    y_dir, x_dir = dir
    possible_dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    indicators = ['^', '>', 'V', '<']

    if map[y + y_dir][x + x_dir] == '#':
        # turn
        curr_index = possible_dirs.index(dir)
        next_index = (curr_index + 1) % len(possible_dirs)
        dir = possible_dirs[next_index]
        indicator = indicators[next_index]
        map[y][x] = indicator
    else: 
        map[y][x] = 'X'
        map[y + y_dir][x + x_dir] = indicator

    return dir

def print_map() -> None:
    print("_"*len(map[0])*2)
    for row in map:
        print(*row)

def check_boundaries(dir:tuple) -> bool:
    y, x = find_self(indicator)
    y_dir, x_dir = dir
    
    return (y + y_dir) >= len(map) or (y + y_dir) < 0 or (x + x_dir) >= len(map[y]) or (x + x_dir) < 0

def count() -> int:
    total = 0
    for row in map:
        for col in row:
            if col == 'X':
                total += 1
    return total

def main():
    on_board = True
    direction = (-1, 0)
    while on_board:
        on_board = not check_boundaries(direction)
        if on_board: direction = move(direction)
        else: 
            y, x = find_self(indicator)
            map[y][x] = 'X'
    print(f"Part One: {count()}")

main()