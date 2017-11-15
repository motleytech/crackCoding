'find missing int in a large file with less memory usage'

import numpy as np
from missingInt1 import FileLineIterator, genMissing

def genMissingIntBig(fpath, maxMem, llimit, ulimit):
    '''find a missing int using only maxMem memory.
    Only works if ulimit - llimit < maxMem ^ 2.
    We will have to use a different strategy if that's not the case'''
    binSize = maxMem * 6
    numInts = ulimit - llimit + 1

    nBuckets = numInts / binSize + 1
    arr = np.array([0]*nBuckets, np.int32)

    fh = open(fpath)
    i = 0
    for i in FileLineIterator(fh):
        arr[(i - llimit) / binSize] += 1

    for x in arr:
        if x < binSize:
            return genMissing(FileLineIterator(fh), llimit, ulimit)
    return i + 1


def test_genMissingIntBig():
    'test for genMissingIntBig'
    import random

    inp = range(1024, 2048)
    a = random.randint(0, len(inp)-1)
    b = random.randint(0, len(inp)-1)
    while b == a:
        b = random.randint(0, len(inp)-1)

    #inp[a] = inp[b]

    fname = '/tmp/intfilebig.txt'
    fh = open(fname, 'w')
    for x in inp:
        fh.write(str(x) + '\n')
    fh.close()

    res = genMissingIntBig(fname, 24, 1024, 2048)
    assert (res == a + 1024) or (res == 2048), "%s != %s" % (res, a)

    print '%s missing.\n\nTest passed' % res

if __name__ == '__main__':
    test_genMissingIntBig()






