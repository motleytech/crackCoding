'''check for winner in a tic tac toe game'''

def checkWin(game):
    'find winners in a tic tac toe game'
    winners = set()

    # check rows
    for row in range(3):
        rowEnt = set()
        for col in range(3):
            rowEnt.add(game[row][col])
        if len(rowEnt) == 1 and '' not in rowEnt:
            winners.add(list(rowEnt)[0])

    # check cols
    for col in range(3):
        colEnt = set()
        for row in range(3):
            colEnt.add(game[row][col])
        if len(colEnt) == 1 and '' not in colEnt:
            winners.add(list(colEnt)[0])

    # check diagonals
    diagEnt = set()
    for diag in range(3):
        diagEnt.add(game[diag][diag])
    if len(diagEnt) == 1 and '' not in diagEnt:
        winners.add(list(diagEnt)[0])

    diagEnt = set()
    for diag in range(3):
        diagEnt.add(game[diag][2-diag])
    if len(diagEnt) == 1 and '' not in diagEnt:
        winners.add(list(diagEnt)[0])

    if winners:
        return True, list(winners)
    return False, []


def test():
    'test for checkWin method'
    game = [['x', '', ''], ['o', 'x', 'o'], ['', '', 'x']]
    res = checkWin(game)
    assert res == (True, ['x'])

    game = [['x', '', ''], ['o', 'x', 'o'], ['', '', 'x']]
    assert checkWin(game) == (True, ['x'])

    game = [['x', '', ''], ['x', 'o', 'o'], ['x', '', 'x']]
    assert checkWin(game) == (True, ['x'])

    game = [['x', '', 'o'], ['o', 'x', 'o'], ['', '', 'o']]
    assert checkWin(game) == (True, ['o'])

    game = [['x', '', 'o'], ['o', 'x', 'x'], ['', '', 'o']]
    assert checkWin(game) == (False, [])

    game = [['x', 'x', 'o'], ['x', 'x', 'o'], ['x', 'o', 'o']]
    assert checkWin(game) == (True, ['x', 'o'])

    print 'Done'

if __name__ == '__main__':
    test()
