'solution for diving board lengths problem'

shorter = 1
longer = 2

def getAllPossibleLengths(k):
    'returns a list of all possible lengths'
    numLongs = 0
    lengths = []
    while numLongs <= k:
        lengths.append(shorter*(k - numLongs) + longer*numLongs)
        numLongs += 1
    return lengths

def test():
    'test method'
    print getAllPossibleLengths(5)

if __name__ == '__main__':
    test()
