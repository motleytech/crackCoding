'converts a binary tree into list of lists (each level is a list)'

def treeToLoL(tree):
    '''return list of lists (each list containing nodes from a
    level in the tree'''
    toVisit = [tree]
    lol = []
    while toVisit:
        lol.append([n for n in toVisit])
        oldToVisit = toVisit
        toVisit = []
        for n in oldToVisit:
            if n.left:
                toVisit.append(n.left)
            if n.right:
                toVisit.append(n.right)
    return lol

if __name__ == '__main__':
    N, M = 0, 41
    from minimalTree import lp2, createTree
    print 'max power of 2 : %s' % lp2(M-N)
    tree1 = createTree(range(N, M), lp2(M-N) - 1, lp2(M-N)/2)

    lol1 = treeToLoL(tree1)
    from pprint import pprint as pp
    pp(lol1)

