'''
method to order/partition a list based on a pivot
into items smaller than the pivot and >= to the pivot
'''

from llist import createRandomList

def partition(lst, x):
    '''
    partition a list based on the pivot x

    works by iterating throught the nodes, and if node is <x,
    we move node to the beginning of the list.

    This method switches the order of elements <x in the list
    (if elements a, b are both <x and occur in a particular order,
    their order will be reversed in the partitioned list)
    '''
    head = lst.getHead()
    if head is None:
        # nothing in the list to partition
        return lst
    prev = head
    curr = prev.next
    if curr is None:
        # there is only 1 element... nothing to partition
        return lst

    while curr is not None:
        if curr.data < x:
            lst.remove(curr, prev)
            lst.insertAtHead(curr)
            curr = prev.next
        else:
            prev = curr
            curr = curr.next

    return lst

def partition2(lst, x):
    '''
    another way to partition list based on pivot x

    works by skipping elements less than x, then iterating over
    remaining elements and moving elements <x after the
    last observed element <x.

    This method keeps the order or elements intact.
    Useful for implementing stable version of quicksort
    (if you wanted to do that).
    '''
    less = None
    curr = lst.getHead()
    prev = None
    # position less at last element less than x
    while curr is not None and curr.data < x:
        less = curr
        prev = curr
        curr = curr.next

    # proceed from less onwards
    while curr is not None:
        if curr.data < x:
            lst.remove(curr, prev)
            if less is not None:
                lst.insertAtNode(curr, less)
            else:
                lst.insertAtHead(curr)
            less = curr
            curr = prev.next
        else:
            prev = curr
            curr = curr.next


def test_partition(func):
    '''
    test for list partition methods
    '''
    print 'Testing %s... ' % func.__name__,
    lst = createRandomList(20, 20)
    func(lst, 10)
    nlst = list(x for x in lst)

    # make sure the list is partitioned correctly
    index = 0
    while index < len(nlst):
        if nlst[index] >= 10:
            break
        index += 1

    while index < len(nlst):
        assert nlst[index] >= 10
        index += 1

    print 'Passed'


if __name__ == '__main__':
    test_partition(partition)
    test_partition(partition2)
