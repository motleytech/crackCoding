'implementation of TreeWithRank class'


class TreeWithRank(object):
    'the tree node with rank'
    def __init__(self, data):
        self.data = data
        self.rank = 0
        self.count = 1
        self.left = self.right = None

    def insert(self, data):
        'insert data into/below the tree node'
        if self.data == data:
            self.count += 1
            return
        if data < self.data:
            self.rank += 1
            if self.left == None:
                self.left = TreeWithRank(data)
            else:
                self.left.insert(data)
        else:
            if self.right == None:
                self.right = TreeWithRank(data)
            else:
                self.right.insert(data)
        return

    def getRank(self, data):
        'get the rank of data'
        if data < self.data:
            if self.left:
                return self.left.getRank(data)
            return 0
        if data > self.data:
            if self.right:
                return self.rank + self.count + self.right.getRank(data)
            return self.rank + self.count
        return self.rank + self.count - 1


def test_TreeWithRank():
    'test for TreeWithRank'
    inp = [5, 1, 4, 4, 5, 9, 7, 13, 3]
    root = None

    for x in inp:
        if root is None:
            root = TreeWithRank(x)
        else:
            root.insert(x)

    assert root.getRank(1) == 0
    assert root.getRank(3) == 1
    assert root.getRank(4) == 3
    assert root.getRank(5) == 5
    assert root.getRank(13) == 8
    assert root.getRank(14) == 9

    print 'Test Passed'

if __name__ == '__main__':
    test_TreeWithRank()



