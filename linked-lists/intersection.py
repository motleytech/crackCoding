'''
check if the given linked lists intersect
return the intersection point
'''

from llist import LinkedList, Node

def getTailAndCount(lst):
    '''
    Return the tail and number of nodes in list
    '''
    count = 0
    curr = lst.getHead()
    if curr != None:
        count += 1
        while curr.next != None:
            curr = curr.next
            count += 1

    return curr, count

def getFirstCommonNode(lst1, lst2):
    '''
    Return the first common nodes between the lists
    '''
    head1, head2 = lst1.getHead(), lst2.getHead()
    curr = head1
    while curr is not None:
        curr2 = head2
        while curr2 is not None:
            if curr2 is curr:
                return curr
            curr2 = curr2.next
        curr = curr.next
    raise Exception("Common node not found.")

def areIntersecting(lst1, lst2):
    '''
    Check if the lists are intersecting and returns the
    intersecting node
    '''
    tail1, count1 = getTailAndCount(lst1)
    tail2, count2 = getTailAndCount(lst2)
    if not count1 or not count2:
        return False, None

    if tail1 is not tail2:
        return False, None

    if count1 < count2:
        node = getFirstCommonNode(lst1, lst2)
    else:
        node = getFirstCommonNode(lst2, lst1)

    if node:
        return True, node
    return False, None


def test_areIntersecting():
    '''
    test for areIntersecting method
    '''
    print 'Testing areIntersecting... ',
    node2, node3 = Node(2), Node(3)
    lst1 = LinkedList().add(Node(1)).add(node2).add(node3)
    lst2 = LinkedList().add(Node(4)).add(Node(5))

    intersecting, node = areIntersecting(lst1, lst2)
    assert intersecting == False
    assert node is None

    lst2.tail.next = node2
    lst2.tail = lst1.tail
    lst2.count += 2

    intersecting, node = areIntersecting(lst1, lst2)
    assert intersecting
    assert node is node2
    print 'Passed'

if __name__ == '__main__':
    test_areIntersecting()
