'''
return the sum of 2 lists where each node corresponds to a digit
'''

from llist import LinkedList, Node, createRandomList

def sumLists(lst1, lst2):
    '''
    find sum of the input lists and output as a list
    '''
    curr1, curr2 = lst1.head, lst2.head
    result = LinkedList()
    carry = 0
    while curr1 is not None and curr2 is not None:
        res = curr1.data + curr2.data + carry
        carry = res / 10
        res = res % 10
        result.add(Node(res))
        curr1 = curr1.next
        curr2 = curr2.next
    rem = curr1 if curr2 is None else curr2

    while rem is not None:
        res = rem.data + carry
        carry = 0
        if res > 9:
            res = res - 10
            carry = 1
        result.add(Node(res))
        rem = rem.next
    return result


def listToNum(lst):
    '''
    convert list to a number
    '''
    lst = reversed([n.data for n in lst])
    return reduce(lambda a, b: a*10 + b, lst, 0)

def testSumLists():
    '''
    test for sumLists method
    '''
    lst1 = createRandomList(4, 8)
    lst2 = createRandomList(5, 8)

    slist = sumLists(lst1, lst2)

    res1, res2, ress = map(listToNum, [lst1, lst2, slist])
    assert res1 + res2 == ress
    print "test passed"

if __name__ == '__main__':
    testSumLists()
