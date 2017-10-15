'''find highest stacking of boxes'''

gMaxHeight = [(0, tuple())]

def canStack(box1, box2):
    'can box2 be stacked on top of box1'
    if box2.length >= box1.length:
        return False
    if box2.width >= box1.width:
        return False
    if box2.height >= box1.height:
        return False
    return True


def stackEm(remaining, stack, height):
    'find highest stacking using backtracking'
    if height > gMaxHeight[0][0]:
        gMaxHeight[0] = (height, tuple(stack))

    for box in remaining.copy():
        if len(stack) == 0 or canStack(box, stack[-1]):
            stack.append(box)
            remaining.remove(box)

            stackEm(remaining, stack, height + box.height)

            remaining.add(box)
            stack.pop()
            continue


def getMaxStackedBoxesHeight(boxes):
    'return highest stack height'
    gMaxHeight[0] = (0, tuple())
    stackEm(set(boxes), [], 0)
    return gMaxHeight[0]

def stackEmBrute(boxes):
    'brute force way to find highest stack'
    from itertools import permutations
    maxHeight = 0
    for x in permutations(boxes):
        currHeight = x[0].height

        for a, b in zip(x, x[1:]):
            if canStack(a, b):
                currHeight += b.height
            else:
                break
        if currHeight > maxHeight:
            maxHeight = currHeight
    return maxHeight


def test_maxStackHeight():
    'test for getMaxStackedBoxesHeight against brute force solution'
    from random import randint, seed
    from pprint import pprint as pp

    if 0:
        randSeed = randint(1, 10000)
        print 'Seed = %s' % randSeed
    else:
        randSeed = 9994
    seed(randSeed)

    class Box(object):
        'box class definition'
        def __init__(self, l, w, h):
            self.length = l
            self.width = w
            self.height = h

        def __repr__(self):
            return 'Box(%s, %s, %s)' % (self.length, self.width, self.height)

    M = 20
    N = 10
    boxes = [Box(randint(1, M), randint(1, M), randint(1, M)) for _ in range(N)]
    mxHeight = getMaxStackedBoxesHeight(boxes)

    pp(boxes)

    r1, r2 = mxHeight[0], stackEmBrute(boxes)

    print r1, r2

    assert r1 == r2
    print 'Test Passed'

if __name__ == '__main__':
    test_maxStackHeight()

