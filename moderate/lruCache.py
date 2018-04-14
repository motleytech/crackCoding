'implementation of an LRU cache'


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

    def moveNodeToEnd(self, node):
        'move a node to the end of the queue'
        if node == self.tail:
            # nothing to do... already at end
            return

        if node == self.head:
            self.head = node.next
            self.head.prev = None
        else:
            prev, nxt = node.prev, node.next
            prev.next = nxt
            nxt.prev = prev
        self.tail.next = node
        node.next = None
        node.prev = self.tail
        self.tail = node
        return node

    def getSize(self):
        'return size of the current queue'
        return self.count

class LRUCache(object):
    'the LRU cache class'
    def __init__(self, size, store):
        self.maxSize = size
        self.queue = Queue()
        self.nodeMap = {}
        self.store = store

    def get(self, key):
        'get a value from the cache (from store if not found in cache)'
        if key in self.nodeMap:
            node = self.nodeMap[key]
            data = node.data[1]
            self.queue.moveNodeToEnd(node)
            return data
        data = self.store.get(key)
        node = Node((key, data))
        self.nodeMap[key] = node
        self.queue.push(node)
        if self.queue.getSize() > self.maxSize:
            key2 = self.queue.pop()[0]
            del self.nodeMap[key2]
        return data

    def __repr__(self):
        return '<LRU %s>' % self.queue.getSize()



class Store(object):
    'dummy data store'
    def __init__(self):
        pass

    def get(self, key):
        'return data corresponding to the key'
        return '%s: data' % key


def test():
    'test for LRU cache'
    import random
    keys = [int(random.gauss(0, 5)) for _ in range(200)]

    store = Store()
    cache = LRUCache(10, store)
    for i, k in enumerate(keys):
        _ = cache.get(k)

        #print '---------- %s' % k

        seen = set()
        curr = cache.queue.tail
        for j in range(i, -1, -1):
            m = keys[j]
            if m in seen:
                continue
            seen.add(m)
            #print m, curr.data[0], cache.queue.count
            assert m == curr.data[0]
            curr = curr.prev
            if not curr:
                break

        assert len(cache.nodeMap.keys()) == cache.queue.count

    print 'Passed'

if __name__ == '__main__':
    test()
