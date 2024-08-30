class ListNode:
    def __init__(self, val = 0, next=None):
        self.val = val
        self.next = next


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)

def printList(head):
    curr = head
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next
    print('\n')



def reverseList_1(head):
    new_head = ListNode(head.val)
    curr = head.next
    while curr:
        newNode = ListNode(curr.val)
        newNode.next = new_head
        new_head = newNode
        curr = curr.next
    return new_head

def reverseList(head):
    prev, curr = None, head
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev

printList(head)

rev = reverseList(head)

printList(rev)