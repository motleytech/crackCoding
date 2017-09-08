'''function to print a binary tree to the console'''

def printTree(tree):
    '''prints a binary tree'''
    names = getNodeNames(tree)
    maxNameLen = max(len(x) for x in names)
    nodeLists = getNodeNameLists(tree, maxNameLen)

    nodeLists.reverse()
    nodeLists = nodeLists[1:]
    sp, ms = 0, maxNameLen
    lines = []
    for nl in nodeLists:
        #print sp, ms, nl
        line = " "*sp + (" "*ms).join([("%%%ss" % maxNameLen) % n for n in  nl])
        #print line
        sp = ms
        ms = ms*2 + maxNameLen
        lines.append(line)

    lines.reverse()
    print "\n".join(lines)


def getNodeNameLists(tree, mnl):
    '''returns node names in the tree in the order or levels
       as a list of lists (each list contains node names from
       a level)
    '''
    nLists = []
    toVisit = [tree]
    while len(toVisit) > 0:
        nLists.append([str(n) for n in toVisit])
        oldToVisit = toVisit
        toVisit = []
        nodesInOld = [n for n in oldToVisit if not isinstance(n, basestring)]
        if len(nodesInOld) == 0:
            break
        for node in oldToVisit:
            if isinstance(node, basestring):
                toVisit.extend([" "*mnl, " "*mnl])
                continue
            if node.left:
                toVisit.append(node.left)
            else:
                toVisit.append(" "*mnl)
            if node.right:
                toVisit.append(node.right)
            else:
                toVisit.append(" "*mnl)
    return nLists


def getNodeNames(tree):
    '''returns a set of all node names from the tree'''
    data = set()
    def dfs(node, height):
        '''depth first search for getting node names'''
        data.add(str(node.data))
        if node.left:
            dfs(node.left, height)
        if node.right:
            dfs(node.right, height)
    dfs(tree, 1)
    return data


if __name__ == '__main__':
    N, M = 0, 41
    from minimalTree import lp2, createTree
    print 'max power of 2 : %s' % lp2(M-N)
    tree1 = createTree(range(N, M), lp2(M-N) - 1, lp2(M-N)/2)
    printTree(tree1)

