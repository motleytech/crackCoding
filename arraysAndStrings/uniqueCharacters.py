'''
determine if a string has all unique characters

1. Solve it.
2. Solve it without using extra storage.

Key idea: Using a dictionary (hashmap / associative array), we simply iterate
over the characters, inserting each new one into the dictionary (or set).

Before inserting a character, we check if it already exists in the dictionary/set.
If it exists, then that character is repeated, and we return False.

If we reach the end of the string while repeating this process, it implies that
all characters are unique (else we would have returned False at some point).

We return True.
'''

def hasUniqueChars(s):
    '''
    checks if a string is composed of unique characters
    (using a set to store seen characters)
    '''
    existing = set()
    for c in s:
        if c in existing:
            return False
        existing.add(c)
    return True

def hasUniqueCharsNoBuf(s):
    '''
    checks if a string consists of unique characters
    This version uses no extra storage.
    Works by iterating over characters and comparing each character with
    all the others to make sure none other matches.
    '''
    ls = len(s)
    for x in range(ls - 1):
        for y in range(x+1, ls):
            if s[x] == s[y]:
                return False
    return True

def testMethod(func):
    '''
    test unique verification methods
    '''
    print 'Testing %s: ' % func.__name__,

    assert func('')
    assert not func('aa')
    assert func('abcde')
    assert not func('abcdea')
    assert not func('aagdjflk')
    assert not func('gdjfklaa')
    assert not func('gdjfjkl')

    print 'Passed'


if __name__ == '__main__':
    testMethod(hasUniqueChars)
    testMethod(hasUniqueCharsNoBuf)
