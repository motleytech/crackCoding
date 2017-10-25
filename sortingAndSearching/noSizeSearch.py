'binary search on a list where size of list is unknown'

class Listy(object):
    '''List class which returns -1 while accessing elements
    beyond the end'''
    def __init__(self, data):
        self.data = data

    def __getitem__(self, index):
        if len(self.data) > index:
            return self.data[index]
        return -1


def bsearch(arr, t, st, end):
    '''binary search which treats elements beyond the end as being larger'''
    while st <= end:
        mid = (st + end) / 2
        val = arr[mid]
        if val > t or val == -1:
            end = mid - 1
        elif val < t:
            st = mid + 1
        else:
            return mid
    return None

def noSizeSearch(arr, t):
    '''search for t in arr, where arr is sorted,
    but its size is unknown'''

    # first jump in powers of 2 and find a point beyond t
    # or the end
    scale = 0
    curr = arr[2**scale - 1]
    while curr < t and curr != -1:
        scale += 1
        curr = arr[2**scale - 1]

    if curr == t:
        return 2**scale - 1

    # now we are beyond t or beyond the end
    # we will use our custom binary search

    st = 2**(scale - 1) - 1
    end = 2**scale - 1
    return bsearch(arr, t, st, end)



def test_noSizeSearch():
    'test for noSizeSearch'
    ls = Listy(range(1, 200))

    res = noSizeSearch(ls, 200)
    assert res == None

    res = noSizeSearch(ls, 189)
    assert res == 188

    print 'Test Passed'

if __name__ == '__main__':
    test_noSizeSearch()
