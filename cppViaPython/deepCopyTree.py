'method returns deep copy of a tree under at given node'


class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def copy(self):
        return Node(self.data)

    def __repr__(self):
        return "Node(%s)" % self.data

    def __str__(self):
        return "<%s>" % self.__repr__()

def deepCopyTree(node):
    cnode = node.copy()
    if node.left:
        cnode.left = deepCopyTree(node.left)
    if node.right:
        cnode.right = deepCopyTree(node.right)
    return cnode

def test_deepCopyTree():
    tree = Node(0)
    tree.left = n1 = Node(1)
    tree.right = n2 = Node(2)

    n1.left = n3 = Node(3)
    n1.right = n4 = Node(4)

    n2.left = n5 = Node(5)
    n2.right = n6 = Node(6)

    res = deepCopyTree(n1)

    assert (res.data == n1.data)
    assert (res is not n1)

    assert (res.left.data == n1.left.data)
    assert (res.left is not n1.left)

    assert (res.right.data == n1.right.data)
    assert (res.right is not n1.right)

    print 'Test Passed'

if __name__ == '__main__':
    test_deepCopyTree()





