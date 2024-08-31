class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(3)
list1.next.next.next = ListNode(4)
list1.next.next.next.next = ListNode(5)
list1.next.next.next.next.next = ListNode(6)


def printList(head):
    if head == None:
        return 
    
    print(head.val, end='->')
    printList(head.next)


def removeNthFromEnds(head, n):
    count = 0
    curr = head
    while curr:
        curr = curr.next 
        count +=1

    i = count - n
    curr = head
    prev = None
    for j in range(i):
        prev = curr
        curr = curr.next 
    
    print('curr->', curr.val, ', prev->', prev.val)
    temp = curr.next 
    prev.next = temp
    return head

printList(list1)
print('\n')
printList(removeNthFromEnds(list1, 2))
print('\n')
printList(list1)
