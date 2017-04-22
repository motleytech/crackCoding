'''
check if a list is a palindrome
'''

from llist import LinkedList

def isPalindrome(lst):
    '''
    return true if lst is a palindrome
    '''
    nodes = list(lst)
    for x, y in zip(nodes, reversed(nodes)):
        if x.data != y.data:
            return False
    return True

def isPalin2(lst, curr):
    '''
    return True, None if lst is a palindrome
    '''
    if curr.next is None:
        return (curr.data == lst.data, lst.next)
    res, node = isPalin2(lst, curr.next)
    if not res:
        return (False, None)
    return (node.data == curr.data, node.next)


def test_isPalindrome():
    '''
    test for isPalindrome methods
    '''
    lst = LinkedList()
    lst.add(1).add(2).add(3)

    assert not isPalindrome(lst)
    assert not isPalin2(lst.head, lst.head)[0]

    lst.add(2).add(1)

    assert isPalindrome(lst)
    assert isPalin2(lst.head, lst.head)[0]

    print 'Test Passed.'


if __name__ == '__main__':
    test_isPalindrome()
