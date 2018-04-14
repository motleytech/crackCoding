'solution to the "add without plus" problem'

def sumB(x, y, c, p):
    'add using bit operations'
    x1, y1 = 1 & (x >> p), 1 & (y >> p)
    s = x1 ^ y1 ^ c
    c = (x1 & y1) | (x1 & c) | (y1 & c)
    return s << p, c


def add(a, b):
    'add without using +'
    res = 0
    p = 0
    c = 0

    while p < 32:
        s, c = sumB(a, b, c, p)
        res |= s
        p += 1

    return res

def test():
    assert add(17, 39) == 56
    assert add(2837, 382748) == 385585
    print 'Passed'

if __name__ == '__main__':
    test()



