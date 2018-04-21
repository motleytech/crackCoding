'solution for the word transformer problem'

from collections import defaultdict
from itertools import combinations

def areOneAway(a, b):
    'true if a and b differ in only 1 character'
    if len(a) != len(b):
        return False
    diff = 0
    for x, y in zip(a, b):
        if x != y:
            diff += 1
    return diff == 1

def transWord(data, a, b):
    'find the transformation from a to b, if one exists in data'
    # create graph from words in data
    dset = set(data)
    graph = defaultdict(set)

    for x, y in combinations(dset, 2):
        if areOneAway(x, y):
            graph[x].add(y)
            graph[y].add(x)

    visited = set()
    done = False
    toVisit = set([a])
    prev = {}
    while toVisit:
        curr = toVisit.pop()
        visited.add(curr)
        for nxt in graph[curr]:
            if nxt not in visited:
                prev[nxt] = curr
                toVisit.add(nxt)
            if nxt == b:
                prev[nxt] = curr
                done = True
                break
        if done:
            break
    if b not in prev:
        return False, []

    path = [b]
    nxt = prev.get(b)
    while nxt:
        path.append(nxt)
        nxt = prev.get(nxt)
    return list(reversed(path))

def test():
    'test for method transWord'
    data = ["DAMP", "LAMP", "LIMP", 'LIME', 'LIKE']
    a = 'DAMP'
    b = 'LIKE'

    res = transWord(data, a, b)

    assert res == ["DAMP", "LAMP", "LIMP", 'LIME', 'LIKE']


if __name__ == '__main__':
    test()
    print 'Passed'
