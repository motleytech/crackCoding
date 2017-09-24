"""find a build order of projects, given the dependencies of the projects"""

from collections import defaultdict

class TopoGraph(object):
    '''
    Graph class which implements some methods which help
    to implement topological sort
    '''
    def __init__(self, nodes, edges):
        '''init method'''
        self.nodes = set(nodes)
        self.nodes_no_inc = self.nodes.copy()
        self.edges = set(edges)

        self.inc_edges = defaultdict(lambda : set())
        self.outgoing_edges = defaultdict(lambda : set())

        for a, b in edges:
            if b in self.nodes_no_inc:
                self.nodes_no_inc.remove(b)
            self.inc_edges[b].add((a, b))
            self.outgoing_edges[a].add((a, b))

    def removeEdge(self, edge):
        '''remove an edge from the graph'''
        a, b = edge
        try:
            self.edges.remove(edge)
            self.inc_edges[b].remove(edge)
            self.outgoing_edges[a].remove(edge)
            if len(self.inc_edges[b]) == 0:
                self.nodes_no_inc.add(b)
        except:
            from traceback import print_exc
            print_exc()

    def getNodeWithNoInc(self):
        '''return a node which has no incoming edges'''
        try:
            node = self.nodes_no_inc.pop()
            return node
        except KeyError:
            return None

    def getOutgoingEdges(self, node):
        '''return all outgoing edges from node'''
        return self.outgoing_edges[node].copy()


def findOrder(projects, edges):
    """
    finds order using Kahn's algorithm
    Algo runs in order O(v+e)
    """
    graph = TopoGraph(projects, edges)
    order = []
    nni = graph.getNodeWithNoInc()
    while nni:
        order.append(nni)
        edges = graph.getOutgoingEdges(nni)
        for edge in edges:
            graph.removeEdge(edge)
        nni = graph.getNodeWithNoInc()

    if len(graph.edges) > 0:
        return None
    return order


def test_findOrder():
    '''
    Test for the findOrder method
    '''
    from pprint import pprint as pp

    projects = ['a', 'b', 'c', 'd', 'e', 'f']
    dependencies = '(a, d), (f, b), (b, d), (f, a), (d, c), (c, e)'


    dependencies = dependencies.replace('), (', ')#(').replace(', ', ',').replace('(', '').replace(')', '').split('#')
    links = [tuple(x.split(',')) for x in dependencies]

    order = findOrder(projects, links)

    if order is None:
        print "No order possible. Dependency loop exists."
    else:
        print "Found Build order:\n%s" % (order, )


if __name__ == '__main__':
    test_findOrder()
