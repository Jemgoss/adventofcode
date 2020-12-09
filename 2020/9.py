from itertools import combinations

with open("9.input") as f:
    data = [int(l) for l in f.readlines()]

# Part 1
pos = 0
found = True
while found:
    val = data[pos + 25]
    found = False
    for combo in combinations(data[pos : pos + 25], 2):
        if sum(combo) == val:
            found = True
            break
    pos += 1
print(val)

# Part 2
pos = 0
while True:
    sum = 0
    end = pos
    while sum < val:
        sum += data[end]
        end += 1
    if sum == val:
        range = data[pos : end]
        print(min(range) + max(range))
        break
    pos += 1
