'search in a rotated array'

def searchRotArray(arr, t):
    '''the modified binary search for a rotated array'''
    # first find the inflexion point
    st = 0
    end = len(arr) - 1
    if arr[0] > arr[end]:
        # its rotated... find inflexion
        left, right = 0, end

        while left < right:
            mid = (left + right + 1) / 2
            if arr[mid] >= arr[left]:
                left = mid
            else:
                right = mid - 1

        # left is at highest value
        if t > arr[0]:
            end = left
        else:
            st = left + 1

    # perform binary search using st, end
    while st < end:
        mid = (st + end) / 2
        if arr[mid] > t:
            st = mid + 1
        elif arr[mid] < t:
            end = mid - 1
        else:
            return mid
    return None


def test_searchRotArray():
    'Test for search rot array'
    inp = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]

    num = 5
    res = searchRotArray(inp, num)
    print res
    assert inp[res] == 5

    num = 2
    res = searchRotArray(inp, num)
    print res
    assert res == None

    print 'Test passed'


if __name__ == '__main__':
    test_searchRotArray()
