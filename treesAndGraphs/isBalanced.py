'''method to check if a binary tree is balanced'''

def isBalanced(node):
    '''
    returns True if tree is balanced (at each node,
    left and right subtree heights differ by <= 1)
    '''
    lb, lh = True, 0
    if node.left:
        lb, lh = isBalanced(node.left)
    rb, rh = True, 0
    if node.right:
        rb, rh = isBalanced(node.right)

    return ((lb and rb) and abs(lh - rh) <= 1, max(lh, rh) + 1)

if __name__ == '__main__':
    N, M = 0, 10
    from minimalTree import lp2, createTree
    from printTree import printTree
    print 'max power of 2 : %s' % lp2(M-N)
    tree1 = createTree(range(N, M), lp2(M-N) - 1, lp2(M-N)/2)
    ib, th = isBalanced(tree1)
    printTree(tree1)
    print ib, th
