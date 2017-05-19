'''
the home of the queue class

its derived from the linkedlist class
'''

import sys
sys.path.append('../linkedLists')
from llist import LinkedList, Node #pylint: disable=E0401,C0413

class Queue(LinkedList):
    def add(self, item):
        node = Node(item)
        LinkedList.add(self, node)

    def push(self, item):
        return self.add(item)

    def remove(self):
        if len(self) < 1:
            raise Exception("Cannot remove from empty Queue")
        node = self.head
        LinkedList.remove(self, node)
        return node.data

    def pop(self):
        return self.remove()

    def peek(self):
        if len(self) < 1:
            raise Exception("Cannot peek into empty Queue")
        return self.head.data

    def isEmpty(self):
        return len(self) == 0






