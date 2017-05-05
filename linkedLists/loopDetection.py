'''
detect if a list has a loop, and find the first loop node

loop is detected by using 2 pointers which traverse the list
at different speeds (1 nodes at a time vs 2).
If there is a loop, the pointers will meet.
'''

from llist import LinkedList, Node

def hasLoop(lst):
    '''
    detect if a loop exists and return the first loop node
    '''
    p1 = p2 = lst.getHead()
    if not p1:
        return False, None

    while p1 != None and p2 != None:
        p1 = p1.next
        p2 = p2.next
        if None in (p1, p2):
            return False, None
        p2 = p2.next
        if p2.next is None:
            return False, None

        if p1 is p2:
            break

    loopLength = 1
    p2 = p2.next
    while p2 is not p1:
        loopLength += 1
        p2 = p2.next

    prev = curr = lst.getHead()
    steps = 0
    while steps < loopLength:
        steps += 1
        curr = curr.next

    while prev is not curr:
        curr = curr.next
        prev = prev.next

    return True, prev

def test_hasLoop():
    '''
    test for hasLoop method
    '''
    print 'Testing hasLoop method ... ',
    nodea = Node('a')
    lst = LinkedList()
    ignore = [lst.add(Node(x)) for x in range(4)]
    lst.add(nodea)
    ignore = [lst.add(Node(x)) for x in range(10)]

    assert not hasLoop(lst)[0]

    lst.tail.next = nodea
    result, node = hasLoop(lst)
    assert result
    assert node is nodea
    print 'Passed'

if __name__ == '__main__':
    test_hasLoop()
