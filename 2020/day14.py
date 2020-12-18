from functools import reduce

with open("day14.input") as f:
    data = [l.rstrip("\n") for l in f.readlines()]

# data = """mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
# mem[8] = 11
# mem[7] = 101
# mem[8] = 0""".split("\n")

# data = """mask = 000000000000000000000000000000X1001X
# mem[42] = 100
# mask = 00000000000000000000000000000000X0XX
# mem[26] = 1""".split("\n")

program = [l.split(" = ") for l in data]

# Part 1

regs = dict()
for ins in program:
    if ins[0] == 'mask':
        mask = ins[1]
        and_mask = int(mask.replace('X', '1'), 2)
        or_mask = int(mask.replace('X', '0'), 2)
    else:
        addr = int(ins[0][4:-1])
        val = int(ins[1])
        regs[addr] = (val & and_mask) | or_mask

print(sum(regs.values()))

# Part 2

def red(acc, x):
    if x[1] == 'X':
        acc.append(x[0])
    return acc

regs = dict()
for ins in program:
    if ins[0] == 'mask':
        mask = ins[1]
        and_mask = int(mask.replace('0', '1').replace('X', '0'), 2)
        or_mask = int(mask.replace('X', '0'), 2)
        xes = reduce(red, enumerate(reversed(mask)), [])
    else:
        addr = (int(ins[0][4:-1]) & and_mask) | or_mask
        val = int(ins[1])
        for i in range(2 ** len(xes)):
            apply_mask = 0
            for j, pos in enumerate(xes):
                shifted = (1 << j)
                if i & shifted:
                    apply_mask |= (1 << pos)
            regs[addr | apply_mask] = val

print(sum(regs.values()))
