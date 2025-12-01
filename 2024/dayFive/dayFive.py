import os

filepath = os.path.join(os.path.dirname(__file__), 'data.txt')

# unpack file
with open(filepath, 'r') as r:
    file = r.read().split("\n\n")
    rules = []
    updates = []

    for rule in file[0].split("\n"):
        rules.append(rule.split('|'))

    for update in file[1].split("\n"):
        updates.append([int(entry) for entry in update.split(',')])
    
reqs = {}
working = []
partOne = 0
partTwo = 0
isVal = True
# list of update -> violations
incorrect_updates = {}
# depend comes before req
# [[dep, req]]
violations = []


def check_valid(input:list) -> list:
    """returns list of violations"""
    violations = []
    for depnum in range(len(input)):
        for reqnum in range(len(input)):
            if input[depnum] in reqs and input[reqnum] in reqs[input[depnum]]:
                if reqnum > depnum:
                    violation = [depnum, reqnum]
                    violations.append(violation)
    return violations 

def fix_val(input:list, violations:list, pass_list:list = []) -> list:
    # swap indecies till work?
    ans = pass_list
    tempList = input
    temp = None
    for violation in violations:
        temp = tempList[violation[0]]
        tempList[violation[0]] = tempList[violation[1]]
        tempList[violation[1]] = temp
    test_vil = check_valid(input)
    if len(test_vil) == 0:
        ans.append(tempList)
    else:
        fix_val(tempList, test_vil, ans)
    return ans
    

# set up what pages require what
for rule in rules:
    det = int(rule[0])
    dep = int(rule[1])
    if dep not in reqs:
        reqs[dep] = []
    reqs[dep].append(det)

# go through all entries in each update
for update in updates:
    working = []
    for entry in update:
        working.append(entry)
    violations = check_valid(working)
    if len(violations) > 0:
        incorrect_updates[str(working)] = violations
    else:
        partOne += working[len(working)//2]

# go through all incorrect updates and reorder to fix
for inc_up, viol in incorrect_updates.items():
    # convert key back to list
    inc_no_brack = inc_up.strip("[]").split(',')
    inc_up = [int(item.strip()) for item in inc_no_brack]
    fixed = fix_val(inc_up, viol)

for item in fixed:
    partTwo += item[len(item) // 2]
 
print(f"Part One: {partOne}")
print(f"Part Two: {partTwo}")