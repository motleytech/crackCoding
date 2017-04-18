'''
Remove duplicate entries from a linked list
'''

from llist import createRandomList

def removeDuplicates(inList):
    '''
    remove duplicates nodes from a linked list
    using a set to keep track of seen items
    '''
    visited = set()
    prev = None
    for node in inList:
        if node.data in visited:
            inList.remove(node, prev)
        else:
            visited.add(node.data)
            prev = node

def remDupesWOBuffer(inList):
    '''
    Remove duplicates without using extra storge.
    For each element, traverse the list and remove any duplicates
    '''
    curr = inList.head
    while curr != None:
        nxt = curr.next
        prev = curr
        while nxt != None:
            if nxt.data == curr.data:
                inList.remove(nxt, prev)
                nxt = nxt.next
            else:
                prev = nxt
                nxt = nxt.next
        curr = curr.next

def numDupes(inList):
    '''
    Count the number of duplicates in the list
    '''
    nodeList = [node.data for node in inList]
    return len(nodeList) - len(set(nodeList))


def test_remDupes(func):
    '''
    test for remove duplicates method
    '''
    print 'Testing %s... ' % func.__name__,

    lst = createRandomList(100, 100)
    ndupes = numDupes(lst)
    while ndupes == 0:
        lst = createRandomList(100, 100)
        ndupes = numDupes(lst)
    assert ndupes != 0

    func(lst)
    assert numDupes(lst) == 0

    print 'Passed.'

if __name__ == '__main__':
    test_remDupes(removeDuplicates)
    test_remDupes(remDupesWOBuffer)
