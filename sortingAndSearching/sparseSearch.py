'implementation of sparse search method'

def bSparseSearch(arr, t):
    '''modified binary search for conducting sparse search
    in an array containing empty strings'''
    st, end = 0, len(arr) - 1

    while st <= end:
        mid = (st + end) / 2
        while mid <= end and arr[mid] == '':
            mid += 1
        if mid > end:
            mid = (st + end) / 2 - 1
            end = mid
            while mid >= st and arr[mid] == '':
                mid -= 1
            if mid < st:
                return None
            else:
                if arr[mid] < t:
                    return None
                elif arr[mid] > t:
                    end = mid - 1
                else:
                    return mid
        else:
            if arr[mid] < t:
                st = mid + 1
            elif arr[mid] > t:
                end = mid - 1
            else:
                return mid
    return None


def test_bSparseSearch():
    'test for bSparseSearch method'
    inp = ['at', '', '', '', '', 'ball', '', '', '', 'car', '',
           '', '', '', '', '', 'dad', '', '', '', '', '']

    for x in ['at', 'ball', 'car', 'dad', 'cat']:
        res = bSparseSearch(inp, x)
        print res, (inp[res] if res is not None else x)
        if x in inp:
            assert x == inp[res]

    print 'Test Passed'


if __name__ == '__main__':
    test_bSparseSearch()
