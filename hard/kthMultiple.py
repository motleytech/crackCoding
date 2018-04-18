'''Solution for the kth multiple problem'''

class Node(object):
    'node of a queue with next and prev pointers'
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Queue(object):
    'queue for storing cached data'
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def push(self, node):
        'add a node to the end of the queue'
        if not isinstance(node, Node):
            node = Node(node)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node

        self.count += 1
        return node

    def pop(self):
        'remove node from front of queue'
        if not self.count:
            raise Exception('Cannot pop from empty queue')
        self.count -= 1
        node = self.head
        if self.count == 0:
            self.head = self.tail = None
        else:
            self.head = node.next
            self.head.prev = None
        return node.data

    def getSize(self):
        'return size of the current queue'
        return self.count

    def __iter__(self):
        node = self.head
        while node != None:
            yield node.data
            node = node.next


def kthMult(k):
    'returns the kth multiple of 3,5,7'
    mults = [1, 3, 5, 7]
    if k < 5:
        return mults[k-1]

    queue = Queue()
    _ = [queue.push(x) for x in mults]

    index = 4
    cmax = 7
    while index < k:
        cval = cmax * 3
        for y in queue:
            if y*7 <= cmax:
                queue.pop()
                continue

            if y*3 >= cval:
                break

            if y*3 > cmax and y*3 < cval:
                cval = y*3
            elif y*5 > cmax and y*5 < cval:
                cval = y*5
            elif y*7 > cmax and y*7 < cval:
                cval = y*7
        cmax = cval
        queue.push(cval)
        index += 1

    return cval

def test():
    'test for kthMult method'
    assert kthMult(5) == 9
    assert kthMult(20) == 175
    assert kthMult(2000) == 100913818359375
    print 'Passed'

if __name__ == '__main__':
    test()
