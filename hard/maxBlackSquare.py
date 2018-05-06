'solution for the max black square problem'

def findlbss(data):
    'find left bottom corners for squares'
    r, c = len(data), len(data[0])
    lbss = []
    for i, row in enumerate(data):
        if i == r - 1:
            continue
        for j, d in enumerate(row):
            if j == c - 1:
                continue
            if d == 0 and data[i+1][j] == 0 and data[i][j+1] == 0:
                sr, sc = 2, 2
                while i + sr < r:
                    if data[i+sr][j] == 0:
                        sr += 1
                    else:
                        break
                while j + sc < c:
                    if data[i][j+sc] == 0:
                        sc += 1
                    else:
                        break
                ss = min(sr, sc)
                lbss.append((i, j, ss))
    return lbss

def findrtss(data):
    'find right top corners for squares'
    rtss = []
    for i, row in enumerate(data):
        if i == 0:
            continue
        for j, d in enumerate(row):
            if j == 0:
                continue
            if d == 0 and data[i-1][j] == 0 and data[i][j-1] == 0:
                sr, sc = 2, 2
                while i - sr >= 0:
                    if data[i-sr][j] == 0:
                        sr += 1
                    else:
                        break
                while j - sc >= 0:
                    if data[i][j-sc] == 0:
                        sc += 1
                    else:
                        break
                ss = min(sr, sc)
                rtss.append((i, j, ss))
    return rtss


def getMaxBlackSquare(data):
    'method to solve the max black square problem'


    # find all left bottom locations and find the max sq size
    lbss = findlbss(data)

    # find all right top locations and find the max sq size
    rtss = findrtss(data)

    rtssDict = dict(((r, c), s) for r, c, s in rtss)

    # for each left bottom, check for the farthest right top using bisection in the diagonal list

    found = None
    ms = 0
    for r, c, s1 in lbss:
        for ss in range(s1-1, 0, -1):
            if (r+ss, c+ss) in rtssDict:
                s2 = rtssDict[(r+ss, c+ss)]
                if s2 > ss and ss > ms-1:
                    ms = ss + 1
                    found = (r, c)
                    break
    return (found, ms)


def test():
    'test for the getMaxBlackSquare method'
    from pprint import pprint as pp

    N = 5
    data = [[0]*N for _ in range(N)]

    data[1][0] = 1
    data[0][1] = 1
    data[4][4] = 1


    pp(data)
    res = getMaxBlackSquare(data)
    print res
    assert res == ((0, 2), 3)

if __name__ == '__main__':
    test()
    print 'Passed'

