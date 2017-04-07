'''
method to check if the given string has all unique chars
'''

def hasUniqueChars(s):
    '''
    checks if a string is composed of unique characters
    (uses a set)
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
    This version uses no extra storage (like a set or dict(hashmap))
    '''
    ls = len(s)
    for x in range(ls - 1):
        for y in range(x+1, ls):
            if s[x] == s[y]:
                return False
    return True

def testMethod(func):
    huc = func
    assert(huc('abcde') == True)
    assert(huc('abcdea') == False)
    assert(huc('aa') == False)
    print 'test passed: %s' % func.__name__


testMethod(hasUniqueChars)
testMethod(hasUniqueCharsNoBuf)
