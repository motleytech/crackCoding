'''Contains tree and graph classes'''

from collections import defaultdict

class DirectedGraph(object):
    '''directed graph class'''
    def __init__(self, edges):
        'init the class'
        self.edges = edges
        self.nodes = nodes = set()
        self.adjList = adjList = defaultdict(lambda : [])

        for a, b in edges:
            adjList[a].append(b)
            nodes.add(a)
            nodes.add(b)

    def getNeighbors(self, node):
        'return neighbors of given node'
        return tuple(self.adjList.get(node, []))

    def getNodes(self):
        'return all nodes in the graph'
        return tuple(self.nodes)

    def getEdges(self):
        'return all edges in the graph'
        return tuple(self.edges)

    def getNumNodes(self):
        'return total number of nodes in graph'
        return len(self.nodes)

    def getNumEdges(self):
        'return total number of edges in graph'
        return len(self.edges)
