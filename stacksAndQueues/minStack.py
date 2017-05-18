'''
implementation of a min stack
'''

class MinStack(object):
    '''
    The min stack class implementation
    '''
    def __init__(self):
        '''init method'''
        self.stack = []

    def pop(self):
        '''remove and return last inserted element'''
        if len(self.stack) == 0:
            raise Exception("Stack empty. 'pop' failed.")

        return self.stack.pop()[0]

    def push(self, value):
        '''add new element to the end of the stack'''
        if len(self.stack) == 0:
            cmin = value
        else:
            cmin = min(self.stack[-1][1], value)
        self.stack.append((value, cmin))
        return self

    def peek(self):
        '''return last inserted element'''
        if len(self.stack) == 0:
            raise Exception("Stack empty. 'peek' failed.")

        return self.stack[-1][0]

    def min(self):
        '''return the min value in the stack'''
        if len(self.stack) == 0:
            raise Exception("Stack empty. 'min' failed.")

        return self.stack[-1][1]

if __name__ == '__main__':
    import unittest
    from exceptions import Exception

    class MyTest(unittest.TestCase):
        def test1(self):
            ms = MinStack()
            self.assertRaises(Exception, ms.min)
            self.assertRaises(Exception, ms.pop)

            ms.push(5).push(3).push(9).push(2).push(-3).push(34).push(33)

            assert ms.min() == -3
            print 'test passed'

    unittest.main()
