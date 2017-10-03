"""convert float between (0, 1) into binary string of 32 chars"""

def binaryToString(num):
    """returns string of binary representation of float num (0 < num < 1),
    if it fits in 32 bits, else returns ERROR"""
    result = []
    for _ in range(32):
        num = num * 2
        result.append(int(num))
        num = num - int(num)
        if num == 0:
            break
    else:
        if num != 0:
            return 'ERROR'
    return ''.join(str(x) for x in result)

def test_binToString():
    '''test for binaryToString'''
    res = binaryToString(0.72)
    assert res == 'ERROR'

    res = binaryToString(0.8125)
    assert res == '1101'

    print 'Test passed'

if __name__ == '__main__':
    test_binToString()

