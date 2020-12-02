with open("1.input") as f:
    data = [int(x) for x in f.readlines()]

# Part 1
for i, a in enumerate(data):
    b = next((e for e in data[i+1:] if e + a == 2020), None)
    if b:
        print(a, b, a * b)
        break

# Part 2
count = len(data)
for i in range(count):
    a = data[i]
    for j in range(i + 1, count):
        b = data[j]
        c = next((e for e in data[j+1:] if e + a + b == 2020), None)
        if c:
            print(a, b, c, a * b * c)
            exit(0)
