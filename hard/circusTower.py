'find the max circus tower height'

from itertools import combinations
from collections import defaultdict

class Person(object):
    'class to hold person attributes'
    def __init__(self, h, w):
        self.h = h
        self.w = w

    def __gt__(self, other):
        if self.h > other.h and self.w > other.w:
            return True
        return False

    def __repr__(self):
        return "Person(%s, %s)" % (self.h, self.w)

    def __eq__(self, other):
        if self.h == other.h and self.w == other.w:
            return True
        return False


def findMaxTowerHeight(inp):
    'find the max tower height'
    ppl = [Person(h, w) for h, w in inp]

    graph = defaultdict(lambda: [])

    for a, b in combinations(ppl, 2):
        if a > b:
            graph[a].append(b)
        if b > a:
            graph[b].append(a)

    return findMaxHeightGraph(graph)


def explore(g, v, known):
    'explore the graph at a Person v, and return dist and path to farthest Person'
    maxDist, maxPath = 0, [v]
    for v2 in g[v]:
        if v2 in known:
            dist, cpath = known[v2]
        else:
            dist, cpath = explore(g, v2, known)
        if dist > maxDist:
            maxDist = dist
            maxPath = [v] + cpath

    known[v] = len(maxPath), maxPath
    return known[v]

def findMaxHeightGraph(graph):
    'find the max height / width of the directed graph'
    known = {}
    fake = Person(1000000, 1000000)
    graph[fake] = graph.keys()
    d, path = explore(graph, fake, known)
    return d - 1, path[1:]


def test():
    'Test for findMaxTowerHeight method'
    inp = [(65, 100), (70, 150), (56, 90), (75, 190), (60, 95), (68, 110)]
    assert findMaxTowerHeight(inp) == (6, [
        Person(75, 190),
        Person(70, 150),
        Person(68, 110),
        Person(65, 100),
        Person(60, 95),
        Person(56, 90)
    ])
    print 'Passed'

if __name__ == '__main__':
    test()
