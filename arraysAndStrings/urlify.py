'''
Replace all spaces in a string with '%20'

We can do this easily in python with the string method 'replace', for example
to urlify the string myurl, its enough to call myurl.replace(' ', '%20')

Its that simple.

To make the task a little more difficult (to be more in line with what
the question expects), we will convert the string into a list of characters.

Our task will now be to return ['a', '%', '2', '0', 'b'] when given an input ['a', ' ', 'b']
'''

def urlify(s):
    '''
    replace spaces in s with %20... the C/Java way
    '''
    # convert string into list of characters
    s = [c for c in s]
    # count number of spaces
    ns = sum(1 for c in s if c == ' ')
    # get length of string
    ls1 = len(s) - 1
    # add 2*ns empty spaces at the end of the list
    s.extend([' ']*(2*ns))
    # get the new length
    ls2 = len(s) - 1

    # move characters from end of string to end of list
    # while replacing space with %20
    while ls1 >= 0:
        if s[ls1] == ' ':
            s[ls2] = '0'
            s[ls2-1] = '2'
            s[ls2-2] = '%'
            ls2 -= 3
        else:
            s[ls2] = s[ls1]
            ls2 -= 1
        ls1 -= 1
    return ''.join(s)

def test_urlify():
    '''
    Test the urlify method
    '''
    print 'Testing URLify: ',
    assert urlify(' ') == '%20'
    assert urlify('a b') == 'a%20b'
    assert urlify('a b ') == 'a%20b%20'
    assert urlify('a  b ') == 'a%20%20b%20'
    print 'Passed'

if __name__ == '__main__':
    test_urlify()
