'''method to check if a tree is a bst'''

def isBST(node):
    '''returns true is the given tree is a bst'''
    lm, ln, rm, rn = [None]*4

    if node.left:
        res, lm, ln = isBST(node.left)
        if not res:
            return False, None, None
    else:
        lm, ln = (node.data, node.data)
    if node.right:
        res, rm, rn = isBST(node.right)
        if not res:
            return False, None, None
    else:
        rm, rn = (node.data, node.data)

    if node.data >= lm and node.data <= rn:
        return True, rm, ln

    return False, None, None


if __name__ == '__main__':
    from minimalTree import lp2, createTree, Node
    from printTree import printTree

    N, M = 0, 10
    tree1 = createTree(range(N, M), lp2(M-N) - 1, lp2(M-N)/2)
    tree1.right.right = Node(6)
    printTree(tree1)
    result, mx, mn = isBST(tree1)
    print '\n', result

