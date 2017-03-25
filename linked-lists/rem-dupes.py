from llist import LinkedList, Node
from random import randint

def createList(N, M):
    '''
    Create a linked list containing N nodes,
    and each node consisting of a random number upto M
    '''
    lst = LinkedList()
    [lst.add(Node(randint(1, M+1))) for x in range(N)]
    return lst


def removeDuplicates(lst):
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

lst = createList(100, 100)
print "The list currently has %s duplicates" % numDupes(lst)
removeDuplicates(lst)
print "The list now has %s duplicates" % numDupes(lst)
