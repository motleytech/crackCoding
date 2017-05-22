'''
create 3 stacks in a single array

first implement it by allocating 1/3 of the array to each stack
'''

class Stack(object):
    def __init__(self, buf, startIndex, size):
        self.buf = buf
        self.startIndex = startIndex
        self.maxSize = size
        self.top = self.startIndex

    def pop(self):
        if self.top == self.startIndex:
            raise Exception("Cannot pop from empty stack")
        self.top -= 1
        return self.buf[self.top]

    def push(self, item):
        if self.maxSize <= (self.top - self.startIndex):
            raise Exception("Stack is full")
        self.buf[self.top] = item
        self.top += 1

    def isEmpty(self):
        return self.top == self.startIndex

def createThreeStacks(size):
    if (size % 3 > 0):
        raise ValueError("size parameter must be divisible by 3")

    buf = [None]*size
    stackSize = size / 3

    stacks = [Stack(buf, stackSize*x, stackSize) for x in range(3)]
    return stacks



class ThreeStacks(object):
    def __init__(self, size):
        self.buf = [None] * size
        self.size = size
        self.sizes = [size/3] * 3
        self.startIndices = [x * (size / 3) for x in range(3)]
        self.tops = self.startIndices[:]

    def pop(self, stackIndex):
        if self.tops[stackIndex] == self.startIndices[stackIndex]:
            raise Exception("Cannot pop from empty stack")
        self.tops[stackIndex] = (self.tops[stackIndex] - 1) % self.size
        return self.tops[stackIndex]



