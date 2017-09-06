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


N = 10
print 'max power of 2 : %s' % lp2(N)
tree = createTree(range(0, N), lp2(N) - 1, lp2(N)/2)

def printTree(tree):
    # tbd
    pass


