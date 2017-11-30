'method to reverse a string (this is a joke ... right?)'


def reverseString(st):
    'returns the reverse of the string st'
    return st[::-1]

def test_reverseString():
    'test for reverseString'
    assert reverseString('') == ''
    assert reverseString('a') == 'a'
    assert reverseString('abcd') == 'dcba'
    print 'Test passed'

if __name__ == '__main__':
    test_reverseString()
