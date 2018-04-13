def findPairsWithSum(a, sm):
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
        if (sm - x) in aset:

            pairs.add((x, sm - x) if x < (sm - x) else (sm-x, x))
    return pairs

def test():
    arr = range(30) + range(5)

    print findPairsWithSum(arr, 10)

if __name__ == '__main__':
    test()



