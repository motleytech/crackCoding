

def findMagicIndex2(arr):
    'find i s.t. i == arr[i] (possible repeated elements)'
    def bisect(arr, st, end):
        'modified binary search'
        if st > end:
            return False, None
        mid = (st + end) / 2
        if arr[mid] == mid:
            return True, mid
        res, mindex = bisect(arr, st, min(mid-1, arr[mid]))
        if res:
            return res, mindex
        res, mindex = bisect(arr, max(mid+1, arr[mid]), end)
        if res:
            return res, mindex
        return False, None

    res, index = bisect(arr, 0, len(arr) - 1)
    return index


def findMagicIndex1(arr):
    'find i s.t. i == arr[i] (unique sorted elements)'
    def bisect(arr, st, end):
        'binary search'
        if st > end:
            return False, None
        mid = (st + end) / 2
        if arr[mid] == mid:
            return True, mid
        if arr[mid] < mid:
            return bisect(arr, mid+1, end)
        return bisect(arr, st, mid-1)

    res, index = bisect(arr, 0, len(arr) - 1)
    return index


def test_findMagicIndex1():
    'test using unique elements'
    from random import randint
    N = 40
    M = 40
    items = sorted(set([randint(-M/2, M) for x in range(N)]))
    mindex1 = findMagicIndex1(items)
    mindex2 = findMagicIndex2(items)

    assert mindex1 == mindex2


    if mindex1 is not None:
        print 'Found %s' % mindex1
        assert items[mindex1] == mindex1

    else:
        print 'Not Found'
        for i, x in enumerate(items):
            assert x != i
    print 'Test 1 Passed'


def test_findMagicIndex2():
    'test using duplicate elements'
    from random import randint
    N = 50
    M = 50
    items = sorted([randint(-M/2, M) for x in range(N)])
    mindex2 = findMagicIndex2(items)

    if mindex2 is not None:
        print 'Found %s' % mindex2
        assert items[mindex2] == mindex2
    else:
        print 'Not Found'
        #print list(enumerate(items))
        for i, x in enumerate(items):
            try:
                assert x != i
            except:
                print 'Error: %s, %s' % (x, i)
                print items
                print 'Test 2 Failed'
                return

    print 'Test 2 Passed'



if __name__ == '__main__':
    test_findMagicIndex1()
    test_findMagicIndex2()
    # # 170, #204, #240, #286, #340
    # x,x | x+2,x+1
    # x,x | x,x+1 | x,x+2
    # x,x |
