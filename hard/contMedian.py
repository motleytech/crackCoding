'solution for the continuous median problem'

class Heap(object):
    'Min/Max heap class'
    def __init__(self, minType=True):
        self.heapType = minType
        self.data = [None]

    def push(self, value):
        'insert data into heap'
        self.data.append(value if self.heapType else -value)
        self.heapifyBack()

    def pop(self):
        'remove min/max element from min/max heap'
        if len(self.data) <= 1:
            raise Exception("Can't pop from empty heap")
        result = self.data[1]
        self.data[1] = self.data.pop()
        self.heapifyFront()
        return result if self.heapType else -result

    def peek(self):
        'look at the root element without removing it'
        if len(self.data) <= 1:
            raise Exception("Can't peek from empty heap")
        return self.data[1] if self.heapType else -self.data[1]


    def __len__(self):
        'return number of items in heap'
        return len(self.data) - 1

    def heapifyBack(self):
        'maintain heap property starting at last element'
        d = self.data
        index = len(self.data) - 1
        parent = index / 2
        while True:
            if d[index] < d[parent]:
                d[index], d[parent] = d[parent], d[index]
            index, parent = parent, parent / 2
            if parent == 0:
                break

    def heapifyFront(self):
        'maintain heap property starting at first element'
        d = self.data
        curr = 1
        left, right = 2*curr, 2*curr + 1
        ld = len(d) - 1
        while left <= ld:

            if right > ld:
                if d[left] < d[curr]:
                    d[curr], d[left] = d[left], d[curr]
                break
            else:
                if d[curr] < d[left] and d[curr] < d[right]:
                    break

                if d[curr] > d[left] or d[curr] > d[right]:
                    if d[left] < d[right]:
                        d[curr], d[left] = d[left], d[curr]
                        curr = left
                    else:
                        d[curr], d[right] = d[right], d[curr]
                        curr = right
                    left, right = 2*curr, 2*curr + 1
                else:
                    break

class MedianTracker(object):
    'Track the median as data is added continuosly'
    def __init__(self):
        self.lowers = Heap(minType=False)
        self.highers = Heap()

    def add(self, value):
        'add a new value'
        if len(self.lowers):
            if value <= self.lowers.peek():
                self.lowers.push(value)
                if len(self.lowers) > len(self.highers) + 1:
                    self.highers.push(self.lowers.pop())
            else:
                self.highers.push(value)
                if len(self.highers) > len(self.lowers):
                    self.lowers.push(self.highers.pop())
        else:
            self.lowers.push(value)

    def median(self):
        'return the current median value'
        if len(self.lowers) == len(self.highers):
            return (self.lowers.peek() + self.highers.peek()) / 2.0
        return self.lowers.peek()


def slowMedian(data):
    'method for aiding in testing - calculates median by sorting'
    data = sorted(data)
    ld2 = len(data) / 2
    if len(data) % 2:
        return data[ld2]
    return (data[ld2] + data[ld2 - 1]) / 2.0

def test():
    'test for method placeholder'
    from random import randint

    for _ in range(20):
        mTracker = MedianTracker()
        data = []
        for _ in range(100):
            y = randint(1, 100)
            data.append(y)
            mTracker.add(y)

            m1, m2 = mTracker.median(), slowMedian(data)
            assert m1 == m2

if __name__ == '__main__':
    test()
    print 'Passed'
