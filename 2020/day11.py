with open("day11.input") as f:
    data = [l.rstrip("\n") for l in f.readlines()]

# data = """L.LL.LL.LL
# LLLLLLL.LL
# L.L.L..L..
# LLLL.LL.LL
# L.LL.LL.LL
# L.LLLLL.LL
# ..L.L.....
# LLLLLLLLLL
# L.LLLLLL.L
# L.LLLLL.LL""".split("\n")

row_count = len(data)
row_length = len(data[0])

# Part 1
def adjacent_seats(seating, row, col):
    seats = 0
    for r in range(max(row - 1, 0), min(row + 2, row_count)):
        for c in range(max(col - 1, 0), min(col + 2, row_length)):
            if r != row or c != col:
                if seating[r][c] == '#':
                    seats += 1
    return seats

seating = [list(r) for r in data]
while True:
    next_seating = [r.copy() for r in seating]

    for r, row in enumerate(seating):
        for c, seat in enumerate(row):
            if seat != '.':
                adjacent = adjacent_seats(seating, r, c)
                if seat == 'L' and adjacent == 0:
                    next_seating[r][c] = '#'
                elif seat == '#' and adjacent >= 4:
                    next_seating[r][c] = 'L'

    if next_seating == seating:
        break
    seating = next_seating

print(sum(r.count('#') for r in seating))

# Part 2
def visible_occupied(seating, row, col, dir):
    while True:
        row += dir[0]
        col += dir[1]
        if row < 0 or row == row_count or col < 0 or col == row_length:
            return False
        if seating[row][col] != '.':
            break
    return seating[row][col] == '#'

seating = [list(r) for r in data]
dirs = ((0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1))

while True:
    next_seating = [r.copy() for r in seating]

    for r, row in enumerate(seating):
        for c, seat in enumerate(row):
            if seat != '.':
                visible_seats = sum(visible_occupied(seating, r, c, dir) for dir in dirs)
                if seat == 'L' and visible_seats == 0:
                    next_seating[r][c] = '#'
                elif seat == '#' and visible_seats >= 5:
                    next_seating[r][c] = 'L'

    if next_seating == seating:
        break
    seating = next_seating

print(sum(r.count('#') for r in seating))
