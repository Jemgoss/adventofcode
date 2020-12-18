import re

with open("day2.input") as f:
    data = f.readlines()

# "7-10 m: qmpgmmsmmmmkmmkj"
pat = re.compile("^([0-9]+)-([0-9]+) (\S): (.*)$")

# Part 1
valid_count = 0
for line in data:
    m = pat.match(line)
    if not m:
        raise Exception("Bad match", line)
    occurrences = m.group(4).count(m.group(3))
    if int(m.group(1)) <= occurrences <= int(m.group(2)):
         valid_count += 1
print(valid_count)

# Part 2
valid_count = 0
for line in data:
    m = pat.match(line)
    if not m:
        raise Exception("Bad match", line)
    p1, p2, ch, pw = int(m.group(1)), int(m.group(2)), m.group(3), m.group(4)
    if (pw[p1 - 1] == ch) != (pw[p2 - 1] == ch):
        valid_count += 1
print(valid_count)
