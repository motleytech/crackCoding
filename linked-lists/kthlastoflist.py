'''
method to retrieve the kth last element of a list
'''

from llist import createRandomList

def getKthLastElem(inList, k):
    '''
    return the kth last element of inList (linked list)
    '''
    fwd, back = inList.head, inList.head
    for _ in range(k):
        if fwd is None:
            raise IndexError("list index -%s out of range" % k)
        fwd = fwd.next

    while fwd is not None:
        fwd = fwd.next
        back = back.next
    return back

lst = createRandomList(10, 100)
nodes = [n.data for n in lst]
nodes2 = list(reversed([getKthLastElem(lst, x).data for x in range(1, 11)]))

assert nodes == nodes2
print "success!!"