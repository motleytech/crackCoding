'find the majority element in an array'

def getMajority(arr):
    'returns the majority element (if there is one, else return -1)'
    num, count, count2 = 0, 0, 0

    for x in arr:
        if count == 0:
            num = x
            count += 1
            continue
        if num == x:
            count += 1
        else:
            count -= 1
    for x in arr:
        if x == num:
            count2 += 1

    if count2 <= len(arr) / 2:
        return -1
    return num

def test():
    'test for getMajority method'
    arr = [1, 2, 5, 9, 5, 9, 5, 5, 5]
    assert getMajority(arr) == 5

    assert getMajority([1, 2, 3, 4, 5]) == -1
    assert getMajority([1, 2, 2, 1]) == -1
    assert getMajority([1, 2, 2, 2, 1]) == 2

    print 'Passed'

if __name__ == '__main__':
    test()
