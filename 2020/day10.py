from collections import Counter

with open("day10.input") as f:
    data = map(int, f.readlines())

# data = [int(l) for l in """16
# 10
# 15
# 5
# 1
# 11
# 7
# 19
# 6
# 12
# 4""".split("\n")]

# data = [int(l) for l in """28
# 33
# 18
# 42
# 31
# 14
# 46
# 20
# 48
# 47
# 24
# 23
# 49
# 45
# 19
# 38
# 39
# 11
# 1
# 32
# 25
# 35
# 8
# 17
# 7
# 9
# 4
# 2
# 34
# 10
# 3""".split("\n")]

seq = sorted(data)

# Part 1
counter = Counter(b - a for a, b in zip([0] + seq, seq))
print(counter[1] * (counter[3] + 1))

# Part 2
counter = Counter({0: 1})
for x in seq:
    counter[x] = sum(counter[i] for i in range(x - 3, x))
print(counter[seq[-1]])
