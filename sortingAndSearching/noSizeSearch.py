'binary search on a list where size of list is unknown'

class Listy(object):
    def __init__(self, data):
        self.data = data

    def __getitem__(self, index):
        if len(self.data) > index:
            return self.data[index]
        return -1


def bsearch(arr, t, st, end):
    while st < end:
        mid = (st + end) / 2
        if arr[mid] > t or arr[mid] == -1:
            end = mid - 1
        elif arr[mid] < t:
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

    st = 2**(scale - 1) - 1
    end = 2**scale - 1
    return bsearch(arr, t, st, end)



def test_noSizeSearch():
    ls = Listy(range(1, 200))

    res = noSizeSearch(ls, 200)
    assert res == None

    res = noSizeSearch(ls, 189)
    assert res == 188

    print 'Test Passed'

if __name__ == '__main__':
    test_noSizeSearch()
