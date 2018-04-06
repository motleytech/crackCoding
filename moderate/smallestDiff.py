'''return pair of values which have smallest diff'''

def findMinDiffPair(sa, sb):
    'returns the pair with min difference between them'
    sa, sb = sorted(sa), sorted(sb)
    ia, ib = 0, 0
    lsa = len(sa)
    lsb = len(sb)
    cmin = abs(sa[ia] - sb[ib])
    gmin = cmin
    minPair = (sa[ia], sb[ib])
    while ia < lsa:
        cia = sa[ia]
        cmin = abs(cia - sb[ib])
        if cmin < gmin:
            gmin = cmin
            minPair = (cia, sb[ib])
        while True:
            if ib == lsb-1:
                break
            if abs(cia - sb[ib+1]) < cmin:
                cmin = abs(cia - sb[ib+1])
                if cmin < gmin:
                    minPair = (cia, sb[ib+1])
                    gmin = cmin
                ib += 1
            else:
                break
        ia += 1
    return minPair

def test():
    'tests for findMinDiffPair'
    da, db = [1, 3, 15, 11, 2], [23, 127, 235, 19, 8]
    assert findMinDiffPair(da, db) == (11, 8)

    da, db = [1, 3, 15, 234, 11, 2], [23, 127, 235, 19, 8]
    assert findMinDiffPair(da, db) == (234, 235)

    print 'done'

if __name__ == '__main__':
    test()
