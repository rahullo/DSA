# How will you display a linked list from the end?

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)

def display(head):
    curr = head
    while curr:
        print(curr.data, end=" -> ")
        curr = curr.next
    print(None, '\n')

def reversedLinkedList(head):
    if head == None:
        return
    
    reversedLinkedList(head.next)
    print(head.data, end='->')

reversedLinkedList(head)