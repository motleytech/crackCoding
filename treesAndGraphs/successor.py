'''method which returns successor of a given node in bst'''

def getSucc(node):
    'return successor of node (assume bst)'
    # find the smallest right child
    if node.right:
        curr = node.right
        while curr.left:
            curr = curr.left
        return curr
    # find a parent, grandparent, where parent is left child of gp
    while node.parent:
        if node == node.parent.left:
            return node.parent
        node = node.parent
    return None


def getMin(node):
    '''returns the mininum element under given node/subtree'''
    curr = node
    while curr.left:
        curr = curr.left
    return curr


if __name__ == '__main__':
    from minimalTree import lp2, createTree
    from printTree import printTree

    N, M = 0, 10
    tree1 = createTree(range(N, M), lp2(M-N) - 1, lp2(M-N)/2)
    printTree(tree1)

    node1 = getMin(tree1)
    while 1:
        nextNode = getSucc(node1)
        if nextNode is None:
            break
        assert nextNode.data == (node1.data + 1)

        print "%s -> %s" % (node1, nextNode)
        node1 = nextNode
