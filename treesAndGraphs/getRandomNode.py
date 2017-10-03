
#
# create binary tree getRandomNode(), insert, find and delete
#

class Node(object):
    def __init__(self, data):
        self.data = data
        self.size = 1
        self.left = self.right = None

    def insert(self, data):
        if data < self.data:
            if not self.left:
                self.left = Node(data)
            else:
                self.left.insert(data)
        else:
            if not self.right:
                self.right = Node(data)
            else:
                self.right.insert(data)
        self.size += 1

    def getRandomNode(self):
        from random import randint
        num = randint(1, self.size)
        return self.getNodeAtIndex(num)

    def getNodeAtIndex(self, num):
        lsize = self.left.size if self.left else 0
        if num <= lsize:
            return self.left.getNodeAtIndex(num)
        if num == lsize + 1:
            return self
        if num > lsize + 1:
            return self.right.getNodeAtIndex(num - lsize - 1)

def test_getRandomNode():
    from minimalTree import createTree, lp2
    from printTree import printTree

    N, M = 0, 7
    tree = createTree(range(N, M), lp2(M-N) - 1, lp2(M-N)/2)
    printTree(tree)

    root = [None]

    def bfs(nn):
        from Queue import Queue
        toVisit = Queue()
        toVisit.put(nn)
        while not toVisit.empty():
            curr = toVisit.get()
            if not root[0]:
                root[0] = Node(curr.data)
            else:
                root[0].insert(curr.data)
            if curr.left:
                toVisit.put(curr.left)
            if curr.right:
                toVisit.put(curr.right)

    bfs(tree)

    bt = root[0]
    print [bt.getRandomNode().data for x in range(20)]


if __name__ == '__main__':
    test_getRandomNode()

