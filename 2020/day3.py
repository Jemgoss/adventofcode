from math import prod

data = []
with open("day3.input") as f:
    for line in f:
        data.append(line.rstrip('\n'))

height = len(data)
width = len(data[0])

def count_trees(slope):
    x = y = 0
    tree_count = 0
    while True:
        x = (x + slope[0]) % width
        y += slope[1]
        if y >= height:
            break
        if data[y][x] == '#':
            tree_count += 1
    return tree_count

# Part 1
print(count_trees((3, 1)))

# Part 2
slopes = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2)
    ]

print(prod(map(count_trees, slopes)))
