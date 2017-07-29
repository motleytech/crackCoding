from copy import deepcopy
from time import time
import random
from sdkInput import easy, medium, hard

def updateRow(possb, pos, val):
    rr = pos/9
    for ov in xrange(rr*9, (rr+1)*9):
        if val in possb[ov]:
            if len(possb[ov]) == 1:
                return False
            possb[ov].remove(val)

def updateCol(possb, pos, val):
    cc = pos%9
    for ov in xrange(cc, 81, 9):
        if val in possb[ov]:
            if len(possb[ov]) == 1:
                return False
            possb[ov].remove(val)

def updateCell(possb, pos, val):
    sc = (pos/27)*27 + ((pos%9)/3)*3
    for addv in (0, 1, 2, 9, 10, 11, 18, 19, 20):
        scv = sc + addv
        if val in possb[scv]:
            if len(possb[scv]) == 1:
                return False
            possb[scv].remove(val)

def updateAll(possb, pos, val):
    if updateRow(possb, pos, val) is False:
        return False
    if updateCol(possb, pos, val) is False:
        return False
    if updateCell(possb, pos, val) is False:
        return False

    return True


def initPossibilities(possb, ins):
    for rr in xrange(9):
        for cc in xrange(9):
            pos = rr*9 + cc
            val = ins[pos]
            if val != 0:
                # update row, col and cell
                possb[pos] = set()

                # update all
                if updateAll(possb, pos, val) is False:
                    print "Failed in initializing possibilities"
                    return False
    return possb

def solveSudoku(possb, ss):
    changed = True
    while changed:
        changed = False
        for pos in xrange(81):
            if len(possb[pos]) == 1:
                changed = True
                val = possb[pos].pop()
                ss[pos] = val
                if updateAll(possb, pos, val) is False:
                    return False

    guessPos = None
    for pos in xrange(81):
        if len(possb[pos]) > 1:
            guessPos = pos
            break

    if guessPos is None:
        return ss

    ss2 = deepcopy(ss)
    guessValues = list(possb[guessPos])
    random.shuffle(guessValues)
    for guess in guessValues:
        possb2 = deepcopy(possb)
        possb2[guessPos] = set()
        ss2[guessPos] = guess
        if updateAll(possb2, guessPos, guess) is False:
            return False
        retVal = solveSudoku(possb2, ss2)
        if retVal is not False:
            return retVal
    return False


def getCell(sdk, cell):
    cs = (cell/3)*27 + (cell%3)*3
    return [sdk[cs + x] for x in (0,1,2,9,10,11,18,19,20)]

def checkSolution(outs):
    # every row
    set9 = set(xrange(1,10))
    for rr in range(9):
        assert set9 == set([outs[rr*9 + x] for x in xrange(9)])

    for cc in xrange(9):
        assert set9 == set([outs[x*9 + cc] for x in xrange(9)])

    for cell in xrange(9):
        assert set9 == set(getCell(outs, cell))

    return "Solution checks out..."


def formatSudoku(outs):
    data = [str(x) for x in outs]
    data = [' '.join(data[x*3:(x+1)*3]) for x in range(27)]
    data = ['   '.join(data[x*3:(x+1)*3]) for x in range(9)]
    data = ['\n'.join(data[x*3:(x+1)*3]) for x in range(3)]
    data = '\n\n'.join(data)
    return '\n' + data + '\n'


def stringToList(inp):
    inp = inp.replace('.', '0')
    return [int(x) for x in inp]

def listToString(inp):
    return "".join(str(x) for x in inp)

def runTests(cases):
    for inp, outp in cases.items():
        if True:
            inp = inp.replace('0', '.')
            sudokuInput = stringToList(inp)
            possibilities = [set(range(1,10)) for x in xrange(9) for y in xrange(9)]
            possb = initPossibilities(possibilities, sudokuInput)
            if possb is False:
                print "No possibilities found"
                continue

            st = time()
            result = solveSudoku(possb, sudokuInput)
            et = time()

            if result is False:
                print "\nFailed to find solution"
                continue
            else:
                checkSolution(result)
                print "Elapsed %10.6f seconds" % (et - st)

            if listToString(result) != outp:
                raise "Test failed."

st1 = time()
runTests(easy)
print '\n\nEasy Elapsed time : %10.6fs\n' % (time() - st1)


st1 = time()
runTests(medium)
print '\n\nMedium Elapsed time : %10.6fs\n' % (time() - st1)


st1 = time()
runTests(hard)
print '\n\nHard Elapsed time : %10.6fs\n' % (time() - st1)
