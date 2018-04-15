'solution for the letters and numbers problem'

digits = set(''.join(str(x) for x in range(10)))

def getLongestSubarr(arr):
    'return the longest subarray with equal number of letters and numbers'
    mDiff = 0
    mIndices = (0, 0)
    scoreMem = {}
    score = 0
    for i, x in enumerate(arr):
        score += (1 if x in digits else -1)
        if score in scoreMem:
            cDiff = i - scoreMem[score]
            if cDiff > mDiff:
                mDiff = cDiff
                mIndices = (scoreMem[score], i)
        else:
            scoreMem[score] = i

    return arr[mIndices[0]+1: mIndices[1]+1]

def test():
    'test for getLongestSubarr'
    assert getLongestSubarr('a1aaaaaa111a1a11111') == '1aaaaaa111a1a111'
    print 'Passed'

if __name__ == '__main__':
    test()
