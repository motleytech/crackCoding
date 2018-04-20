'solution for the Missing Two problem'

import math

def findMissingTwo(data):
    'finds and returns the two missing numbers from the input'
    N = len(data) + 2
    x = N*(N+1)/2 - sum(data)
    y = math.factorial(N) / reduce(lambda a, b: a*b, data, 1)

    a = (x - math.sqrt(x*x - 4*y)) / 2.0
    b = (x + math.sqrt(x*x - 4*y)) / 2.0

    return (a, b)

def test():
    'test for findMissingTwo method'
    from random import randint
    N = randint(10, 25)
    data = range(1, N+1)

    r1, r2 = randint(1, N), randint(1, N)
    while r2 == r1:
        r2 = randint(1, N)
    r1, r2 = sorted((r1, r2))

    data.remove(r1)
    data.remove(r2)

    res = findMissingTwo(data)
    assert res == (r1, r2)

if __name__ == '__main__':
    test()
    print 'Passed'
