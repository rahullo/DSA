#How will you find the middle of the linked list?

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


def findMiddleOfList(head):
    curr = prev = head
    i = 0
    while curr and curr.next:
        if i == 0:
            curr = curr.next 
            i+=1
        elif i == 1:
            curr = curr.next 
            prev = prev.next 
            i= 0

        # curr = curr.next.next 
        # prev = prev.next 
    return prev

display(head)
print(findMiddleOfList(head).data)