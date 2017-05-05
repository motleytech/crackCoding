'''
Given two strings, check if one is a permutation of the other. Permutations of
this kind are also called anagrams.

The idea is to create a character freq map (using a dict) of the two strings
and compare them.

Note: We will ignore the spaces in the string, so that "i am lord voldemort"
is indeed a permutation of "tom marvolo riddle"
'''

from collections import defaultdict

def createFreqMap(s, ignoreSpaces=True):
    '''
    create a freq map of the characters occuring in s
    '''
    fmap = defaultdict(lambda: 0)
    for c in s:
        if ignoreSpaces:
            if c != ' ':
                fmap[c] += 1
        else:
            fmap[c] += 1
    return fmap

def areFreqMapsSame(m1, m2):
    '''
    Compare 2 frequency maps and return True if they are same.
    '''
    # compare number of keys... must have same number of keys
    # number of keys == number of unique characters in each string
    if len(m1) != len(m2):
        return False
    # is freq of occurence of each character the same in both
    for k, v in m1.items():
        if k not in m2:
            return False
        if m2[k] != v:
            return False
    return True

def isPermutation(s1, s2):
    '''
    check if s1 and s2 are anagrams of each other (contain the same characters)
    '''
    return areFreqMapsSame(createFreqMap(s1), createFreqMap(s2))

def testIsPerm():
    '''
    test for our implementation
    '''
    assert isPermutation('abcd', 'cdba')
    assert isPermutation('bbbb', 'bbbb')
    assert isPermutation('ab', 'ba')
    assert not isPermutation('abcd', 'cdbae')
    assert not isPermutation('abcd', 'cdbe')
    assert isPermutation('tom marvolo riddle', 'i am lord voldemort')
    print 'test passed'

if __name__ == '__main__':
    testIsPerm()
