'implement the paint fill logic'

from Queue import Queue

def fillPaint(grid, x, y, color):
    'starting from x,y fills matching pixels in grid with color'
    toVisit = Queue()
    toVisit.put((x, y))
    oColor = grid[x][y]

    while not toVisit.empty():
        a, b = toVisit.get()
        grid[a][b] = color

        if a < (len(grid)-1) and grid[a+1][b] == oColor:
            toVisit.put((a+1, b))


        if b < (len(grid[a]) - 1) and grid[a][b+1] == oColor:
            toVisit.put((a, b+1))

        if a > 0 and grid[a-1][b] == oColor:
            toVisit.put((a-1, b))

        if b > 0 and grid[a][b-1] == oColor:
            toVisit.put((a, b-1))

def test_fillPaint():
    'test for fillPaint method'
    grid = [[0]*5 for _ in range(5)]
    grid[2][2] = 5
    fillPaint(grid, 0, 0, 1)


    assert grid[3][3] == 1
    assert sum(sum(x) for x in grid) == 29

    grid = [[0]*5 for _ in range(5)]
    fillPaint(grid, 3, 3, 1)

    assert grid[0][0] == 1
    assert sum(sum(_) for _ in grid) == 25

    print 'Test passed'

if __name__ == '__main__':
    test_fillPaint()



