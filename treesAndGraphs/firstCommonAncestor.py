
def getFCA(n1, n2):
    c1, c2 = 0, 0

    n1c, n2c = n1, n2
    while n1c.parent:
        n1c = n1c.parent
        c1 += 1

    while n2c.parent:
        n2c = n2c.parent
        c2 += 1

    n1c, n2c = n1, n2

    if c1 > c2:
        for x in range(c1-c2):
            n1c = n1c.parent
    else:
        for x in range(c2-c1):
            n2c = n2c.parent

    while n1c != n2c:
        n1c = n1c.parent
        n2c = n2c.parent

    return n1c



def test_getFCA():
    from minimalTree import createTree, lp2

    N, M = 0, 41
    tree = createTree(range(N, M), lp2(M-N) - 1, lp2(M-N)/2)

    assert getFCA(tree.left.right.right, tree.right.left.left.right).data == 31
    assert getFCA(tree.left.right.right, tree.left.left.left.right).data == 15




if __name__ == '__main__':
    test_getFCA()
    print 'Test Passed'











