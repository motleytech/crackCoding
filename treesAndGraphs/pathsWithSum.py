

def pathsWithSums(target, node, sums, cpath, paths):
    value = node.data

    cpath.append(value)
    sums.append(0)
    count = len(sums)
    for i in range(count):
        sums[i] += value
        if sums[i] == target:
            paths.append(cpath[i:])

    if node.left:
        pathsWithSums(target, node.left, sums, cpath, paths)
    if node.right:
        pathsWithSums(target, node.right, sums, cpath, paths)

    for i in range(count):
        sums[i] -= value

    sums.pop()
    cpath.pop()

def pathsWithSums2(target, node, sums, sumsMap, pathCount):
    sums.append(node.data)
    sums[-1] += sums[-2]
    sumsMap[sums[-1]].append(0)

    if (sums[-1] - target) in sumsMap:
        pathCount[0] += len(sumsMap[sums[-1] - target])

    if node.left:
        pathsWithSums2(target, node.left, sums, sumsMap, pathCount)
    if node.right:
        pathsWithSums2(target, node.right, sums, sumsMap, pathCount)

    sumsMap[sums[-1]].remove(0)
    sums.pop()


def test_pathsWithSums():
    from minimalTree import createTree, lp2
    from printTree import printTree
    from random import randint
    from collections import defaultdict

    N, M = 0, 400
    values = sorted([randint(0, 50) for x in range(N, M)])
    tree = createTree(values, lp2(M-N) - 1, lp2(M-N)/2)
    #printTree(tree)

    paths = []
    target = 52
    pathsWithSums(target, tree, [], [], paths)
    print len(paths)
    v1 = len(paths)

    #for x in paths:
        #assert sum(x) == target
        #print x, sum(x)


    pathCount = [0]
    target = 52
    pathsWithSums2(target, tree, [0], defaultdict(lambda: []), pathCount)
    print pathCount[0], '\n'
    v2 = pathCount[0]
    assert v1 == v2


if __name__ == '__main__':
    test_pathsWithSums()
