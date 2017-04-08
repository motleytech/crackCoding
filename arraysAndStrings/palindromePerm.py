'''
Check if a given string is a permutation of a palindrome

In other words, can we rearrage the characters to form a palindrome?

Think yourself before reading ahead...
The key idea is to realize that every character must occur an
even number of times (because it must repeat on both halves)
with the possible exception of the center character.

So, each character in a palindrome must occur an even number of times, with
the possible exception that only 1 character can occur an odd number
of times (if length of string is odd)

All we need to do is create a freq map of the characters and verify that
at most 1 character has odd freq
'''

from collections import defaultdict

def createFreqMap(s, ignoreSpace=True):
    '''
    Create a freq map of the characters of s
    '''
    fmap = defaultdict(lambda: 0)
    for c in s:
        if ignoreSpace and c == ' ':
            continue
        fmap[c] += 1
    return fmap

def isPermOfPalindrome(s):
    '''
    Check if s is a permutation of a palindrome
    '''
    if sum(v%2 for v in createFreqMap(s).values()) > 1:
        return False
    return True

def testIPOP():
    '''
    Test our verification method
    '''
    print "Testing isPermOfPalindrome... ",
    assert isPermOfPalindrome('amanaplanacanalpanama')
    assert not isPermOfPalindrome('notapalin')
    assert isPermOfPalindrome('a man a plan a canal panama')
    assert isPermOfPalindrome('')
    assert isPermOfPalindrome('tact coa')
    print "Passed"

if __name__ == '__main__':
    testIPOP()
