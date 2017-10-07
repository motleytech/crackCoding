'''return ways for robot to go across grid of x,y size'''

def canMove(grid, xx, yy):
    'return true if its possible to move to point xx, yy'
    if xx >= len(grid):
        return False
    if yy >= len(grid[xx]):
        return False
    if grid[xx][yy] == 'offLimit':
        return False
    return True

def findPath(grid, x, y, r, s, path, visited):
    'returns True if path exists'
    path.append((x, y))
    if (x, y) in visited:
        return False

    visited.add((x, y))
    if x == r and y == s:
        return True
    # move right if possible
    if canMove(grid, x, y+1):
        res = findPath(grid, x, y+1, r, s, path, visited)
        if res:
            return True
    if canMove(grid, x+1, y):
        res = findPath(grid, x+1, y, r, s, path, visited)
        if res:
            return True
    path.pop()
    return False

def test_findPath():
    'test for findPath method'
    rows = 5
    cols = 10
    grid = [[0]*cols for _ in range(rows)]

    grid[2][9] = 'offLimit'
    path = []
    visited = set()
    res = findPath(grid, 0, 0, rows-1, cols-1, path, visited)

    if res:
        print 'Path found'
        print path
        print 'Test Passed'
    else:
        print 'No path found'
        print 'Test Failed'

if __name__ == '__main__':
    test_findPath()
