'''
the stack class lives here.

its derived from the linkedlist class
'''

import sys
sys.path.append('../linkedLists')
from llist import LinkedList, Node #pylint: disable=E0401,C0413

class Stack(LinkedList):
    '''
    the implementation of the stack class
    '''
    def pop(self):
        '''
        remove and return the last inserted item from the stack
        '''
        if len(self) < 1:
            raise Exception("Attempting to pop from empty Stack")
        node = self.head
        self.remove(node)
        return node.data

    def push(self, value):
        '''
        add a new item to the stack
        '''
        node = Node(value)
        self.insertAtHead(node)

    def peek(self):
        '''
        return the last inserted item without removing it from the stack
        '''
        if len(self) < 1:
            raise Exception("Attempting to peek into empty Stack")
        return self.head.data

    def isEmpty(self):
        '''
        returns true if stack is empty
        '''
        return len(self) == 0
