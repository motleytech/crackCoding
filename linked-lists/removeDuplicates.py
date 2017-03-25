'''Implements duplicate removal from linked lists'''

from random import randint
from llist import LinkedList, Node

def createRandomList(N, M):
    '''
    Create a linked list containing N nodes,
    and each node consisting of a random number upto M
    '''
    newList = LinkedList()
    ignore = [newList.add(Node(randint(1, M+1))) for _ in range(N)]
    return newList

def removeDuplicates(inList):
    '''
    remove duplicates nodes from a linked list
    '''
    visited = set()
    prev = None
    for node in inList:
        if node.data in visited:
            inList.remove(node, prev)
        else:
            visited.add(node.data)
            prev = node


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
