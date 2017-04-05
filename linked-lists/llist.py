'''definitions for LinkedList and Node classes'''

class Node(object):
    '''the class for the list node object'''
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return "<Node:%s>" % self.data

    def __str__(self):
        return self.__repr__()

    def copy(self, other):
        '''copy data from other node to this one'''
        self.data = other.data

class LinkedList(object):
    '''the linked list class'''
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def add(self, node):
        '''
        add a node to the end of the linked list
        '''
        if self.tail is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        node.next = None
        self.count += 1
        return self

    def remove(self, node, prev=None):
        '''
        Remove the given node from the list
        optionally, the caller can provide the prev node (if it exists) to
        make the removal faster
        '''
        if self.count == 0:
            raise ValueError('Cannot remove %s from empty list' % node)
        if self.head is node:
            if self.tail is node:
                self.head = self.tail = None
            else:
                self.head = node.next
        elif self.tail is node:
            prev = prev if prev else self._getPrevNode(node)
            self.tail = prev
            prev.next = None
        else:
            # probably a middle node
            prev = prev if prev else self._getPrevNode(node)
            if prev is None:
                raise ValueError('Could not find prev node to %s in list' % node)
            if prev.next is not node:
                raise ValueError('Node %s is not the next of provided prev %s' % (node, prev))
            prev.next = node.next
        self.count -= 1
        return self

    def _getPrevNode(self, node):
        '''
        Return the node previous to the given node in the linked list (if it exists),
        else return None.
        '''
        if self.head is node:
            return None
        prev = self.head
        while prev:
            if prev.next is node:
                return prev
            prev = prev.next
        # dropped through at the end... could not find prev
        return None

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        nodes = []
        curr = self.head
        while curr:
            nodes.append("%s" % curr)
            curr = curr.next
        return "## LinkedList : " + " -> ".join(nodes) + " -> None ##"

    def __iter__(self):
        curr = self.head
        while curr:
            yield curr
            curr = curr.next

    def __len__(self):
        return self.count


def createRandomList(N, M):
    '''
    Create a linked list containing N nodes,
    and each node consisting of a random number upto M
    '''
    from random import randint
    newList = LinkedList()
    _ = [newList.add(Node(randint(1, M+1))) for _ in range(N)]
    return newList
