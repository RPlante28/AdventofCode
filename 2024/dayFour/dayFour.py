# NOT COMPLETE -> NEED TO FINISH P2
import os

filepath = os.path.join(os.path.dirname(__file__), 'data.txt')

def unpack(file:str) -> list:
    with open(file, 'r') as reader:
        return reader.read().splitlines()

def check_str(input:str, target:str, type:str) -> int:
    return int(input == target or input[::-1] == target)

def check_range(file:list, target, row:int, col:int) -> int:
    """
    checks all surrounding possible combinations to see if there are any matching words

    """

    ans = 0
    size = len(target)
    string = ""

    right_bound = col + size > len(file[row])
    lower_bound = row + size > len(file)
    left_bound = col < size - 1

    # check diag left -> right
    if not lower_bound:
        if not right_bound:
            string = ""
            for i in range(size):
                string += file[row + i][col + i]
            ans += check_str(string, target, 'lr_diag')

        # check diag right -> left
        if not left_bound:
            string = ""
            for j in range(size):
                string += file[row + j][col - j]
            ans += check_str(string, target, 'rl_diag')

        # check down
        string = ""
        for r in range(size):
            string += file[row + r][col]
        ans += check_str(string, target, 'down')


    # check left -> right
    if not(right_bound):
        string = ""
        for c in range(size):
            string += file[row][col + c]
        ans += check_str(string, target, 'l_r')

    return ans

def check_cross() -> bool:
    """Checks middle char to see if there is matching cross"""
    ans = False

    return ans

def part_one(file:str, target:str) -> None:
    # main function
    data = unpack(file)
    ans = 0

    for line in range(len(data)):
        for char in range(len(data[line])):
            ans += check_range(data, target, line, char)
    
    print(ans)

def part_two(file:str, target:str) -> None:
    # part two
    data = unpack(file)
    ans = 0

    for line in range(len(data)):
        for char in range(len(data[line])):
            ans += check_range(data, target, line, char)

    print(ans)

part_one(filepath, "XMAS")
part_two(filepath, "MAS")