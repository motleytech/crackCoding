'novel method returns the max of 2 values'

def retMax(a, b):
    'returns the max of a and b'
    ab = (a - b)
    # k == 0 if a > b else 1
    k = (ab & (1 << 63)) / (1 << 63)
    return k * b + (1 - k) * a

def test():
    'test for retMax method'
    assert retMax(3, 4) == 4
    assert retMax(-1, -2) == -1
    assert retMax(-41, 23) == 23
    assert retMax(5, 5) == 5
    assert retMax(0, 20) == 20
    assert retMax(-5, 0) == 0
    assert retMax(0, 0) == 0
    print 'Done'

if __name__ == '__main__':
    test()
