from collections import defaultdict

class DirectedGraph(object):
    def __init__(self, edges):
        self.edges = edges
        self.nodes = nodes = set()
        self.adjList = adjList = defaultdict(lambda : [])

        for a, b in edges:
            adjList[a].append(b)
            nodes.add(a)
            nodes.add(b)

    def getNeighbors(self, node):
        return tuple(self.adjList.get(node, []))

    def getNodes(self):
        return tuple(self.nodes)

    def getEdges(self):
        return tuple(self.edges)

    def getNumNodes(self):
        return len(self.nodes)

    def getNumEdges(self):
        return len(self.edges)
