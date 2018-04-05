
# given (x1, y1, x2, y2) and (a1, b1, a2, b2),
# find intersection point

# check for infinite slope (y1 == y2) or (b1 == b2)
# if so, then do something, else something else

# order endpoints

# if slopes are same, look for endpoint overlap
  # if slope is infinite, check if same x, and look for overlap at endpoints
  # else, figure out Cs and if lines overlap, check overlap at start endpoints
# else
  # if slope of one is infinite, get x value. From x, get y for the other line, and see if this y falls within known ys
  # else, solve the 2 equations to find the point.

import math

inf = float('Inf')

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return '(%s, %s)' % (self.x, self.y)

    def __str__(self):
        return self.__repr__()

    def __gt__(self, other):
        if self.x > other.x:
            return True
        if self.x == other.x and self.y > other.y:
            return True
        return False

    def __eq__(self, other):
        if isinstance(other, tuple):
            return self.x, self.y == other
        return self.x, self.y == other.x, other.y

def getSlope(a, b):
    if b.x == a.x:
        m1 = inf
    else:
        m1 = float(b.y - a.y) / (b.x - a.x)
    return m1

def getIntrc(a, m):
    return (a.y - m * a.x)


def findIntersection(p1, p2, p3, p4):
    if p1 > p2:
        p1, p2 = p2, p1
    if p3 > p4:
        p3, p4 = p4, p3

    m1, m2 = getSlope(p1, p2), getSlope(p3, p4)

    if m1 > m2:
        m1, m2 = m2, m1
        p1, p2, p3, p4 = p3, p4, p1, p2


    if m1 == m2:
        if m1 == inf:
            if p1.x == p3.x:
                # either p1 is between p3 and p4
                if p3.y <= p1.y <= p4.y:
                    return p1
                # p3 is between p1 and p2
                if p1.y <= p3.y <= p2.y:
                    return p3
        else:
            c1, c2 = getIntrc(p1, m1), getIntrc(p3, m2)
            if c1 == c2:
                # if same Cs, then check overlap at endpoints again
                if p3.x <= p1.x <= p4.x:
                    return p1
                if p1.x <= p3.x <= p2.x:
                    return p3
    else:
        if m2 == inf:
            x2 = p3.x
            c1 = getIntrc(p1, m1)
            y1 = m1 * x2 + c1
            if p3.y <= y1 <= p4.y:
                return (p3.x, y1)
        else:
            c1, c2 = getIntrc(p1, m1), getIntrc(p3, m2)
            x = (c2 - c1) / (m1 - m2)
            if (p1.x <= x <= p2.x) and (p3.x <= x <= p4.x):
                y = m1 * x + c1
                return (x, y)
    return None


def test():
    # intersecting lines
    pa = Point(0, 0)
    pb = Point(5, 0)
    pc = Point(0, 1)
    pd = Point(5, -1)

    res = findIntersection(pa, pb, pc, pd)
    print res
    assert res == (2.5, 0.0)

    pa = Point(0, 0)
    pb = Point(0, 5)
    pc = Point(-1, 0)
    pd = Point(1, 5)

    res = findIntersection(pa, pb, pc, pd)
    print res
    assert res == (0.0, 2.5)

    # non-intersecting lines
    pa = Point(0, 0)
    pb = Point(5, 0)
    pc = Point(0, 4)
    pd = Point(5, 1)

    res = findIntersection(pa, pb, pc, pd)
    print res
    assert res == None

    # parallel
    pa = Point(0, 0)
    pb = Point(5, 5)
    pc = Point(-1, 1)
    pd = Point(4, 6)

    res = findIntersection(pa, pb, pc, pd)
    print res
    assert res == None

    # overlapping
    pa = Point(0, 0)
    pb = Point(5, 5)
    pc = Point(-1, -1)
    pd = Point(4, 4)

    res = findIntersection(pa, pb, pc, pd)
    print res
    assert res == (0, 0)






if __name__ == '__main__':
    test()

