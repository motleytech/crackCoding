'''
Implementation of queue via 2 stacks
'''
from stack import Stack

class QueueViaStacks(object):
    def __init__(self):
        self.s1, self.s2 = Stack(), Stack()

    def pop(self):
        if self.s1.isEmpty() and self.s2.isEmpty():
            raise Exception("Queue empty. 'pop' failed.")
        if self.s2.isEmpty():
            while not self.s1.isEmpty():
                self.s2.push(self.s1.pop())

        return self.s2.pop()

    def push(self, value):
        self.s1.push(value)
        return self

if __name__ == '__main__':
    def test():
        from random import randint
        qvs = QueueViaStacks()
        values = [randint(1, 100) for x in range(3)]
        ignore = [qvs.push(x) for x in values]

        assert qvs.pop() == values[-3]
        qvs.push(2000)
        assert qvs.pop() == values[-2]
        assert qvs.pop() == values[-1]
        assert qvs.pop() == 2000

        print 'test passed'

    test()


