'''
determine if a string has all unique characters

1. Solve it.
2. Solve it without using extra storage.
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
    test unique checking methods
    '''
    print 'Testing %s: ' % func.__name__,

    assert func('') == True
    assert func('aa') == False
    assert func('abcde') == True
    assert func('abcdea') == False
    assert func('aagdjflk') == False
    assert func('gdjfklaa') == False
    assert func('gdjfjkl') == False

    print 'Passed'


testMethod(hasUniqueChars)
testMethod(hasUniqueCharsNoBuf)
