from llist import LinkedList, Node

def isPalindrome(lst):
    nodes = list(lst)
    for x, y in zip(nodes, reversed(nodes)):
        if x.data != y.data:
            return False
    return True

lst = LinkedList()
lst.add(1).add(2).add(3)
print isPalindrome(lst)
lst.add(2).add(1)

print isPalindrome(lst)


