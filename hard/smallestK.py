'adding solution for smallest k problem'

from random import randint, shuffle

def partition(arr, a, b):
    'parition the arr between position a, b using pivot=arr[a]'
    pivot = arr[a]
    p1, p2 = a+1, b
    while p2 >= p1:
        if arr[p2] < pivot:
            arr[p1], arr[p2] = arr[p2], arr[p1]
            p1 += 1
        else:
            p2 -= 1
    arr[p2], arr[a] = arr[a], arr[p2]
    return p2

def getSmallestK(arr, k):
    'return the smallest k elements in arr'
    st = 0
    end = len(arr) - 1
    pPos = None
    while pPos not in (k-1, k):
        pivot = randint(st, end)
        arr[st], arr[pivot] = arr[pivot], arr[st]
        pPos = partition(arr, st, end)
        if pPos > k:
            end = pPos - 1
        elif pPos < k-1:
            st = pPos + 1
        else:
            break
    return arr[:k]

def test():
    'test for getSmallestK method'
    data = range(20)
    for x in range(1, 20):
        shuffle(data)
        assert sorted(getSmallestK(data, x)) == range(x)
    print 'Passed'

if __name__ == '__main__':
    test()
