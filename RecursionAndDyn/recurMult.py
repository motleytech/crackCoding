'''multiply 2 numbers without using * (using add, sub, shift, etc)'''

def recurMul(a, b):
    'returns a*b without actually using *'
    result = 0
    bb = list(reversed('0' + bin(b)[2:]))

    lbb = len(bb) - 1
    cindex = 0
    result = 0
    while cindex <= lbb:
        x = bb[cindex]
        if x == '0':
            cindex += 1
            continue

        y = bb[cindex+1]
        if x == '1' and y == '0':
            result += (a << cindex)
            cindex += 2
            continue

        yindex = cindex + 2
        while bb[yindex] == '1':
            yindex += 1
        result += (a << yindex) - (a << cindex)
        cindex = yindex + 1

    return result

def test_recurMul():
    'test for recurMul method'
    from random import randint

    for _ in range(50):
        a, b = randint(11, 99), randint(11, 99)

        assert recurMul(a, b) == a*b
    print 'Test passed.'

if __name__ == '__main__':
    test_recurMul()

