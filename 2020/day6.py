with open("day6.input") as f:
    data = f.read().rstrip('\n').split("\n\n")

# Part 1
print(sum([len(set(list(group.replace("\n", "")))) for group in data]))

# Part 2
print(sum([len(set.intersection(*[set(list(g)) for g in group.split("\n")])) for group in data]))
