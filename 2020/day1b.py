from itertools import combinations
from math import prod

def part1(data):
    for combo in combinations(data, 2):
        if sum(combo) == 2020:
            return combo, prod(combo)

def part2(data):
    for combo in combinations(data, 3):
        if sum(combo) == 2020:
            return combo, prod(combo)

with open("1.input") as f:
    data = [int(x) for x in f.readlines()]

print(part1(data))
print(part2(data))
