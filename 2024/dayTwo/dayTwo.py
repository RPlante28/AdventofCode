import os

file_name = os.path.join(os.path.dirname(__file__), 'data.txt')

def unpack(file):
    with open(file, 'r') as reader:
        for block in reader.read().split("\n\n"):
            return list(map(lambda val: list(map(int, val.split())), block.splitlines()))

data = unpack(file_name)

def valid_asc(nums: list[int]) -> bool:
    return all(1 <= b - a <= 3 for a, b in zip(nums, nums[1:]))

def valid_desc(nums: list[int]) -> bool:
    return all(1 <= a - b <= 3 for a, b in zip(nums, nums[1:]))

def is_valid(data) -> int:
    numSafe = 0
    for line in data:
        if valid_asc(line) or valid_desc(line):
            numSafe += 1
    return numSafe  

print(is_valid(data))

# part two - problem dampener
# if you can remove one level to fix report, then it can be considered safe

def is_valid_damp(data) -> int:
    numSafeDamp = 0
    for line in data:
        variations = [line[:i] + line[i + 1:] for i, _ in enumerate(line)]
        counted = 0
        for var in variations:
            if (valid_asc(var) or valid_desc(var)) and counted == 0:
                counted += 1
                numSafeDamp += 1
    return numSafeDamp

print(is_valid_damp(data))

