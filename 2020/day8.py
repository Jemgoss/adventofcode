with open("day8.input") as f:
    data = [l.rstrip("\n") for l in f.readlines()]

# Test data
# data = """nop +0
# acc +1
# jmp +4
# acc +3
# jmp -3
# acc -99
# acc +1
# jmp -4
# acc +6""".split("\n")

# Part 1
def run_program(program):
    acc = pc = 0
    end = len(program)
    try:
        while pc < end:
            ins, x = program[pc]
            program[pc] = None # cannot revisit!
            if ins == "jmp":
                pc += int(x)
            else:
                if ins == "acc":
                    acc += int(x)
                pc += 1
    except:
        raise Exception("Program failed", (pc, acc))
    return acc

try:
    run_program([l.split(" ") for l in data])
except Exception as e:
    print(e.args[1][1])

# Part 2
def fixed_up_programs(program):
    swaps = ("nop", "jmp")
    for line in program:
        op = line[0]
        if op in swaps:
            line[0] = swaps[1 - swaps.index(op)]
            yield program
            line[0] = op

for program in fixed_up_programs([l.split(" ") for l in data]):
    try:
        print(run_program(list(program)))
        break
    except:
        pass
