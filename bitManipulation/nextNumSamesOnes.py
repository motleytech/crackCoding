'''Find the next and previous numbers which have the
same number of 1 bits in the binary representation'''

def nextNumSameOnes(n):
    '''returns next number'''
    if n <= 0:
        return 0
    seq = bin(n)[2:]
    seql = len(seq)
    c0 = 0

    while c0 < seql and seq[-c0-1] == '0':
        c0 += 1

    c1 = c0
    while c1 < seql and seq[-c1-1] == '1':
        c1 += 1

    print c0, c1, seql
    if c1 == seql:
        res = '1'
    else:
        res = seq[:-c1-1] + '1'

    res += '0'*(c0 + 1) + '1'*(c1 - c0 - 1)

    return res

def prevNumSameOnes(n):
    '''returns previous number'''
    if n <= 0:
        return 0

    np1 = n + 1
    if (np1 & n) == 0:
        return 0

    # find first 10...
    # count 1s before 0
    # count 0s before 1
    # change 10 to 01, move 1s to left and zeros to right
    c1 = 0
    seq = bin(n)[2:]
    seql = len(seq)
    while c1 < seql and seq[-c1-1] == '1':
        c1 += 1

    c0 = c1
    while c0 < seql and seq[-c0-1] == '0':
        c0 += 1

    print c1, c0, seql
    if c0 == seql - 1:
        res = '1'
    else:
        res = seq[:-c0-1] + '01'
    res = res + '1'*(c1) + '0'*(c0 - c1 - 1)

    return res



def test_nextNumSameOnes():
    '''test for next and prev methods'''
    n = 159
    print bin(n)[2:]
    res = nextNumSameOnes(n)
    print res

    print ''
    n = 0b110011
    print bin(n)[2:]
    res = prevNumSameOnes(n)
    print res

if __name__ == '__main__':
    test_nextNumSameOnes()
