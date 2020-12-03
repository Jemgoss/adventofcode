from math import prod

data = []
with open("3.input") as f:
    for line in f:
        data.append(line.rstrip('\n'))

# Part 1
height = len(data)
width = len(data[0])
x = y = 0
tree_count = 0
while True:
    x = (x + 3) % width
    y += 1
    if y >= height:
        break
    if data[y][x] == '#':
        tree_count += 1
print(tree_count)

# Part 2
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

slopes = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2)
    ]

print(prod(map(count_trees, slopes)))
