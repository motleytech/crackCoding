'''implementation of radix sort for integers'''

def radixSort(arr, radix=10):
    '''radix sort method'''
    shift = 1

    buckets = [[] for _ in range(radix)]
    done = False
    while not done:
        done = True

        for x in arr:
            val = (x / shift) % radix
            buckets[val].append(x)
            if val > 0:
                done = False

        index = 0
        for i, bucket in enumerate(buckets):
            for x in bucket:
                arr[index] = x
                index += 1
            buckets[i] = []
        shift *= radix
    return arr

def test_radixSort():
    'test for radixSort'
    from random import randint

    inp = [randint(0, 100) for _ in range(20)]

    sinp = sorted(inp)
    assert sinp == radixSort(inp)
    print 'Test passed'

if __name__ == '__main__':
    test_radixSort()
