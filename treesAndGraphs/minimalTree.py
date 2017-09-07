# Given a sorted (increasing order) array with unique integer elements, write an algo- rithm to create a binary search tree with minimal height.

# in order filling of nodes
# left
# root
# right
# up

import math

class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

    def __str__(self):
        return str(self.data)


def lp2(n):
    return pow(2, int(math.log(n, 2) + 0.001))


def createTree(data, index, jumpValue, node=None):
    if not node:
        node = Node(data[index])
        print 'Node %s' % node.data
    if jumpValue >= 1:
        nodel = Node(data[index-jumpValue])
        node.left = nodel
        print 'Left %s' % nodel.data
        createTree(data, index-jumpValue, jumpValue/2, nodel)

        while jumpValue > 0 and index + jumpValue >= len(data):
            jumpValue = jumpValue / 2
        if jumpValue == 0:
            return
        noder = Node(data[index+jumpValue])
        node.right = noder
        print 'Right %s' % noder.data
        createTree(data, index+jumpValue, jumpValue/2, noder)
    return node


if __name__ == '__main__':
    N, M = 0, 41
    print 'max power of 2 : %s' % lp2(M-N)
    tree = createTree(range(N, M), lp2(M-N) - 1, lp2(M-N)/2)
    from printTree import printTree
    printTree(tree)


