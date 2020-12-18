import math

with open("day12.input") as f:
    data = f.readlines()

# data = """F10
# N3
# F7
# R90
# F11""".split("\n")

# Part 1
dir = [1, 0]
rad = 0
pos = [0, 0]

for line in data:
    i = line[0]
    val = int(line[1:])
    #print(pos, dir, i, val)
    if i == 'F':
        pos[0] += dir[0] * val
        pos[1] += dir[1] * val
    elif i == 'N':
        pos[1] += val
    elif i == 'S':
        pos[1] -= val
    elif i == 'E':
        pos[0] += val
    elif i == 'W':
        pos[0] -= val
    else:
        if i == 'L':
            rad += math.radians(val)
        elif i == 'R':
            rad -= math.radians(val)
        dir[0] = int(math.cos(rad))
        dir[1] = int(math.sin(rad))
print(pos, abs(pos[0]) + abs(pos[1]))

# Part 2
pos = [0, 0]
way = [10, 1]

for line in data:
    i = line[0]
    val = int(line[1:])
    #print(pos, way, i, val)
    if i == 'F':
        pos[0] += way[0] * val
        pos[1] += way[1] * val
    elif i == 'N':
        way[1] += val
    elif i == 'S':
        way[1] -= val
    elif i == 'E':
        way[0] += val
    elif i == 'W':
        way[0] -= val
    else:
        if i == 'L':
            rad = math.radians(val)
        elif i == 'R':
            rad = math.radians(-val)
        # rotation trans: (x * cos(T) - y * sin(T), x * sin(T) + y * cos(T))
        x = way[0] * int(math.cos(rad)) - way[1] * int(math.sin(rad))
        y = way[0] * int(math.sin(rad)) + way[1] * int(math.cos(rad))
        way[0] = x
        way[1] = y
print(pos, abs(pos[0]) + abs(pos[1]))
