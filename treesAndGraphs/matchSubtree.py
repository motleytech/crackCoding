
#Tl and T2 are two very large binary trees, with Tl much bigger than T2. Create an
#algorithm to determine if T2 is a subtree of Tl.
#A tree T2 is a subtree ofTi if there exists a node n in Ti such that the subtree of n is identical to T2.
#That is, if you cut off the tree at node n, the two trees would be identical.

def doTreesMatch(node1, node2):
    if node1.data != node2.data:
        return False

    if (node1.left and node2.left):
        if not doTreesMatch(node1.left, node2.left):
            return False
    elif (node1.left or node2.left):
        return False

    if (node1.right and node2.right):
        if not doTreesMatch(node1.right, node2.right):
            return False
    elif (node1.right or node2.right):
        return False

    return True




def isSubtree(t1, t2):
    # walk nodes of t1 in bfs order
    # for each node, try to match with t2
    toVisit = [t1]
    while toVisit:
        node = toVisit.pop()
        if doTreesMatch(node, t2):
            return True, node
        if node.left:
            toVisit.append(node.left)
        if node.right:
            toVisit.append(node.right)
    return False, None


def test_isSubtree():
    from minimalTree import createTree, lp2
    from printTree import printTree

    N, M = 0, 41
    tree1 = createTree(range(N, M), lp2(M-N) - 1, lp2(M-N)/2)
    #printTree(tree1)


    N, M = 0, 7
    tree2 = createTree(range(N, M), lp2(M-N) - 1, lp2(M-N)/2)
    #printTree(tree2)

    assert isSubtree(tree1, tree2)[0] == True

    N, M = 0, 8
    tree2 = createTree(range(N, M), lp2(M-N) - 1, lp2(M-N)/2)
    #printTree(tree2)

    assert isSubtree(tree1, tree2)[0] == False

if __name__ == '__main__':
    test_isSubtree()
    print 'Test Passed'

