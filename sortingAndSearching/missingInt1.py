'''generate an integer that's not present in a file'''

import numpy as np
import math

class FileLineIterator(object):
    'iterator which returns integers from file'
    def __init__(self, fh):
        self.fh = fh

    def __iter__(self):
        self.fh.seek(0)
        return self

    def next(self):
        'returns integer from next line'
        line = self.fh.readline()
        if line == '':
            raise StopIteration
        if line[-1] == '\n':
            return int(line[:-1])
        return int(line)

def genMissingFromFile(fpath, llimit, ulimit):
    'returns integer missing from file'
    with open(fpath) as fh:
        fIter = FileLineIterator(fh)
        val = genMissing(fIter, llimit, ulimit)
    return val

def genMissing(inp, llimit, ulimit):
    'returns integer missing from inp'
    arr = np.array([0]*((ulimit - llimit)/32 + 2), np.uint32)

    for x in inp:
        if llimit <= x <= ulimit:
            x = x - llimit
            arr[x/32] |= 1 << (x % 32)

    allOnes = sum(1 << x for x in range(32))
    for i, y in enumerate(arr):
        if y < allOnes:
            z = y ^ allOnes
            rz = z ^ (z & z - 1)
            num = i * 32 + int(math.log(rz, 2))
            return num + llimit
    return None

def test_genMissingFromFile():
    'test for genMissingFromFile'
    import random

    inp = range(1024, 2048)
    a = random.randint(0, len(inp)-1)
    b = random.randint(0, len(inp)-1)
    while b == a:
        b = random.randint(0, len(inp)-1)

    inp[a] = inp[b]

    fname = '/tmp/intfile.txt'
    fh = open(fname, 'w')
    for x in inp:
        fh.write(str(x) + '\n')
    fh.close()

    res = genMissingFromFile(fname, 1024, 2048)
    assert (res == a + 1024) or (res == 1024), "%s != %s" % (res, a)

    print '%s missing.\n\nTest passed' % res

if __name__ == '__main__':
    test_genMissingFromFile()



