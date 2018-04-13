'solution for pairs with sum problem'

def findPairsWithSum(a, sm):
    'returns pais from a that sum to sm'
    pairs = set()
    aset = set(a)
    smb2 = 'dummy'
    if not sm % 2:
        smb2 = sm/2

    for x in aset:
        if x == smb2:
            if a.count(x) > 1:
                pairs.add((x, x))
            continue
        if sm - x in aset:

            pairs.add((x, sm - x) if x < (sm - x) else (sm-x, x))
    return pairs

def test():
    'test for findPairsWithSum'
    arr = range(30) + range(5)
    assert sorted(findPairsWithSum(arr, 10)) == [(0, 10), (1, 9), (2, 8), (3, 7), (4, 6)]

    print 'Passed'

if __name__ == '__main__':
    test()
