'''
Given 2 strings s1 and s2, and a method isSubstring, write a
method to detect if s1 is a rotation of s2

The key ideas are...
1. len(s1) == len(s2)
2. s1 is a substring of s2 + s2

If the above 2 conditions are met, then s2 is a rotation of s1

'''

def isSubstring(s1, s2):
    '''
    Returns True if s1 is a substring of s2
    '''
    return s1 in s2

def isRotation(s1, s2):
    '''
    Returns True if s1 is a rotation of s2
    '''
    if len(s1) == len(s2):
        if isSubstring(s1, s2 + s2):
            return True
    return False

def test_isRotation():
    print 'Testing isRotation...',

    assert isRotation('abcd', 'bcda')
    assert isRotation('a', 'a')

    print 'Passed'

if __name__ == '__main__':
    test_isRotation()






