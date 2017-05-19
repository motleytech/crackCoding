'''
sorting a stack
'''

from stack import Stack

def sortStack(st):
    '''
    sort the given stack using another temporary stack
    '''
    tempStack = Stack() # with max at top

    while not st.isEmpty():
        topSt = st.pop()
        count = 0
        while (not tempStack.isEmpty()) and tempStack.peek() > topSt:
            st.push(tempStack.pop())
            count += 1

        tempStack.push(topSt)
        while count > 0:
            tempStack.push(st.pop())
            count -= 1

    while not tempStack.isEmpty():
        st.push(tempStack.pop())
    return

if __name__ == '__main__':
    def test():
        '''
        test for sortStack method
        '''
        st = Stack()
        st.push(4).push(1).push(8).push(2).push(9)

        sortStack(st)

        assert st.pop() == 1
        assert st.pop() == 2
        assert st.pop() == 4
        assert st.pop() == 8
        print 'test passed'

    test()
