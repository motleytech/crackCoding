'''
Given an MxN matrix, for every 0 element in the matrix,
make the entire row and column of those elements 0.
'''

def rowColZero(mat):
    '''
    for each zero element, zero out the whole row and
    column for that element
    '''
    M, N = len(mat), len(mat[0])
    # create sets of rows and columns that need to be zeroed
    rzeros, czeros = set(), set()
    for x in range(M):
        for y in range(N):
            if mat[x][y] == 0:
                rzeros.add(x)
                czeros.add(y)

    # zero out rows
    for r in rzeros:
        for c in range(N):
            mat[r][c] = 0

    # zero out columns
    for r in range(M):
        for c in czeros:
            mat[r][c] = 0

    return mat

def test_rowColZero():
    '''
    test for the rowColZero method
    '''
    print 'Testing rowColZero...',

    m = [[1, 2], [3, 0]]
    m2 = [[1, 0], [0, 0]]
    rowColZero(m)
    assert m == m2

    m = [[1, 2, 3], [3, 0, 1]]
    m2 = [[1, 0, 3], [0, 0, 0]]
    rowColZero(m)
    assert m == m2
    print 'Passed'

if __name__ == '__main__':
    test_rowColZero()
