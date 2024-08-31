#Insert a node in a sorted linked list

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
# head.next.next.next = Node(4)
head.next.next.next = Node(5)
head.next.next.next.next = Node(6)

def display(head):
    curr = head
    while curr:
        print(curr.data, end=" -> ")
        curr = curr.next
    print(None, '\n')


def insertInSorted(head, node):
    curr = head

    if node <= curr.data:
        newNode = Node(node)
        newNode.next = curr
        head = newNode
        return head
    
    prev = None
    while curr:
        if curr.data >= node:
            newNode = Node(node)
            prev.next = newNode
            newNode.next = curr
            return head
        prev = curr
        curr = curr.next 
    return head

display(head)
insertInSorted(head, -1)
display(insertInSorted(head, -1))
