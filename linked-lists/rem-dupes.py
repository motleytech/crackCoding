from llist import LinkedList, Node
from random import randint


def remDupes(lst):
    '''
    remove duplicates nodes from a linked list
    '''
    visited = set()
    prev = None
    toRemove = set()
    for node in lst:
        if node.data in visited:
            lst.remove(node, prev)
        else:
            visited.add(node.data)
            prev = node

def numDupes(lst):
    nodeList = [node.data for node in lst]
    return len(nodeList) - len(set(nodeList))


lst = LinkedList()
[lst.add(Node(randint(1,50))) for x in range(100)]

print "The list currently has %s duplicates" % numDupes(lst)
remDupes(lst)
print "The list now has %s duplicates" % numDupes(lst)
