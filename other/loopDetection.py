from pprint import pprint as pp

def rngAlgo(seed):
    state = [seed]
    N = 4
    magic = 3197
    def nextNum():
        value = state[0] + magic
        value = int(str(value * value)[N/2:N+N/2])
        state[0] = value
        return value
    return nextNum


maxx, maxc = 0, 0
for x in range(500):
    rng = rngAlgo(x)

    visited = set()
    count = 0
    while 1:
        y = rng()
        count += 1
        if y in visited:
            print x, count
            if count > maxc:
                maxc = count
                maxx = x
            break
        visited.add(y)

print maxx, maxc

rng = rngAlgo(53)
values = [rng() for y in range(20)]
print values

