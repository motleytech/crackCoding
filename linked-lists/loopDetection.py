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

    loopNodes = set([p2])
    p2 = p2.next
    while p2 is not p1:
        loopNodes.add(p2)
        p2 = p2.next

    curr = lst.getHead()
    while True:
        if curr in loopNodes:
            return True, curr
        curr = curr.next

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

    assert hasLoop(lst)[0] == False

    lst.tail.next = nodea
    result, node = hasLoop(lst)
    assert result
    assert node is nodea
    print 'Passed'

if __name__ == '__main__':
    test_hasLoop()
