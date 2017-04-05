# pylint: disable=C0103

'''Implements duplicate removal from linked lists'''

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
    remove duplicates without using extra storge
    for each element, traverse the list and remove any duplicates
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


lst = createRandomList(100, 100)
print "The list currently has %s duplicates" % numDupes(lst)
removeDuplicates(lst)
print "The list now has %s duplicates" % numDupes(lst)

lst = createRandomList(100, 100)
print "The list currently has %s duplicates" % numDupes(lst)
remDupesWOBuffer(lst)
print len(lst)
print "The list now has %s duplicates" % numDupes(lst)
