'print the last k lines from an input file'

def getLastkLines(fpath, k):
    'given a filepath, returns the last k lines from file'
    total = 0
    currk, lastk = [None]*k, [None]*k
    csize = 0

    fHandle = open(fpath)
    while True:
        line = fHandle.readline()
        if line == '':
            break
        total += 1
        currk[csize] = line
        csize += 1
        if csize == k:
            lastk = currk
            currk = [None]*k
            csize = 0
    if csize == k:
        return currk
    else:
        if total >= k:
            return lastk[-(k-csize):] + currk[:csize]
        else:
            return currk[:csize]


def printLastkLines(fpath, k):
    'given filepath, prints the last k lines from file'
    lastk = getLastkLines(fpath, k)
    print "".join(lastk)


def test_printLastkLines():
    'test for printLastkLines'
    fpath = '/tmp/plkl.txt'
    k = 30
    total = 150
    with open(fpath, 'w') as fh:
        for x in range(total):
            fh.write('%s\n' % x)

    lastk = getLastkLines(fpath, k)

    print lastk
    assert lastk == ['%s\n'%x for x in range(total-k, total)]
    print 'Test passed'


if __name__ == '__main__':
    test_printLastkLines()

