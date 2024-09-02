# Split a Circular Linked List into two equal parts. If the number of nodes in the
# list are odd then make first list one node extra than second list.

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
head.next.next.next.next.next.next = head

def display(head):
    curr = head
    while curr.next != head:
        print(curr.data, end=" -> ")
        curr = curr.next
    print(curr.data, '->',None, '\n')


def splitLinkedList(head):
    slow = head
    fast = head 
    
    while fast.next != head and fast.next.next != head:
        slow = slow.next 
        fast = fast.next.next 

    # if fast.next.next and fast.next != head:
    #     fast = fast.next

    if fast.next.next == head:
        fast = fast.next 

    print('slow-> ', slow.data, ', fast-> ', fast.data)
    head1 = head

    if head.next != head:
        head2 = slow.next 
    
    fast.next = slow.next 

    slow.next = head

    return head1, head2


display(head)
h1, h2 = splitLinkedList(head)
display(h1)
display(h2)