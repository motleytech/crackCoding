'''
check if the given linked lists intersect
return the intersection point

Lists intersect if the last node is the same.
To find intersection point (first common node), find length
of both lists... if the smaller list has n nodes and the longer
one has m nodes, then the first intersecting node must be in
the last n nodes of the longer list. Skip the first m-n nodes in
the longer list, then traverse the lists together comparing each node.
Running time O(m+n)
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

def getFirstCommonNode(lst1, count1, lst2, count2):
    '''
    Return the first common nodes between the lists
    '''
    curr1, curr2 = lst1.getHead(), lst2.getHead()

    for ignore in range(max(0, count1 - count2)):
        curr1 = curr1.next
    for ignore in range(max(0, count2 - count1)):
        curr2 = curr2.next

    while curr1 is not None:
        if curr1 is curr2:
            return curr1
        curr1 = curr1.next
        curr2 = curr2.next

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

    return True, getFirstCommonNode(lst1, count1, lst2, count2)


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
