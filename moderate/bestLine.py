'''
find the line which passes through max number of points
'''

from collections import defaultdict
from itertools import combinations

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

def getBestLine(pts):
    lineDict = defaultdict(lambda : 0)

    for p1, p2 in combinations(pts, 2):
        lineDict[getLine(p1, p2)] += 1

    lPoints, line = sorted(((y, x) for x, y in lineDict.items()), reverse=True)[0]
    #print lPoints, line
    return line

def test():
    points = [(0, 0), (5, 0), (0, 5), (5, 5), (2, 2), (3, 3), (4, 4), (6, -1), (7, -2), (8, -3), (9, -4)]
    assert getBestLine(points) == (-1.0, 5.0)
    print 'done'

if __name__ == '__main__':
    test()




