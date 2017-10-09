'''generate permutations of a given string'''


def permutationsUnique(seq):
    '''iterate though permutations of a seq containing
    unique elements'''
    def _recurPerms(unused, curr):
        if len(unused) == 0:
            yield ''.join(curr)
        else:
            for x in unused.copy():
                unused.remove(x)
                curr.append(x)
                for y in _recurPerms(unused, curr):
                    yield y
                curr.pop()
                unused.add(x)

    return _recurPerms(set(seq), [])

def permutations(seq, curr=None):
    '''iterate through permuations of seq containing
    unique or duplicates'''
    if len(seq) == 0:
        yield ''.join(curr)
    for i, x in enumerate(seq):
        if i > 0:
            if x == seq[i-1]:
                continue
        nseq = seq[:i] + seq[i+1:]
        curr.append(x)
        for y in permutations(nseq, curr):
            yield y
        curr.pop()


def test_permutations():
    '''test for both permutation methods'''
    inp = 'sqnc'
    pgen = permutationsUnique(inp)
    data1 = [x for x in pgen]

    p2gen = permutations(inp, [])
    data2 = [x for x in p2gen]

    assert len(data1) == len(data2)
    assert sorted(data1) == sorted(data2)

    inp = 'aabc'
    p3gen = permutations(inp, [])
    data3 = [x for x in p3gen]

    assert len(data3) == 12

    inp = 'aaabc'
    p3gen = permutations(inp, [])
    data3 = [x for x in p3gen]

    assert len(data3) == 20

    inp = 'aabbc'
    p3gen = permutations(inp, [])
    data3 = [x for x in p3gen]

    assert len(data3) == 30

    print 'Test passed'


if __name__ == '__main__':
    test_permutations()


