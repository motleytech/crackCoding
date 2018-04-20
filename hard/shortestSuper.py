
from collections import defaultdict

def setDiff(d1, d2):
    res = set()
    for x, y in d1.items():
        z = d2[x]
        if y - z > 0:
            res.add(x)
    return res

def findMinSubseq(a, b):
    'find shortest subseq in b which has all elements of a'
    aset = set(a)
    info = []
    score = defaultdict(lambda: 0)
    minSeq = (len(b), 0, len(b))
    for i, x in enumerate(b):
        score[x] += 1
        if x in aset:
            nscore = score.copy()
            for j, oscore in reversed(info):
                if setDiff(nscore, oscore) == aset:
                    if i - j < minSeq[0]:
                        minSeq = (i - j, j, i)
                    break
            info.append((i, nscore))
    return minSeq

def test():
    'test for method findMinSubseq'
    pass

if __name__ == '__main__':
    test()
