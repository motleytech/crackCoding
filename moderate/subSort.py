'solution to the subsort problem'

def subSort(seq):
    'returns the starting and ending indices of sub seq that requires sorting'
    # find dip from left and rise from right
    index = 0
    try:
        while seq[index] <= seq[index+1]:
            index += 1
    except IndexError:
        return 0, 0
    left = index

    index = len(seq) - 1
    try:
        while seq[index - 1] <= seq[index]:
            index -= 1
    except IndexError:
        return 0, 0
    right = index

    # find min element to right of left
    minRofL = seq[left]
    index = left + 1
    while index < len(seq):
        if seq[index] < minRofL:
            minRofL = seq[index]
        index += 1
    # find first element just more than minRofL starting from left

    index = 0
    while seq[index] <= minRofL:
        index += 1

    leftBound = index

    # find max element to the left of right
    maxLofR = seq[right]
    index = right - 1
    while index >= 0:
        if seq[index] > maxLofR:
            maxLofR = seq[index]
        index -= 1

    # find first element just less than maxLofR starting from right
    index = len(seq) - 1
    while seq[index] >= maxLofR:
        index -= 1
    rightBound = index

    return leftBound, rightBound

def test():
    'test for subSort method'
    data = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
    print subSort(data)

if __name__ == '__main__':
    test()
