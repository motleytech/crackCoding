'''recursive solution to the towers of hanoi problem'''

def solveHanoi(towers, k, a, b, c):
    'recursively solve the towers of hanoi'
    if k == 1:
        towers[b].append(towers[a].pop())
        return
    solveHanoi(towers, k-1, a, c, b)
    solveHanoi(towers, 1, a, b, c)
    solveHanoi(towers, k-1, c, b, a)

def test_solveHanoi():
    'test for solveHanoi'
    for N in range(2, 10):
        towers = [range(N), [], []]

        solveHanoi(towers, N, 0, 2, 1)
        assert towers[2] == range(N)
        print 'Solved case %s' % N

    print 'Test passed'

if __name__ == '__main__':
    test_solveHanoi()
