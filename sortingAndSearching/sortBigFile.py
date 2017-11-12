'Method to implement an external sort using bubble merging'


import os


def sortBigFile(fname, foname, maxmem):
    '''sort lines in fname and output the sorted foname file
    using upto maxmem'''
    tname = '/tmp/tname1.txt'
    csize = maxmem / 5
    # first create sorted chunks, then merge those chunks
    clines = createSortedChunks(fname, tname, csize)

    if len(clines) <= 3:
        os.rename(tname, foname)
        return True, 1

    tname2, passes = sortChunks(tname, csize, clines)
    os.rename(tname2, foname)
    return True, passes


def areEmpty(la, lb, ia, ib):
    'true if la and lb have both been exhausted'
    if ia == len(la) and ib == len(lb):
        return True
    return False


def getNext(la, lb, ia, ib):
    'return the next smallest element between la & lb'
    if ib == len(lb) and ia != len(la):
        return la[ia], ia+1, ib, False
    if ia == len(la) and ib != len(lb):
        return lb[ib], ia, ib+1, False
    if la[ia] <= lb[ib]:
        return la[ia], ia+1, ib, False
    return lb[ib], ia, ib+1, True


def mergeChunks(achunk, bchunk, csize):
    'merge 2 chunks and returns sorted result'
    cchunk, dchunk = [], []
    msize = 0
    i, j = 0, 0
    didSwap = False
    while True:
        if areEmpty(achunk, bchunk, i, j):
            break
        line, i, j, swap = getNext(achunk, bchunk, i, j)
        msize += len(line)
        if swap:
            didSwap = True
        if msize <= csize:
            cchunk.append(line)
        else:
            dchunk.append(line)
    return cchunk, dchunk, didSwap


def sortChunks(tname, csize, clines):
    'bubble merge and sort the chunks'
    changed = True
    t2name = '/tmp/tname2.txt'
    passes = 0
    while changed:
        changed = False
        thandle = open(tname)
        t2handle = open(t2name, 'w')
        currChunk = 0
        achunk = [thandle.readline().strip() for _ in range(clines[currChunk])]
        while True:
            currChunk += 1
            if clines[currChunk] == 0:
                bchunk = []
            else:
                bchunk = [thandle.readline().strip() for _ in range(clines[currChunk])]

            cchunk, achunk, mods = mergeChunks(achunk, bchunk, csize)
            if mods:
                changed = True

            clines[currChunk - 1] = len(cchunk)
            for line in cchunk:
                t2handle.write(line + '\n')

            if len(achunk) == 0 and clines[currChunk+1] == 0:
                clines[currChunk] = 0
                break

        t2handle.close()
        thandle.close()
        os.remove(tname)
        os.rename(t2name, tname)
        passes += 1
    return tname, passes


def createSortedChunks(fname, oname, csize):
    'initial chunk creation and sorting'
    clines = []
    cindex = 0
    fhandle = open(fname)
    ohandle = open(oname, 'w')
    extra = None
    bytesRead = 0

    EOF = False
    while not EOF:
        cindex += 1
        nextBoundary = cindex*csize
        lines = []

        if extra is not None:
            lines.append(extra)
            bytesRead += len(extra)
        extra = None

        while bytesRead < nextBoundary:
            line = fhandle.readline()
            if line == '':
                EOF = True
                break
            lines.append(line)
            bytesRead += len(line)

        if bytesRead > nextBoundary:
            lastLine = lines.pop()
            extra = lastLine
            bytesRead -= len(lastLine)

        lines.sort()

        for line in lines:
            ohandle.write(line)
        clines.append(len(lines))

    fhandle.close()
    ohandle.close()
    clines.extend([0, 0])
    return clines


def createTestFile(fname):
    'create a test file for input to sortBigFile'
    from random import choice
    spaces = 3
    nchars = 26
    ncs = nchars + spaces

    charsWS = range(ncs)
    chars26 = range(nchars)

    charMap = {}
    orda = ord('a')
    for x in range(nchars):
        charMap[x] = chr(x + orda)
    for y in range(nchars, ncs):
        charMap[y] = ' '


    if os.path.exists(fname):
        return
    f1 = open(fname, 'w')
    for x in range(1000):
        length = 20
        statement = charMap[choice(chars26)] + \
            ''.join(charMap[choice(charsWS)] for z in range(length - 1)) + '\n'
        f1.write(statement)

    f1.close()


def test_sortBigFile():
    'main test function'
    # create random lines

    fpath = '/tmp/file1.txt'
    if os.path.exists(fpath):
        os.remove(fpath)
    createTestFile(fpath)

    fopath = '/tmp/file2.txt'
    if os.path.exists(fopath):
        os.remove(fopath)

    _, passes = sortBigFile(fpath, fopath, 4000)

    print 'Number of passes : %s' % passes

    # verify that file is sorted
    inp1 = open(fpath).readlines()
    inp1.sort()

    inp2 = open(fopath).readlines()

    match = True
    for x, y in zip(inp1, inp2):
        if x.strip() != y.strip():
            print "Error:\n%s\n%s" % (x.strip(), y.strip())
            match = False
            break

    if match:
        print 'Test Passed'
    else:
        print 'Test FAILED'


if __name__ == '__main__':
    test_sortBigFile()

