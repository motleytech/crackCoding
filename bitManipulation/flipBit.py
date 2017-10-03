
'''find the maximum 1 bit seq formed by flipping a single
0 bit in the given binary number'''

def flipBit4LongSeq(n):
    'finds longest seq after flipping one 0 bit'
    if n == 0:
        return 1
    seq = bin(n)[2:]
    print seq
    seq = seq.split('0')
    if len(seq) == 1:
        return len(seq) + 1

    maxLen = 0
    for x, y in zip(seq, seq[1:]):
        clen = len(x) + len(y) + 1
        if clen > maxLen:
            maxLen = clen
    return maxLen


def test_flipBit4LongSeq():
    'test for the flipBit4LongSeq method'
    n = 1775
    res = flipBit4LongSeq(n)
    assert res == 8
    print 'Test passed'

    n = 359975
    res = flipBit4LongSeq(n)
    print res
    assert res == 8

if __name__ == '__main__':
    test_flipBit4LongSeq()
    print 'done'


