
def createFreqMap(s):
    fmap = {}
    for c in s:
        if c in fmap:
            fmap[c] += 1
        else:
            fmap[c] = 1
    return fmap

def compareMaps(m1, m2):
    if len(m1) != len(m2):
        return False
    for k, v in m1.items():
        if k not in m2:
            return False
        if m2[k] != v:
            return False
    return True

def isPermutation(s1, s2):
    if len(s1) != len(s2):
        return False
    return compareMaps(createFreqMap(s1), createFreqMap(s2))

def testIsPerm():
    assert(isPermutation('abcd', 'cdba') == True)
    assert(isPermutation('bbbb', 'bbbb') == True)
    assert(isPermutation('ab', 'ba') == True)
    assert(isPermutation('abcd', 'cdbae') == False)
    assert(isPermutation('abcd', 'cdbe') == False)
    print 'test passed'

testIsPerm()
