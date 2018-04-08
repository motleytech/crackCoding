'''
method to return hits / pseudo-hits for a given an instance of prob/solution
in a game of master mind
'''

from collections import defaultdict

def getHits(prob, sol):
    'returns hits and pseudo hits for prob/sol'
    pdict, sdict = defaultdict(lambda: 0), defaultdict(lambda: 0)
    hits = 0
    for pc, sc in zip(prob, sol):
        if pc != sc:
            pdict[pc] += 1
            sdict[sc] += 1
        else:
            hits += 1

    phits = 0
    for c, v in sdict.items():
        phits += min(pdict[c], v)

    return hits, phits

def test():
    'test for getHits method'
    assert getHits('rgby', 'ggrr') == (1, 1)
    assert getHits('RGGB', 'YRGB') == (2, 1)
    print 'done'

if __name__ == '__main__':
    test()
