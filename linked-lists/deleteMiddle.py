from llist import LinkedList, createRandomList

lst = createRandomList(6, 100)
print lst

def deleteMiddle(node):
    if node.next:
        node.copy(node.next)
        node.next = node.next.next


nodes = list(lst)
deleteMiddle(nodes[3])
print lst
