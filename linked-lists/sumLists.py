
from llist import LinkedList, Node, createRandomList

def sumLists(lst1, lst2):
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

lst1 = createRandomList(4, 8)
lst2 = createRandomList(5, 8)

print lst1
print lst2
slist = sumLists(lst1, lst2)
print slist

def listToNum(lst):
    lst = reversed([n.data for n in lst])
    return reduce(lambda a, b: a*10 + b, lst, 0)

def testSumLists(lst1, lst2, sm):
    res1, res2 , ress = map(listToNum, [lst1, lst2, sm])
    assert(res1 + res2 == ress)
    print "test passed"

testSumLists(lst1, lst2, slist)




