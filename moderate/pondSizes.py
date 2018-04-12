'''solution for the pond sizes problem'''

from itertools import product

def pondSizes(plot):
    'performs bfs to find separate ponds'
    toVisit = set(range(len(plot)*len(plot[0])))
    parts = []
    while toVisit:
        c = toVisit.pop()
        x, y = c / 4, c % 4
        if plot[x][y]:
            continue

        cpart = [c]
        clist = [c]
        while clist:
            c = clist.pop()
            x, y = c / 4, c % 4
            for (a, b) in product([-1, 0, 1], [-1, 0, 1]):
                x2, y2 = x + a, y + b
                if 0 <= x2 < 4 and 0 <= y2 < 4:
                    c2 = x2*4 + y2
                    if not plot[x2][y2] and c2 in toVisit:
                        toVisit.remove(c2)
                        clist.append(c2)
                        cpart.append(c2)
        parts.append(cpart)
    return [len(p) for p in parts], parts

def test():
    'test for pondSizes method'
    plot = [[0, 2, 1, 0],
            [0, 1, 0, 1],
            [1, 1, 0, 1],
            [0, 1, 0, 1]]

    assert pondSizes(plot) == ([2, 4, 1], [[0, 4], [3, 6, 10, 14], [12]])
    print 'Passed'

if __name__ == '__main__':
    test()
