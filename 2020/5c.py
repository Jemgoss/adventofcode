with open("5.input") as f:
    data = [l.rstrip("\n") for l in f.readlines()]

# Part 1
def seat_numbers(codes):
    for code in codes:
        yield int(code.replace('B', '1').replace('R', '1').replace('L', '0').replace('F', '0'), 2)

max_seat_no = max(seat_numbers(data))
print(max_seat_no)

# Part 2
min_seat_no = min(seat_numbers(data))
seating = set(range(min_seat_no, max_seat_no))
seating.difference_update(seat_numbers(data))
print(seating.pop())
