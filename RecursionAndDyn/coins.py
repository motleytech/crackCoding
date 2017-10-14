coins = [1, 5, 10, 25]
lesserThan = {
    5: 1,
    10: 5,
    25: 10
}

def fways10(n, cache={}):
    if (n, 10) in cache:
        return cache[(n, 10)]
    w1 = 1
    w5 = n/5

    w10 = 0
    for x in range(1, n/10 + 1):
        rem = n - x*10
        w10 += 1 + rem/5
    res = w1 + w5 + w10
    cache[(n, 10)] = res
    return res


def fways25(n):
    cache = {}
    w25 = 0
    for y in range(0, n/25 + 1):
        rem = n - y*25
        w25 += fways10(rem, cache)
    return w25

for x in range(20, 50, 10):
    print x, fways10(x)


print fways25(100000)

