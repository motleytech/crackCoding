'''
method to order/partition a list based on a pivot
into items smaller than the pivot and >= to the pivot
'''

from llist import createRandomList, LinkedList

def partition(lst, x):
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
    assert(isinstance(lst, LinkedList))
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


lst = createRandomList(20, 20)
lst2 = lst.createCopy()
print lst, "\n\n"
partition(lst, 10)
print lst, "\n\n"

print lst2, "\n\n"
partition2(lst2, 10)
print lst2, "\n\n"

