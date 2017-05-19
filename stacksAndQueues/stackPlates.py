'''
implementation of the stack of plates
'''

class StackOfPlates(object):
    '''The stack of plates class'''
    def __init__(self, maxSize):
        '''self explanatory'''
        self.stacks = []
        self.maxSize = maxSize

    def pop(self):
        '''remove and return the last added value'''
        if len(self.stacks) == 0:
            raise Exception("Stack empty. 'pop' failed.")

        value = self.stacks[-1].pop()
        while len(self.stacks) > 0 and len(self.stacks[-1]) == 0:
            self.stacks.pop()
        return value

    def push(self, value):
        '''insert a new value at the last stack'''
        if len(self.stacks) == 0:
            self.stacks.append([])
        if len(self.stacks[-1]) >= self.maxSize:
            self.stacks.append([])
        self.stacks[-1].append(value)
        return self

    def popAt(self, index):
        '''remove and return the last value from stack at pos index'''
        if len(self.stacks) <= index:
            raise Exception('No sub-stack at index %s.' % index)

        value = self.stacks[index].pop()
        if len(self.stacks[index]) == 0:
            self.stacks.pop(index)
        return value

    def __str__(self):
        if len(self.stacks) == 0:
            return '< stack empty >'
        return "\n".join(str((i, str(x))) for i, x in enumerate(self.stacks))

if __name__ == '__main__':
    def test():
        '''test for Stack of Plates class'''
        sop = StackOfPlates(2)

        sop.push(5).push(3).push(6).push(2).push(9).push(11)
        print sop

        assert sop.pop() == 11
        assert sop.popAt(0) == 3
        assert sop.popAt(1) == 2

        print sop

        print 'test passed'

    test()
