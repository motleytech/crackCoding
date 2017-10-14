'''solution for the eight queens problem'''

def placeQueens(occupied, k, remcols, solutions):
    '''n queens solved using backtracking'''
    if k == 8:
        solutions.append(occupied[:])
    for c in remcols.copy():
        clash = False
        for d in range(1, k+1):
            if abs(occupied[k-d] - c) == d:
                clash = True
                break
        if clash:
            continue
        remcols.remove(c)
        occupied[k] = c
        placeQueens(occupied, k+1, remcols, solutions)
        remcols.add(c)

def rotate90(sol):
    '''rotate a given placement by 90 degrees ccw'''
    slen = len(sol) - 1
    solCopy = sol[:]
    for x, y in enumerate(sol):
        solCopy[slen-y] = x
    return solCopy

def reflect(sol):
    'reflect a solution horizontally (about a vertical line)'
    slen = len(sol) - 1
    solCopy = sol[:]
    for x, y in enumerate(sol):
        solCopy[slen-x] = y
    return solCopy

def removeSimilars(sols):
    'remove similar solutions (which are rotations / reflections)'
    toRemove = set()
    numSols = len(sols)
    for i, x in enumerate(sols):
        for j in range(i+1, numSols):
            toMatch = sols[j]
            for _ in range(4):
                toMatch = rotate90(toMatch)
                if x == toMatch:
                    toRemove.add(j)
                    break
            if j in toRemove:
                continue
            toMatch = reflect(toMatch)
            for _ in range(4):
                toMatch = rotate90(toMatch)
                if x == toMatch:
                    toRemove.add(j)
                    break

    newSols = sols[:]
    for i in range(len(newSols)-1, -1, -1):
        if i in toRemove:
            newSols.pop(i)
    return newSols


def test_placeQueens():
    'test for the placeQueens method'
    locations = [0]*8
    solutions = []
    placeQueens(locations, 0, set(range(8)), solutions)

    assert len(solutions) == 92

    newSols = removeSimilars(solutions)

    assert len(newSols) == 12
    print 'Test passed'


if __name__ == '__main__':
    test_placeQueens()
