'''Given a directed graph, design an algorithm to
find out whether there is a route between two nodes.'''

from Queue import Queue
from logging import error

def bfs(graph, a, b):
    'breadth first search which returns shortest path'
    if a == b: # same nodes, so path is trivial
        return True, [a]

    toVisit = Queue()
    toVisit.put(a)
    seen = set()
    previous = {}
    found = False

    while not found and (not toVisit.empty()):
        c = toVisit.get()
        for d in graph.getNeighbors(c):
            if d in seen:
                continue
            previous[d] = c
            if d == b:
                found = True
                break
            toVisit.put(d)
            seen.add(d)

    if not found:
        return False, []

    path = computePath(a, b, previous)
    if path is None:
        error("Error in tracing path")
        return False, []
    return True, path


def computePath(a, b, previous):
    '''given nodes a and b and a map of previous nodes
    visited in the bfs, returns path from a to b'''
    path = [b]
    prev = previous.get(b, None)
    while prev and prev != a:
        path.append(prev)
        prev = previous.get(prev, None)

    if prev is None:
        return None

    path.append(a)
    path = list(reversed(path))
    return path


def routeExists(graph, a, b):
    '''
    Returns True if there is a path between nodes a and
    b in the graph
    Else, returns False
    '''
    return bfs(graph, a, b)[0]

if __name__ == '__main__':
    from treeAndGraph import DirectedGraph
    edges = [(1, 2), (2, 3), (3, 1)]
    graph1 = DirectedGraph(edges)
    print bfs(graph1, 2, 1)
