'solution for max contiguous sum problem'

def maxContiguousSum(seq):
    'finds the max sum for contiguous elements'
    maxSum = seq[0]
    currentSum = 0
    index = 0

    while index < len(seq):
        currentSum += seq[index]
        if currentSum > maxSum:
            maxSum = currentSum

        if currentSum <= 0:
            currentSum = 0
        index += 1
    return maxSum

def test():
    'test for maxContiguousSum method'
    data = [2, -8, 3, -2, 4, -10]
    assert maxContiguousSum(data) == 5

    data = [-1, 0, -2, -3, -4]
    assert maxContiguousSum(data) == 0

    data = [-2, -3, 4, -1, -2, 1, 5, -3]
    assert maxContiguousSum(data) == 7


    data = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    assert maxContiguousSum(data) == 6

    print 'done'

if __name__ == '__main__':
    test()
