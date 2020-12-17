from functools import reduce

with open("13.input") as f:
    timestamp = int(f.readline())
    bus_ids = f.readline().rstrip("\n")

#timestamp = 939
#bus_ids = "7,13,x,x,59,x,31,19"
#bus_ids = "1789,37,47,1889"

# Part 1
buses = [int(id) for id in bus_ids.split(",") if id != 'x']
bus = reduce(lambda a, b: a if a[1] < b[1] else b, [(id, (int((timestamp + id - 1) / id) * id)) for id in buses])
print(bus[0] * (bus[1] - timestamp))

# Part 2
buses = [(i, int(id)) for i, id in enumerate(bus_ids.split(",")) if id != 'x']
buses.sort(key=lambda a: a[1])
buses.reverse()
#print(buses)

def remainder(num, divisor):
    return num - divisor * (num // divisor)

ts = buses[0][1] - buses[0][0]
idx = 0
incr = 1
bus_count = len(buses)
while idx < bus_count:
    after, id = buses[idx]
    if after == 0:
        rem = 0
    else:
        rem = id * (int(after/id) + 1) - after
    #print(ts, incr, idx, buses[idx], rem)
    while True:
        r = remainder(ts, id)
        #print(f"\t\t{ts} {r}")
        if r == rem:
            break
        ts += incr
    #print(f"\tfound {ts} after {iters} iterations")
    incr *= id
    idx += 1
print(ts)
