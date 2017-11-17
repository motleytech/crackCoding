'search for an item in a sorted matrix'

import bisect

NOT_FOUND = (False, (None, None))

def transpose(mat, r, s):
    'returns the transpose of a matrix'
    nmat = []
    for y in range(s):
        row = []
        nmat.append(row)
        for x in range(r):
            row.append(mat[x][y])
    return nmat

def getSortedMatrix(n, m):
    'creates and returns a sorted matrix'
    r, s = n, m
    if n > m:
        r, s = m, n

    row = []
    last = 0
    for x in range(1, r+1):
        curr = last + x
        row.append(curr)
        last = curr

    for x in range(r+1, s+1):
        curr = last + r
        row.append(curr)
        last = curr

    for y in range(r, 0, -1):
        curr = last + y
        row.append(curr)
        last = curr

    mat = [[(y - x) for y in row[x:x+s]] for x in range(0, n)]

    if n > m:
        mat = transpose(mat, r, s)
    return mat

class MatDiagToList(object):
    'allows indexing the diag of a matrix like a list'
    def __init__(self, mat, sx, sy, nels):
        self.mat = mat
        self.sx = sx
        self.sy = sy
        self.nels = nels

    def __getitem__(self, x):
        if x < 0:
            x = self.nels = x

        if x >= self.nels:
            raise IndexError

        return self.mat[self.sx + x][self.sy + x]

    def __len__(self):
        return self.nels

class MatSeqToList(object):
    'allows indexing a row/col of a matrix like a list'
    def __init__(self, mat, sx, sy, ex, ey):
        self.mat = mat
        self.sx = sx
        self.sy = sy
        self.ex = ex
        self.ey = ey
        self.nels = max(ex - sx, ey - sy) + 1
        self.dxy = True if ex > sx else False

    def __getitem__(self, offset):
        if offset < 0:
            offset = self.nels - offset

        if offset >= self.nels:
            raise IndexError

        if self.dxy:
            return self.mat[self.sx+offset][self.sy]
        return self.mat[self.sx][self.sy+offset]

    def __len__(self):
        return self.nels

def linBSearch(mat, t, sx, sy, ex, ey):
    'search for element in a linear part of the matrix'
    mlen = max(ex - sx, ey - sy) + 1
    pos = bisect.bisect_left(MatSeqToList(mat, sx, sy, ex, ey), t)
    if pos >= mlen:
        return NOT_FOUND
    if sx == ex:
        if mat[sx][sy + pos] == t:
            return True, (sx, sy + pos)
        return NOT_FOUND

    if mat[sx + pos][sy] == t:
        return True, (sx + pos, sy)
    return NOT_FOUND

def findInMatRecur(mat, t, sx, sy, ex, ey):
    'search for the element t in the submatrix'
    if sx > ex or sy > ey:
        return NOT_FOUND
    if ex - sx == 0 or ey - sy == 0:
        return linBSearch(mat, t, sx, sy, ex, ey)

    nels = min(ex - sx, ey - sy) + 1
    pos = bisect.bisect_left(MatDiagToList(mat, sx, sy, nels), t)

    if pos == 0 and mat[sx][sy] != t:
        return NOT_FOUND

    cx, cy = sx + pos, sy + pos

    if pos < nels and mat[cx][cy] == t:
        return True, (cx, cy)

    res, pxy = findInMatRecur(mat, t, cx, sy, ex, cy-1)
    if res:
        return res, pxy
    return findInMatRecur(mat, t, sx, cy, cx-1, ey)

def findInMatrix(mat, t):
    'search for element t in the matrix'
    r, s = len(mat), len(mat[0])
    return findInMatRecur(mat, t, 0, 0, r-1, s-1)

def test_findInMatrix():
    'test for findInMatrix method'
    m, n = 12, 5
    mat = getSortedMatrix(m, n)

    for x in range(len(mat)):
        for y in range(len(mat[0])):
            el = mat[x][y]
            res, (sx, sy) = findInMatrix(mat, el)
            assert res and x == sx and y == sy

    res, (sx, sy) = findInMatrix(mat, -20)
    assert (not res) and (sx == None) and (sy == None)
    res, (sx, sy) = findInMatrix(mat, m * n + 20)
    assert (not res) and (sx == None) and (sy == None)
    print 'Test Passed'

if __name__ == '__main__':
    test_findInMatrix()



