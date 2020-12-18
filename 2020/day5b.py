with open("5.input") as f:
    data = [l.rstrip("\n") for l in f.readlines()]

# Part 1
def seat_no(code):
    return int(code.replace('B', '1').replace('R', '1').replace('L', '0').replace('F', '0'), 2)

max_seat_no = max([seat_no(assignment) for assignment in data])
print(max_seat_no)

# Part 2
seating = set(range(0, max_seat_no + 1))
seating.difference_update([seat_no(assignment) for assignment in data])
print(seating.pop())
