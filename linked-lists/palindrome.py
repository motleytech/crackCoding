from llist import LinkedList, Node

def isPalindrome(lst):
    nodes = list(lst)
    for x, y in zip(nodes, reversed(nodes)):
        if x.data != y.data:
            return False
    return True

def isPalin2(lst, curr):
    if curr.next is None:
        return (curr.data == lst.data, lst.next)
    res, node = isPalin2(lst, curr.next)
    if not res:
        return (False, None)
    return (node.data == curr.data, node.next)


lst = LinkedList()
lst.add(1).add(2).add(3)
print isPalindrome(lst), isPalin2(lst.head, lst.head)[0]
lst.add(2).add(1)

print isPalindrome(lst), isPalin2(lst.head, lst.head)[0]


