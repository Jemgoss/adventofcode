from itertools import filterfalse
from functools import reduce
import re

with open("day16.input") as f:
    data = f.read()

# data = """class: 1-3 or 5-7
# row: 6-11 or 33-44
# seat: 13-40 or 45-50
#
# your ticket:
# 7,1,14
#
# nearby tickets:
# 7,3,47
# 40,4,50
# 55,2,20
# 38,6,12"""

# data = """class: 0-1 or 4-19
# row: 0-5 or 8-19
# seat: 0-13 or 16-19
#
# your ticket:
# 11,12,13
#
# nearby tickets:
# 3,9,18
# 15,1,5
# 5,14,9"""

field_data, your_ticket, nearby = data.split("\n\n")

pat = re.compile("^([^:]+): ([0-9]+)-([0-9]+) or ([0-9]+)-([0-9]+)$")
fields = [(g[0], int(g[1]), int(g[2]), int(g[3]), int(g[4])) for g in [pat.match(line).groups() for line in field_data.split("\n")]]

my_ticket = list(map(int, your_ticket.strip("your ticket:\n").split(",")))

nearby_tickets = [list(map(int, nums.split(","))) for nums in nearby.strip("nearby tickets:\n").split("\n")]

def field_valid_for_num(field, num):
    return field[1] <= num <= field[2] or field[3] <= num <= field[4]

def fields_valid_for_num(fields, num):
    return map(lambda field: field_valid_for_num(field, num), fields)

# Part 1
print(sum(map(lambda nums: sum(filterfalse(lambda num: any(fields_valid_for_num(fields, num)), nums)), nearby_tickets)))

# # Part 2
valid_tickets = list(filter(lambda nums: all(map(lambda num: any(fields_valid_for_num(fields, num)), nums)), nearby_tickets))
valid_tickets.append(my_ticket)

# print(fields)
# print(valid_tickets)

field_count = len(fields)
invalid_sets = [(i, set()) for i in range(field_count)]
for nums in valid_tickets:
    for i, num in enumerate(nums):
        for j, field in enumerate(fields):
            if not field_valid_for_num(field, num):
                invalid_sets[j][1].add(i)

invalid_sets.sort(key=lambda x: len(x[1]))
invalid_sets.reverse()

remaining_fields = set(range(field_count))
ordered_fields = [None] * field_count
for idx, s in invalid_sets:
    valid_fields = remaining_fields.difference(s)
    if len(valid_fields) != 1:
        raise Exception("Should only be 1 valid field!")
    field = valid_fields.pop()
    ordered_fields[field] = idx
    remaining_fields.remove(field)
prod = 1
for idx, val in enumerate(my_ticket):
    field_name = fields[ordered_fields[idx]][0]
    #print(f"{field_name} = {val}")
    if field_name.startswith("departure"):
        prod *= val
print(prod)
