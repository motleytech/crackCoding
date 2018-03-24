'''
class to provide deadlock free locks

The solution uses networkx for detect a loop in the directed graph
formed by list of locks
'''

import networkx as nx

class DeadFreeLocks(object):
    '''class to check if lock order can cause deadlocks'''
    def __init__(self):
        'init method'
        self.orders = []

    def requestLockOrder(self, order):
        'verify that the requested lock order wont cause deadlocks'
        if len(order) == 1:
            return True
        links = []
        for od in self.orders:
            links.extend(list(zip(od, od[1:])))

        links.extend(list(zip(order, order[1:])))

        graph = nx.DiGraph(links)
        try:
            loops = nx.find_cycle(graph)
        except:
            loops = []
        if len(loops) > 0:
            return False
        self.orders.append(order)
        return True

def main():
    dfl = DeadFreeLocks()

    assert dfl.requestLockOrder([1, 2, 3, 4]) == True
    assert dfl.requestLockOrder([1, 3, 5]) == True
    assert dfl.requestLockOrder([7, 5, 9, 2]) == False


if __name__ == '__main__':
    main()
    print 'done'


