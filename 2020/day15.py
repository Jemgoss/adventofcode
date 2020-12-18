with open("day15.input") as f:
    data = [int(x) for x in f.readline().rstrip().split(",")]

#data = [0,3,6]

# Part 1

def run_sequence(data, turns):
    positions = dict()
    for turn, num in enumerate(data, start = 1):
        positions[num] = turn

    prev = None
    while turn != turns:
        if prev:
            num = turn - prev
        else:
            num = 0
        prev = positions.get(num)
        turn += 1
        positions[num] = turn

    return num

print(run_sequence(data, 2020))

# Part 2

print(run_sequence(data, 30000000))
