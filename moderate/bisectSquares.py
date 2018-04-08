'''
find a line that bisects 2 given squares

The key idea - a line that bisects a square must pass
through the center of the square.

Thus the line through the centers of the two squares
is the required solution.

If both squares have the same center, any line passing
through the center suffices.
'''

INF = float('inf')

def getLine(p1, p2):
    '''
    returns (m, c) for a line (y = mx + c)
    in case of m==INF (vertical line), c corresponds to the x offset
    '''
    if p2[0] == p1[0]:
        return (INF, p1[0])
    # from y = y1 + (x - x1) * (y2 - y1) / (x2 - x1)
    m = float(p2[1] - p1[1]) / (p2[0] - p1[0])
    c = p1[1] - m*p1[0]
    return (m, c)

def getBisectingLine(sq1, sq2):
    'returns a pair of points on the bisecting line '
    p11, p12 = sq1
    p21, p22 = sq2
    p1c = tuple([float(p11[x] + p12[x])/2 for x in range(2)])
    p2c = tuple([float(p21[x] + p22[x])/2 for x in range(2)])
    if p1c == p2c:
        result = (p1c, (p1c[0] + 1, p1c[1]))
    else:
        result = (p1c, p2c)

    return getLine(*result)

def test():
    'test for getBisectinLine method'
    sq1 = ((0, 0), (1, 1))
    sq2 = ((1, 1), (2, 2))

    assert getBisectingLine(sq1, sq2) == (1.0, 0)

    sq1 = ((0, 0), (1, 1))
    sq2 = ((1, 0), (2, 1))

    assert getBisectingLine(sq1, sq2) == (0, 0.5)

    sq1 = ((0, 0), (1, 1))
    sq2 = ((0, 1), (1, 2))

    assert getBisectingLine(sq1, sq2) == (INF, 0.5)

    sq1 = ((1, 1), (2, 2))
    sq2 = ((0, 0), (3, 3))

    assert getBisectingLine(sq1, sq2) == (0, 1.5)

    print 'done'

if __name__ == '__main__':
    test()
