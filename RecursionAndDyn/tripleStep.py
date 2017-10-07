'''Count ways to get to nth step, given child can
take 1, 2 or 3 steps at a time'''

# let f(n) be the ways to get to step n, then
# f(n) = f(n-1) + f(n-2) + f(n-3)

def tripleStep(n):
    'return number of ways to get to nth step'
    if 1 <= n <= 3:
        return n

    a, b, c = 1, 2, 3
    n = n-3
    while n > 0:
        n -= 1
        a, b, c = b, c, (a + b + c)
    return c

def test_tripleStep():
    'test for tripleStep method'
    for x in range(1, 20):
        res = tripleStep(x)
        print x, res

if __name__ == '__main__':
    test_tripleStep()
