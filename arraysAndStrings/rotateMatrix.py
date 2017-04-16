'''
rotate a given NxN matrix by 90 degrees in the anti clockwise direction
'''

def rotate90ccw(m):
    '''
    rotate the NxN matrix m 90 degrees in the ccw direction
    (using constant extra space)
    '''
    N = len(m)
    crange = N/2
    rrange = crange if N % 2 == 0 else crange + 1

    for a in range(rrange):
        for b in range(crange):
            temp = m[a][b]
            x1, y1 = a, b
            for _ign in range(3):
                x2, y2 = y1, N - 1 - x1
                m[x1][y1] = m[x2][y2]
                x1, y1 = x2, y2
            m[x1][y1] = temp

def test_rotate90ccw():
    '''
    test for rotate90ccw
    '''
    from pprint import pprint as _pp
    print 'Testing rotate90ccw...',

    m = [[0, 1], [2, 3]]
    rotate90ccw(m)
    m2 = [[1, 3], [0, 2]]
    assert m == m2

    m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    rotate90ccw(m)
    m2 = [[3, 6, 9], [2, 5, 8], [1, 4, 7]]
    assert m == m2

    m = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]
    rotate90ccw(m)
    m2 = [[3, 7, 11, 15], [2, 6, 10, 14], [1, 5, 9, 13], [0, 4, 8, 12]]
    assert m == m2

    print 'Passed.'

if __name__ == '__main__':
    test_rotate90ccw()
