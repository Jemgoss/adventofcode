from functools import reduce

with open("day5.input") as f:
    data = [l.rstrip("\n") for l in f.readlines()]

# Part 1
def decode(acc, pos):
    return (acc[0] + (acc[1] if pos == acc[2] else 0), acc[1] >> 1, acc[2])

def seat_no(assignment):
    return reduce(decode, assignment[:7], (0, 64, 'B'))[0] * 8 + \
           reduce(decode, assignment[7:], (0, 4, 'R'))[0]

max_seat_no = max([seat_no(assignment) for assignment in data])
print(max_seat_no)

# Part 2
seating = set(range(0, max_seat_no + 1))
def remove_seat(seating, assignment):
    seating.remove(seat_no(assignment))
    return seating

remaining = reduce(remove_seat, data, seating)
my_seat = remaining - set(range(0, len(remaining))) # Remove consecutive seats from the beginning.
print(my_seat.pop())
