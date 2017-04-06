'''
method to check if the given string has all unique chars
'''

def hasUniqueChars(s):
    existing = set()
    for c in s:
        if c in existing:
            return False
        existing.add(c)
    return True

def hasUniqueCharsNoBuf(s):
    ls = len(s)
    for x in range(ls - 1):
        for y in range(x+1, ls):
            if s[x] == s[y]:
                return False
    return True

def testBufMethod():
    huc = hasUniqueChars
    assert(huc('abcde') == True)
    assert(huc('abcdea') == False)
    assert(huc('aa') == False)
    print 'test 1 passed'

def testNonBufMethod():
    hnb = hasUniqueCharsNoBuf
    assert(hnb('abcde') == True)
    assert(hnb('abcdea') == False)
    assert(hnb('aa') == False)
    print 'test 2 passed'

testBufMethod()
testNonBufMethod()
