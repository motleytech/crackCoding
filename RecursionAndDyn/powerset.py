'find powerset of a given sequence/set'

def powerset(a):
    '''uses bit strings to create powerset'''
    la = list(a)
    pset = []
    for x in range(2**len(la)):
        xx = bin(x)[2:]
        cset = [la[i] for i, y in enumerate(reversed(xx)) if y == '1']
        pset.append(cset)
    return pset

def powerset2(a, st):
    '''uses recursion to create powerset'''
    if st == -1:
        return [[]]
    else:
        pset = powerset2(a, st-1)
        return pset + [x + [a[st]] for x in pset]

def test_powerset():
    'test for the powerset methods'
    N = 4
    inp = range(N)
    pset1 = powerset(inp)
    print pset1
    assert len(pset1) == 2**(len(inp))

    pset2 = powerset2(inp, len(inp) - 1)
    print pset2
    assert len(pset2) == 2**(len(inp))

    assert pset1 == pset2

    print '\nTest passed'

if __name__ == '__main__':
    test_powerset()

