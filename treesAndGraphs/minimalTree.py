'''Given a sorted (increasing order) array with
   unique integer elements, write an algorithm to
   create a binary search tree with minimal height.'''

import math

class Node(object):
    '''the binary tree node class'''
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return self.__str__()


def lp2(n):
    'return the highest power of 2 <= n'
    return pow(2, int(math.log(n, 2) + 0.001))


def createTree(data, index, jumpValue, node=None):
    '''creates a minimal height binary search tree from
    given sorted list'''
    if not node:
        node = Node(data[index])
    if jumpValue >= 1:
        nodel = Node(data[index-jumpValue])
        node.left = nodel
        createTree(data, index-jumpValue, jumpValue/2, nodel)

        while jumpValue > 0 and index + jumpValue >= len(data):
            jumpValue = jumpValue / 2
        if jumpValue == 0:
            return
        noder = Node(data[index+jumpValue])
        node.right = noder
        createTree(data, index+jumpValue, jumpValue/2, noder)
    return node


if __name__ == '__main__':
    N, M = 0, 41
    print 'max power of 2 : %s' % lp2(M-N)
    tree = createTree(range(N, M), lp2(M-N) - 1, lp2(M-N)/2)
    from printTree import printTree
    printTree(tree)


