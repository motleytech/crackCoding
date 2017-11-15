'''find duplicates in a given array containing all numbers 1 - 32k,
using only 4k of memory'''

import numpy as np

def findDuplicates(inp):
    'return list of duplicates ... find them using bit mapping'
    bitmap = np.array([0]*4000, np.uint8)

    dupes = []
    for x in inp:
        y = x - 1
        pos, offset = y / 8, y % 8
        if (bitmap[pos] >> offset) & 1 == 1:
            dupes.append(x)
        else:
            bitmap[pos] |= 1 << offset

    return dupes


def test_findDuplicates():
    'test for findDuplicates'
    from random import randint

    inp = range(1, 32001)

    dupes = [randint(1, 32000) for _ in range(20)]

    inp.extend(dupes)

    res = findDuplicates(inp)

    assert sorted(dupes) == sorted(res)
    print 'Test passed'

if __name__ == '__main__':
    test_findDuplicates()


