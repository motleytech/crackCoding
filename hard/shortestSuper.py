'solution for the shortest supersequence problem'

from collections import defaultdict

def setDiff(d1, d2):
    'return elements in the diff of d1 and d2'
    res = set()
    for x, y in d1.items():
        if y > d2[x]:
            res.add(x)
    return res

def findMinSubseq(a, b):
    'find shortest subseq in b which has all elements of a'
    aset = set(a)
    info = []
    score = defaultdict(lambda: 0)
    minSeq = (len(b), 0, len(b))
    for i, x in enumerate(b):
        if x in aset:
            cscore = score.copy()
            score[x] += 1
            for j, oscore in reversed(info):
                if setDiff(score, oscore) == aset:
                    if i - j < minSeq[0]:
                        minSeq = (i - j, j, i)
                    break
            info.append((i, cscore))
    return minSeq[1:]

def test():
    'test for method findMinSubseq'
    a = [1, 5, 9]
    b = [7, 5, 9, 0, 2, 1, 3, 5, 7, 9, 1, 1, 5, 8, 8, 9, 7]
    assert findMinSubseq(a, b) == (7, 10)

    print 'Passed'

if __name__ == '__main__':
    test()
