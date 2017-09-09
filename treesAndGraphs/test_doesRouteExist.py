'Tests for doesRouteExist.py file'

# pylint: skip-file

from doesRouteExist import routeExists
from treeAndGraph import DirectedGraph
import unittest

class RouteExistsTests(unittest.TestCase):
    '''test class'''
    def test_trivial0(self):
        edges = []
        graph = DirectedGraph(edges)

        assert routeExists(graph, 1, 1)
        assert routeExists(graph, 1, 2) == False

    def test_trivial1(self):
        edges = [(1, 2)]
        graph = DirectedGraph(edges)

        assert routeExists(graph, 1, 1)
        assert routeExists(graph, 1, 2)
        assert routeExists(graph, 2, 1) == False

    def test_trivial2(self):
        edges = [(1, 2), (2, 3), (3, 1)]
        graph = DirectedGraph(edges)

        assert routeExists(graph, 1, 3)
        assert routeExists(graph, 2, 1)
        assert routeExists(graph, 1, 4) == False

    def test_trivial3(self):
        edges = [(1, 2), (2, 3), (4, 5)]
        graph = DirectedGraph(edges)

        assert routeExists(graph, 1, 4) == False
        assert routeExists(graph, 1, 5) == False
        assert routeExists(graph, 3, 1) == False
        assert routeExists(graph, 1, 3)


if __name__ == '__main__':
    unittest.main()
    print 'done'
