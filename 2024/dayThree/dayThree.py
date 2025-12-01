import os
import re

filepath = os.path.join(os.path.dirname(__file__), 'data.txt')
pattern = r"(mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\))"

def unpack(file):
    count = 0
    with open(file, 'r') as reader:
        return re.split(pattern, reader.read())

def get_valid(array:list) -> list:
    valid_arr = []
    for chunk in array:
        if chunk is not None:
            match = re.search(pattern, chunk)
            if match:
                valid_arr.append(chunk)
    return valid_arr

def mul(num1:int, num2:int) -> int:
    return num1 * num2

def calc_all(array:list, part2:bool = False) -> int:
    sum = 0
    fin_arr = []
    do_arr = []
    dont_arr = []
    do = True
    for val in array:
        if val == "don't()":
            do = False
        elif val == "do()":
            do = True

        if (do or not part2) and 'mul' in val:
            do_arr.append(val)
        elif not do and 'mul' in val:
            dont_arr.append(val)
    fin_arr = [op for op in do_arr if op not in dont_arr]
    for op in fin_arr:
        sum += eval(op)
    return sum

data = unpack(filepath)
valid_data = get_valid(data)
# if calculating for part 2, run calc_all(valid_data, True)
print(calc_all(valid_data, True))
