

# Given a binary search tree with distinct elements, print all possible
# arrays that could have led to this tree.

def recurBFS(curr, pnext, inputs):
    if len(pnext) == 0:
        inputs.append(curr[:])
        return
    for x in pnext.copy():
        curr.append(x)
        pnext.remove(x)
        if x.left:
            pnext.add(x.left)
        if x.right:
            pnext.add(x.right)

        recurBFS(curr, pnext, inputs)

        if x.left:
            pnext.remove(x.left)
        if x.right:
            pnext.remove(x.right)
        pnext.add(x)
        curr.pop()


def test_recurBFS():
    from minimalTree import createTree, lp2
    from printTree import printTree

    N, M = 0, 7
    tree = createTree(range(N, M), lp2(M-N) - 1, lp2(M-N)/2)

    #printTree(tree)
    #print '\n'

    inputs = []
    recurBFS([], set([tree]), inputs)

    #from pprint import pprint as pp
    #pp(inputs)
    #print '\n%s' % len(inputs)
    assert len(inputs) == 80


if __name__ == '__main__':
    test_recurBFS()
    print 'Test Passed'





