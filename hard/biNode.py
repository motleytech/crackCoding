'solution for converting binary search tree to sorted doubly linked list'


class Node(object):
    'the node class, having pointers for left and right elements'
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def treeToList(node, prev=None):
    'converts a bst to sorted doubly linked list. returns the tail element'
    if node.left:
        prev = treeToList(node.left, prev)
    node.left = prev
    if prev:
        prev.right = node
    if node.right:
        prev = treeToList(node.right, node)
    else:
        prev = node
    return prev


def test():
    'test for treeToList method'
    root = Node(3)
    left = root.left = Node(1)
    left.left = Node(0)
    left.right = Node(2)

    right = root.right = Node(5)
    right.left = Node(4)
    right.right = Node(6)

    n = treeToList(root)
    elements = []
    while True:
        elements.append(n.data)
        if n.left:
            n = n.left
        else:
            break

    while True:
        elements.append(n.data)
        if n.right:
            n = n.right
        else:
            break

    assert elements == [6, 5, 4, 3, 2, 1, 0, 0, 1, 2, 3, 4, 5, 6]

    print 'Passed'


if __name__ == '__main__':
    test()
