"""solution to the bit insertion problem"""

def bitInsert(N, M, i, j):
    """Insert M into N between positions i and j (j > i)"""

    # create a bitstring with 1s between positions i and j
    mask = 0
    for x in range(i, j+1):
        mask |= (1 << x)

    # clear N between ith and jth bit
    N = N & (~mask)
    # shift M to position i and insert into N
    return N | (M << i)

def test_bitInsert():
    '''test for bitInsert method'''
    N = 0b10000000000
    M = 0b10011
    i = 2
    j = 6

    assert bitInsert(N, M, i, j) == 0b10001001100
    print 'Test Passed'

if __name__ == '__main__':
    test_bitInsert()
    print 'done'
