'''
Delete a given middle node from a linked list. You only have access
to the node... you have no access to the list elements before the node,
and no access to the list data structure.

Note: This is a very hackish thing to do.
Usually, there should never arise a situation where you have
to delete a node without having access to the linked list itself. This can
also screw up data structures that the list might be maintaining
regarding the elements in the list (e.g. count of nodes in the list).
'''

from llist import createRandomList


def deleteMiddle(node):
    '''
    Given a node in the middle of a linked list, delete it.
    No access to the list of nodes prior to the given node
    is available.

    '''
    if node.next:
        node.copy(node.next)
        node.next = node.next.next

def test_deleteMiddle(func):
    '''
    test for deleteMiddle method
    '''
    print 'Testing %s... ' % func.__name__,

    lst = createRandomList(6, 1000)
    nodes = list(lst)
    node3data = nodes[3].data
    func(nodes[3])
    assert nodes[2].next.data != node3data

    print 'Passed.'

if __name__ == '__main__':
    test_deleteMiddle(deleteMiddle)
