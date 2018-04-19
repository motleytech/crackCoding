'solution to the masseuse problem'

cache = {}

def getMaxBusyTime(inp, p=0):
    'recursively finds the max time that the masseuse can be busy'
    if p in cache:
        return p
    o1, o2, o3 = inp[p], inp[p], 0
    if p < len(inp) - 2:
        o1 += getMaxBusyTime(inp, p+2)
    if p < len(inp) - 3:
        o2 += getMaxBusyTime(inp, p+3)
    if p < len(inp) - 1:
        o3 = getMaxBusyTime(inp, p+1)
    cache[p] = max(o1, o2, o3)
    return cache[p]

def test():
    'test for getMaxBusyTime method'
    inp = [30, 15, 60, 75, 45, 15, 15, 45]

    assert getMaxBusyTime(inp) == 180
    print 'Passed'

if __name__ == '__main__':
    test()
