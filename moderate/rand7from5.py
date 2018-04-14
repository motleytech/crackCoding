'''solution for the rand7 from rand5 problem'''

from random import randint

def rand5():
    'returns random int between 0 and 4 inclusive'
    return randint(0, 4)

def rand7():
    'returns random int between 0 and 6 inclusive'
    while True:
        value = 5*rand5() + rand5()
        if value < 21:
            return value % 7

def test():
    'test for rand7 method'
    from collections import defaultdict
    values = defaultdict(lambda: 0)
    for x in range(10000):
        values[rand7()] += 1

    for x, y in values.items():
        print x, y
        assert 1.0/8 <= float(y)/10000 <= 1.0/6

    print 'Passed'

if __name__ == '__main__':
    test()
