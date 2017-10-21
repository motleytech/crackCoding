'implementation of sorted merge'

def sortedMerge(a, b):
    '''method to merge 2 sorted arrays a,b
    a must have enough space to fit b at the end'''
    na, nb = len(a), len(b)

    # assume last nb elements of a are empty
    curr, la, lb = na - 1, na - nb - 1, nb - 1

    while lb >= 0 and la >= 0:
        if b[lb] >= a[la]:
            a[curr] = b[lb]
            curr -= 1
            lb -= 1
        else:
            a[curr] = a[la]
            curr -= 1
            la -= 1

    while lb >= 0:
        a[curr] = b[lb]
        curr -= 1
        lb -= 1
    return a

def test_sortedMerge():
    'test for sorted merge'
    ta = range(10) + range(20, 30)
    tb = range(-12, -8)
    oldta = ta[:]
    ta += [0]*len(tb)

    sortedMerge(ta, tb)
    assert sorted(ta) == ta

    for x in oldta:
        assert x in ta
    for x in tb:
        assert x in ta

    print 'Test passed.'

if __name__ == '__main__':
    test_sortedMerge()




